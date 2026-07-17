"""Synthetic end-to-end test of the structured code extraction.

Takes a real snapshot from snapshots/ (falls back to an embedded excerpt of
the same file so CI never depends on snapshot churn), reshapes it into the
PDF snapshot format ([[page N]] markers), perturbs a copy the way a real
manual revision would, and runs the actual diff path (SnapshotStore.handle).

Asserts the heuristic's contract:
  - real codes on changed lines are caught (99213 CPT with code vocabulary,
    Z30.011 ICD-10-CM, G2012 HCPCS, modifier 25);
  - false-positive bait is excluded (SF zip 94110 on a line with no code
    vocabulary, year 2026);
  - page anchors come from the nearest preceding [[page N]] marker and are
    rendered as url#page=N deep links in the diff report;
  - the per-page 'Page updated' stamp capture serializes and diffs by page.
"""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from source_check import (  # noqa: E402
    SnapshotStore, extract_code_entries, snapshot_page_map,
    parse_page_stamps, stamp_change_detail, stamps_display,
    revision_changes,
)

REAL_SNAPSHOT = REPO / "snapshots" / "fqhc" / "fqhc_cms_center.txt"
# Excerpt of snapshots/fqhc/fqhc_cms_center.txt (2026-07-16) so the fixture
# is stable even if the live snapshot is re-baselined or removed.
FALLBACK_LINES = [
    "FQHC Information Center | CMS Skip to main content",
    "Centers for Medicare & Medicaid Services CMS Newsroom",
    "Popular terms Physician Fee Schedule Local Coverage Determination",
    "Telehealth Covid-19 Agents and Brokers CMS.gov main menu Medicare",
    "Enrollment & renewal Original Medicare (Part A and B) Eligibility",
    "Annual Medicare Participation Announcement Providers & suppliers",
    "Medicare Managed Care Eligibility and Enrollment",
    "Health plans Health plan enrollment Medigap (Medicare Supplement)",
    "Coordination of benefits Prescription drug coverage",
    "Employer services Provider enrollment Opt out of Medicare",
    "Electronic prescribing Revalidation Managed care marketing",
    "Provider compliance programs Waived tests Demonstration projects",
]

SOURCE_URL = "https://example.org/manual-section.pdf"


def base_lines() -> list[str]:
    if REAL_SNAPSHOT.exists():
        lines = [ln for ln in
                 REAL_SNAPSHOT.read_text(encoding="utf-8").splitlines()
                 if ln.strip()][:12]
        if len(lines) >= 12:
            return lines
    return FALLBACK_LINES


def make_old_and_new() -> tuple[str, str]:
    real = base_lines()
    old = (["[[page 1]]"] + real[:6]
           + ["Telehealth billing code G2012 rate update pending"]
           + ["[[page 2]]"] + real[6:12])
    new = list(old)
    # removal: the HCPCS-code line disappears from page 1
    new.remove("Telehealth billing code G2012 rate update pending")
    # additions on page 2: real codes plus false-positive bait
    new += [
        "CPT code 99213 office visit, established patient, now reimbursable",
        "Use modifier 25 when billed with a significant separate service",
        "Diagnosis Z30.011, encounter for initial prescription of "
        "contraceptive pills",
        "Mail to San Francisco CA 94110 effective in 2026",
    ]
    return "\n".join(old), "\n".join(new)


def run_diff(tmp_path: Path) -> tuple[str, SnapshotStore]:
    store = SnapshotStore(tmp_path / "snapshots", tmp_path / "diffs")
    old_text, new_text = make_old_and_new()
    p = store._path("fpact", "synthetic_doc")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(old_text, encoding="utf-8")
    report = store.handle("fpact", "synthetic_doc", "CHANGED",
                          {"snapshot_text": new_text}, SOURCE_URL)
    assert report, "CHANGED with a prior snapshot must produce a diff report"
    return Path(report).read_text(encoding="utf-8"), store


def test_codes_table_catches_real_codes_and_pages(tmp_path):
    content, store = run_diff(tmp_path)
    table = content.split("## Text diff")[0]

    assert "| `99213` | CPT | added | high |" in table
    assert "Z30.011" in table
    assert "| `G2012` | HCPCS | removed | high |" in table
    assert "| `25` | modifier |" in table

    # page anchors: G2012 was removed from page 1, 99213 added on page 2
    assert f"[p.1]({SOURCE_URL}#page=1)" in table
    assert f"[p.2]({SOURCE_URL}#page=2)" in table

    entries = {e["code"]: e for e in store.codes["synthetic_doc"]}
    assert entries["99213"]["page"] == 2
    assert entries["G2012"]["page"] == 1


def test_false_positive_bait_is_excluded(tmp_path):
    content, store = run_diff(tmp_path)
    table = content.split("## Text diff")[0]
    codes = {e["code"] for e in store.codes["synthetic_doc"]}

    assert "94110" not in codes and "94110" not in table   # SF zip, no vocab
    assert "2026" not in codes                              # year
    assert not any(c.startswith("20") and len(c) == 4 for c in codes)


def test_five_digit_needs_vocab():
    diff = ["--- previous", "+++ current",
            "+Send payment of 12345 dollars to the district office",
            " unrelated context line",
            "+Procedure code 93000 electrocardiogram added to schedule"]
    entries = extract_code_entries(diff)
    codes = {e["code"]: e for e in entries}
    assert "12345" not in codes            # amount, no vocab anywhere near
    assert codes["93000"]["confidence"] == "high"          # vocab on the line


def test_page_map_nearest_preceding_marker():
    pm = snapshot_page_map("[[page 1]]\nalpha\n[[page 3]]\nbeta")
    assert pm == {"alpha": 1, "beta": 3}


def test_page_stamp_roundtrip_and_diff():
    s = "p1: May 2026|p2: May 2026|p4: November 2024"
    assert parse_page_stamps(s) == {1: "May 2026", 2: "May 2026",
                                    4: "November 2024"}
    assert parse_page_stamps("May 2026") is None            # legacy format
    assert parse_page_stamps("") == {}
    assert stamps_display(s) == "May 2026 (p1-2); November 2024 (p4)"
    # portal revision dates and legacy values pass through unchanged
    assert stamps_display("2025-05-23T00:02:23") == "2025-05-23T00:02:23"

    detail = stamp_change_detail(s, "p1: May 2026|p2: June 2026|p5: June 2026")
    assert "page 2: 'May 2026' -> 'June 2026'" in detail
    assert "page 5 now stamped 'June 2026'" in detail
    assert "page 4 stamp removed (was 'November 2024')" in detail
    assert "page 1" not in detail                           # unchanged page
    # legacy fallback keeps the raw before/after
    assert stamp_change_detail("May 2026", s) == f"'May 2026' -> '{s}'"


def test_revision_changes_names_moved_sections():
    prev = {"rural": {"title": "RHC/FQHC (rural)",
                      "revision_date": "2026-06-16T15:00:00"},
            "tarf": {"title": "TAR Form (tarf)",
                     "revision_date": "2023-08-06T01:58:46"},
            "gone": {"title": "Retired Section",
                     "revision_date": "2022-01-01T00:00:00"}}
    cur = {"rural": {"title": "RHC/FQHC (rural)",
                     "revision_date": "2026-07-16T16:54:22"},
           "tarf": {"title": "TAR Form (tarf)",
                    "revision_date": "2023-08-06T01:58:46"},
           "fresh": {"title": "Brand New Section",
                     "revision_date": "2026-07-01T09:00:00"}}
    out = revision_changes(prev, cur)
    assert "'RHC/FQHC (rural)' revised 2026-06-16 -> 2026-07-16" in out
    assert "new section 'Brand New Section' (2026-07-01)" in out
    assert "section removed: 'Retired Section'" in out
    assert len(out) == 3                    # unchanged tarf not mentioned
    assert revision_changes(cur, cur) == []
