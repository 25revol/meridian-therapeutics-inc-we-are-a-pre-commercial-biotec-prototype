from datetime import datetime, timezone

def ts(s):
    return datetime.fromisoformat(s).replace(tzinfo=timezone.utc).isoformat()

SEED_DATA = {
    "documents": [
        {"id": "DOC-001", "title": "Master Batch Record — MTX-204 Drug Substance", "type": "Master Batch Record", "status": "Effective", "version": "3.1", "owner": "J. Nakamura", "effective_date": ts("2024-09-15"), "next_review": ts("2025-09-15"), "system": "MasterControl"},
        {"id": "DOC-002", "title": "SOP-QA-017: Deviation Investigation and Reporting", "type": "SOP", "status": "Effective", "version": "2.4", "owner": "R. Osei", "effective_date": ts("2024-06-01"), "next_review": ts("2025-06-01"), "system": "MasterControl"},
        {"id": "DOC-003", "title": "SOP-MFG-042: Aseptic Fill-Finish Operations", "type": "SOP", "status": "In Review", "version": "1.8", "owner": "L. Ferreira", "effective_date": None, "next_review": None, "system": "MasterControl"},
        {"id": "DOC-004", "title": "Validation Protocol — VP-2024-011: Process Validation Stage 2", "type": "Validation Protocol", "status": "Approved", "version": "1.0", "owner": "S. Patel", "effective_date": ts("2024-11-01"), "next_review": ts("2026-11-01"), "system": "Veeva Vault"},
        {"id": "DOC-005", "title": "Analytical Method Transfer Plan — HPLC Potency Assay", "type": "Method Transfer Plan", "status": "Effective", "version": "2.0", "owner": "C. Liu", "effective_date": ts("2024-08-20"), "next_review": ts("2025-08-20"), "system": "SharePoint"},
        {"id": "DOC-006", "title": "SOP-QC-009: Out-of-Specification Investigation", "type": "SOP", "status": "Effective", "version": "3.0", "owner": "R. Osei", "effective_date": ts("2024-03-10"), "next_review": ts("2025-03-10"), "system": "MasterControl"},
        {"id": "DOC-007", "title": "Risk Assessment — RA-2024-004: BLA-Enabling Process Changes", "type": "Risk Assessment", "status": "Draft", "version": "0.3", "owner": "S. Patel", "effective_date": None, "next_review": None, "system": "SharePoint"},
    ],
    "capas": [
        {"id": "CAPA-2024-031", "title": "Bioburden exceedance in DS bulk hold — root cause correction", "source": "Deviation DEV-2024-088", "status": "In Progress", "priority": "Critical", "owner": "L. Ferreira", "opened_date": ts("2024-10-04"), "due_date": ts("2025-01-15"), "effectiveness_check": None, "linked_lot": "LOT-DS-2408"},
        {"id": "CAPA-2024-028", "title": "HPLC column qualification gaps identified during audit", "source": "Internal Audit AUD-2024-003", "status": "Open", "priority": "Major", "owner": "C. Liu", "opened_date": ts("2024-09-18"), "due_date": ts("2024-12-31"), "effectiveness_check": None, "linked_lot": None},
        {"id": "CAPA-2024-019", "title": "Environmental monitoring trending — Grade B particle counts", "source": "EM Trend Report Q2-2024", "status": "Effectiveness Check", "priority": "Major", "owner": "J. Nakamura", "opened_date": ts("2024-07-02"), "due_date": ts("2024-11-30"), "effectiveness_check": ts("2024-11-28"), "linked_lot": None},
        {"id": "CAPA-2024-012", "title": "SOP revision cycle overdue — 14 documents past review date", "source": "QMR Q1-2024", "status": "Closed", "priority": "Minor", "owner": "R. Osei", "opened_date": ts("2024-04-15"), "due_date": ts("2024-08-01"), "effectiveness_check": ts("2024-08-05"), "linked_lot": None},
        {"id": "CAPA-2024-036", "title": "Label reconciliation discrepancy — DP lot release", "source": "Deviation DEV-2024-101", "status": "Open", "priority": "Critical", "owner": "L. Ferreira", "opened_date": ts("2024-11-12"), "due_date": ts("2025-02-01"), "effectiveness_check": None, "linked_lot": "LOT-DP-2411"},
    ],
    "lots": [
        {"id": "LOT-DS-2408", "product": "MTX-204 Drug Substance", "lot_number": "DS-2408-001", "stage": "Drug Substance", "status": "Quarantine", "manufactured_date": ts("2024-08-14"), "release_date": None, "expiry_date": ts("2025-08-14"), "disposition": "Pending Investigation", "linked_capa": "CAPA-2024-031"},
        {"id": "LOT-DS-2406", "product": "MTX-204 Drug Substance", "lot_number": "DS-2406-002", "stage": "Drug Substance", "status": "Released", "manufactured_date": ts("2024-06-22"), "release_date": ts("2024-07-30"), "expiry_date": ts("2025-06-22"), "disposition": "Approved", "linked_capa": None},
        {"id": "LOT-DP-2411", "product": "MTX-204 Drug Product", "lot_number": "DP-2411-001", "stage": "Drug Product", "status": "Quarantine", "manufactured_date": ts("2024-11-05"), "release_date": None, "expiry_date": ts("2025-11-05"), "disposition": "Pending Label Review", "linked_capa": "CAPA-2024-036"},
        {"id": "LOT-DP-2409", "product": "MTX-204 Drug Product", "lot_number": "DP-2409-003", "stage": "Drug Product", "status": "Released", "manufactured_date": ts("2024-09-10"), "release_date": ts("2024-10-02"), "expiry_date": ts("2025-09-10"), "disposition": "Approved", "linked_capa": None},
        {"id": "LOT-CTM-2410", "product": "MTX-204 Clinical Trial Material", "lot_number": "CTM-2410-001", "stage": "CTM Fill-Finish", "status": "Released", "manufactured_date": ts("2024-10-18"), "release_date": ts("2024-11-01"), "expiry_date": ts("2025-04-18"), "disposition": "Approved — Phase 2 Study MT-204-002", "linked_capa": None},
    ],
}