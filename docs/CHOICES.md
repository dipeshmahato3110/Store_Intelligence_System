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


# Choices - 2026-06-01

## Analytics Architecture

- Chose FastAPI as analytics backend.
- Chose in-memory storage for prototype phase.
- Chose YOLOv8 tracking for visitor detection.
- Chose zone-based customer journey tracking.
- Chose POS CSV ingestion before database integration.

## POS Analytics

- Added purchases endpoint.
- Added brand sales endpoint.
- Added revenue endpoint.

# Choices - 2026-06-02

## Event-Driven Dwell Analytics

### Decision

Moved dwell analytics from local Python memory to FastAPI event ingestion.

Previous:

detect.py
→ visitor_dwell list

New:

detect.py
→ DWELL Event
→ FastAPI
→ events_db

### Reason

* Eliminates process isolation issues
* Aligns with event-driven architecture
* Makes analytics APIs independent of detection process
* Easier future migration to PostgreSQL

---

## Zone Performance KPI

### Decision

Created zone-performance analytics combining:

* Visitor Count
* Average Dwell Time
* Revenue
* Purchases

### Reason

Retail managers need business KPIs rather than raw tracking data.

The KPI provides:

Zone
→ Engagement
→ Revenue
→ Conversion Signals

---

## Zone Stability Filter

### Problem

Visitors standing near zone boundaries generated false transitions.

Example:

DERMDOC
→ MINIMALIST
→ DERMDOC
→ MINIMALIST

### Decision

Require multiple consecutive detections before accepting a zone transition.

### Reason

* Reduces tracking noise
* Produces cleaner journeys
* Improves dwell accuracy
* Improves conversion analytics

---

## Submission Strategy

Focus shifted from feature development to:

* Documentation
* Demo preparation
* Screenshots
* Presentation

Reason:

Core analytics platform is functionally complete and submission-ready.


# Choices - 2026-06-02

## Data Persistence

Selected:

* SQLite database
* Local file-based storage

Reason:

* Persistent storage across FastAPI restarts
* Lightweight and easy to deploy
* No external database dependency for prototype phase

Future:

* PostgreSQL migration

---

## Dashboard Architecture

Selected:

* Server-side HTML dashboard
* Bootstrap 5 UI
* Chart.js visualizations

Reason:

* Rapid development
* Easy reviewer access
* Minimal frontend complexity

---

## Dashboard KPIs

Selected:

* Total Revenue
* Total Orders
* Total Visitors
* Conversion Rate

Reason:

* Provides immediate business visibility
* Aligns with retail analytics objectives

---

## Dashboard Visualizations

Selected:

* Brand Revenue Bar Chart
* Zone Performance Chart
* Revenue Distribution Pie Chart
* Top Brands Table

Reason:

* Enables quick identification of top-performing brands
* Supports zone-level performance analysis
* Improves business insight communication

---

## Zone Stability Filtering

Selected:

* Zone transition smoothing
* Consecutive zone confirmation before transition

Reason:

* Reduces false zone switches near boundaries
* Improves customer journey accuracy
* Produces more reliable dwell analytics

---

## Submission Strategy

Selected:

* Complete end-to-end analytics pipeline
* Working dashboard demonstration
* POS integration
* Documentation and presentation

Reason:

* Demonstrates complete business workflow
* Maximizes evaluation coverage
* Provides clear reviewer experience
