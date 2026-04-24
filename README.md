# Meridian Therapeutics QMS Prototype

**One quality system built for BLA-stage GMP**

Connect your controlled documents, CAPA workflows, and LIMS data in a single
audit-ready environment as you scale toward BLA-enabling activities.

---

## Overview

This prototype demonstrates a unified Quality Management System (QMS) for
Meridian Therapeutics, Inc. — purpose-built to address the fragmentation pain
of transitioning from early-stage to late-stage GMP as BLA-enabling activities
approach.

---

## Tech Stack

| Layer | Technology |
|------------|------------------------------|
| Frontend | React + Vite + Tailwind CSS |
| Backend | FastAPI (Python 3.12) |
| Database | PostgreSQL via Supabase |
| Infra | Docker Compose |

---

## Prerequisites

- Docker Desktop (v4.20+)
- Node.js 18+ (for local frontend dev)
- Python 3.12+ (for local backend dev)

---

## Quick Start

```bash
# 1. Clone the repo
git clone <repo-url> && cd meridian-qms

# 2. Copy environment variables
cp .env.example .env
# Edit .env with your Supabase credentials

# 3. Start all services
docker compose up --build

# 4. Seed demo data
docker compose exec backend python seed.py
```

Frontend → http://localhost:5173
Backend API → http://localhost:8000
API Docs → http://localhost:8000/docs

---

## Key Endpoints

| Method | Path | Description |
|--------|------------|-------------|
| GET | /api/health | Health check |

---

## Demo Overview

1. **Dashboard** — StatsRow surfaces open CAPAs, pending document reviews,
   and lot disposition counts at a glance. DataTable lists all quality records
   ingested from connected systems.

2. **Controlled Documents** — Track document lifecycle from draft through
   approved, with version history and owner assignment.

3. **CAPA Workflow** — Create, assign, and close corrective actions with
   linked root-cause evidence and effectiveness checks.

> Empty state copy: *"No records yet. Controlled documents, CAPAs, and lot
> data will appear here once ingested from your connected systems."*

---

## Folder Structure

```
├── frontend/      # React + Vite app
├── backend/       # FastAPI application
├── docker-compose.yml
└── .env.example
```

---

## Notes

This is a prototype for internal evaluation. Not intended for production GMP
use without full validation per 21 CFR Part 11 / Annex 11 requirements.