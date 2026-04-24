from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

app = FastAPI(title="Meridian Therapeutics QMS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CAPAS = [
    {"id": "CAPA-001", "title": "OOS Result - Sterility Test Lot 2201", "status": "Open", "priority": "Critical", "owner": "J. Patel", "due_date": "2024-08-15"},
    {"id": "CAPA-002", "title": "Environmental Monitoring Excursion Suite B", "status": "In Review", "priority": "High", "owner": "S. Chen", "due_date": "2024-08-22"},
    {"id": "CAPA-003", "title": "SOP Deviation - Gowning Procedure", "status": "Closed", "priority": "Medium", "owner": "R. Torres", "due_date": "2024-07-30"},
    {"id": "CAPA-004", "title": "Equipment Calibration Overdue - HPLC Unit 3", "status": "Open", "priority": "High", "owner": "M. Liu", "due_date": "2024-09-01"},
    {"id": "CAPA-005", "title": "Supplier Audit Finding - Raw Material Vendor", "status": "In Progress", "priority": "Medium", "owner": "J. Patel", "due_date": "2024-09-10"},
]

CHANGE_CONTROLS = [
    {"id": "CC-001", "title": "Introduce PAT for In-Process Monitoring", "status": "Approved", "category": "Process", "initiated_by": "D. Kim", "effective_date": "2024-09-01"},
    {"id": "CC-002", "title": "Update Aseptic Fill SOP v4.2", "status": "Pending Approval", "category": "Document", "initiated_by": "S. Chen", "effective_date": "2024-08-28"},
    {"id": "CC-003", "title": "Column Resin Change - Protein A Purification", "status": "Under Review", "category": "Material", "initiated_by": "R. Torres", "effective_date": "2024-10-15"},
    {"id": "CC-004", "title": "New QC Instrument Qualification - LC-MS/MS", "status": "Draft", "category": "Equipment", "initiated_by": "M. Liu", "effective_date": "2024-11-01"},
    {"id": "CC-005", "title": "Revised Batch Release Criteria for Drug Substance", "status": "Approved", "category": "Specification", "initiated_by": "J. Patel", "effective_date": "2024-08-01"},
]

BATCH_RECORDS = [
    {"id": "BR-2401", "product": "MTX-101 Drug Substance", "lot": "DS-2401", "status": "Released", "manufactured": "2024-07-01", "release_date": "2024-07-18", "yield_pct": 94.2},
    {"id": "BR-2402", "product": "MTX-101 Drug Substance", "lot": "DS-2402", "status": "Under Review", "manufactured": "2024-07-15", "release_date": None, "yield_pct": 91.8},
    {"id": "BR-2403", "product": "MTX-101 Drug Product", "lot": "DP-2401", "status": "Released", "manufactured": "2024-07-20", "release_date": "2024-08-05", "yield_pct": 97.1},
    {"id": "BR-2404", "product": "MTX-101 Drug Product", "lot": "DP-2402", "status": "On Hold", "manufactured": "2024-08-01", "release_date": None, "yield_pct": 88.3},
    {"id": "BR-2405", "product": "MTX-101 Drug Substance", "lot": "DS-2403", "status": "In Manufacturing", "manufactured": "2024-08-10", "release_date": None, "yield_pct": None},
]

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "Meridian Therapeutics QMS API", "version": "1.0.0"}

@app.get("/api/capas")
def get_capas():
    return {"data": CAPAS, "total": len(CAPAS)}

@app.get("/api/capas/{capa_id}")
def get_capa(capa_id: str):
    for c in CAPAS:
        if c["id"] == capa_id:
            return c
    return {"error": "CAPA not found"}, 404

@app.get("/api/change-controls")
def get_change_controls():
    return {"data": CHANGE_CONTROLS, "total": len(CHANGE_CONTROLS)}

@app.get("/api/batch-records")
def get_batch_records():
    return {"data": BATCH_RECORDS, "total": len(BATCH_RECORDS)}

@app.get("/api/stats")
def get_stats():
    open_capas = sum(1 for c in CAPAS if c["status"] in ("Open", "In Progress"))
    critical_capas = sum(1 for c in CAPAS if c["priority"] == "Critical")
    pending_cc = sum(1 for c in CHANGE_CONTROLS if c["status"] in ("Pending Approval", "Under Review", "Draft"))
    released_batches = sum(1 for b in BATCH_RECORDS if b["status"] == "Released")
    on_hold_batches = sum(1 for b in BATCH_RECORDS if b["status"] == "On Hold")
    avg_yield = round(
        sum(b["yield_pct"] for b in BATCH_RECORDS if b["yield_pct"] is not None)
        / sum(1 for b in BATCH_RECORDS if b["yield_pct"] is not None), 1
    )
    return {
        "open_capas": open_capas,
        "critical_capas": critical_capas,
        "pending_change_controls": pending_cc,
        "released_batches": released_batches,
        "on_hold_batches": on_hold_batches,
        "avg_batch_yield_pct": avg_yield,
        "total_capas": len(CAPAS),
        "total_change_controls": len(CHANGE_CONTROLS),
        "total_batch_records": len(BATCH_RECORDS),
    }