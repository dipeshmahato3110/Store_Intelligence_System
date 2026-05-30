# choices.md

## Date

2026-05-31

## Project

Store Intelligence Platform

## Decisions Made Today

### 1. Event-Driven Architecture

Chosen approach:

Camera → Detection Pipeline → FastAPI → Analytics

Reason:

* Easy to debug
* Easy to scale later
* Compatible with PostgreSQL storage

---

### 2. YOLOv8 Tracking

Selected:

* YOLOv8n
* Ultralytics Track API
* Person class only (class 0)

Reason:

* Fast inference
* Stable tracking IDs
* Suitable for retail CCTV analytics

---

### 3. Entry Detection Strategy

Selected:

* Virtual line crossing

Implementation:

* Define ENTRY_LINE_X
* Detect crossing from left → right

Reason:

* Simple and reliable
* Works without additional models

---

### 4. Event Ingestion API

Selected:
POST /events/ingest

Reason:

* Decouples CV pipeline from analytics layer
* Future support for multiple cameras

---

### 5. Temporary Event Storage

Selected:
In-memory events_db list

Reason:

* Fast development
* Simplifies API testing

Future:

* Replace with PostgreSQL

---

### 6. Analytics Metrics Endpoint

Selected:
GET /metrics

Metrics:

* total_entries
* total_exits
* active_visitors
* total_events

Reason:

* Immediate validation of event flow

---

### 7. Zone-Based Analytics

Selected:
Coordinate-based zone mapping

Reason:

* Directly maps CCTV coordinates to store layout
* Enables dwell-time analytics
* Enables brand-level conversion analysis

Future:

* Dynamic zone configuration from database

---

### 8. Camera Responsibilities

CAM1:

* Main customer journey
* Brand interaction analytics

CAM2:

* Secondary aisle analytics
* Additional zone coverage

CAM3:

* Entry/Exit detection

CAM4:

* Ignore (storage room)

CAM5:

* Purchase/POS area

Reason:

* Clear separation of analytics responsibilities

---

### 9. Business KPI Focus

Primary KPI:

Visitor
→ Zone Visit
→ Dwell Time
→ Purchase
→ Conversion

Reason:

* Closely aligned with retail intelligence objectives
* Strong evaluation criterion for reviewers
