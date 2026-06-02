# Store Intelligence System

## Purplle Tech Challenge 2026

An AI-powered retail analytics platform that transforms CCTV footage and Point-of-Sale (POS) transactions into actionable store intelligence.

The system combines computer vision, customer journey analytics, dwell-time analysis, conversion intelligence, and sales analytics to help retailers understand customer behavior and optimize in-store performance.

---

# Problem Statement

Retail stores often lack visibility into:

* Customer movement patterns
* Brand engagement
* Dwell behavior
* Purchase conversion
* Revenue contribution by store zones

Traditional CCTV systems only provide recordings and do not generate actionable business insights.

---

# Solution

Store Intelligence System converts CCTV footage and POS transactions into real-time analytics.

### Analytics Pipeline
```text
CCTV Cameras

        ↓

YOLOv8 Person Detection

        ↓

Multi-Object Tracking

        ↓

Entry Detection

        ↓

Zone Detection

        ↓

Journey Analytics

        ↓

Dwell Analytics

        ↓

POS Purchase Integration

        ↓

Brand Conversion Intelligence

        ↓

Dashboard
```
---

# Features

## Computer Vision

* YOLOv8 Person Detection
* Multi-Object Tracking
* Entry Detection
* Zone Detection
* Visitor Identification

## Customer Analytics

* Footfall Analytics
* Visitor Journey Tracking
* Dwell Time Analysis
* Zone Performance Analytics
* Conversion Analytics

## POS Analytics

* CSV Purchase Integration
* Brand Revenue Analytics
* Top Brand Analysis
* Revenue Intelligence

## Backend

* FastAPI APIs
* Event Ingestion
* Analytics Endpoints
* SQLite Persistence

## Dashboard

* KPI Cards
* Revenue Analytics
* Zone Performance Charts
* Revenue Distribution Charts
* Top Brands Table
* Responsive UI

---

# Architecture

```text
CCTV Cameras
        ↓
YOLOv8 Detection
        ↓
Tracking
        ↓
Event Generation
        ↓
FastAPI Backend
        ↓
Analytics Layer
        ↓
SQLite Storage
        ↓
Dashboard
```

---

# Analytics Modules

## Entry Analytics

Detects customers entering the store using virtual line crossing.

Metrics:

* Total Entries
* Active Visitors

---

## Journey Analytics

Tracks movement of visitors across store zones.

Example:

```text
Visitor_101

ENTRY
↓
GOOD_VIBES
↓
DERMDOC
↓
FACES_CANADA
↓
PURCHASE
```

---

## Dwell Analytics

Measures time spent in each zone.

Metrics:

* Average Dwell Time
* Zone Engagement
* Brand Interaction Duration

---

## Conversion Analytics

Measures relationship between visitors and purchases.

Metrics:

* Total Visitors
* Checkout Visitors
* Conversion Rate

---

## POS Analytics

Integrated with Purplle POS CSV dataset.

Processed Fields:

* Order ID
* Product Name
* Brand Name
* Quantity
* GMV
* Salesperson

Generated Metrics:

* Revenue
* Purchases
* Brand Sales
* Top Brands

---

# Dashboard

Dashboard provides:

### KPI Cards

* Revenue
* Orders
* Visitors
* Conversion %

### Visualizations

* Brand Revenue Chart
* Zone Performance Chart
* Revenue Distribution Pie Chart

### Reports

* Top Brands
* Purchase Analytics
* Revenue Analytics

---

# API Endpoints

## Core Analytics

```text
GET /health
GET /events
GET /metrics
```

## Customer Analytics

```text
GET /journeys
GET /dwell
GET /conversion
```

## POS Analytics

```text
GET /purchases
GET /brands
GET /top-brands
GET /revenue
```

## Zone Intelligence

```text
GET /zone-performance
GET /zone-performance-v2
GET /dwell-v2
```

---

# Technology Stack

Frontend

* HTML
* Bootstrap 5
* Chart.js

Backend

* FastAPI
* Pydantic

Computer Vision

* YOLOv8
* OpenCV

Data Processing

* Pandas

Storage

* SQLite

Language

* Python

---

# Project Structure

```text
# Project Structure

```text
store-intelligence/

├── app/
│   ├── database.py
│   ├── db_models.py
│   ├── main.py
│   └── models.py
│
├── data/
│   ├── pos/
│   │   ├── Brigade Road - Store Data.xlsx
│   │   └── Brigade_Bangalore.csv
│   │
│   └── videos/
│       ├── CAM 1.mp4
│       ├── CAM 2.mp4
│       ├── CAM 3.mp4
│       ├── CAM 4.mp4
│       ├── CAM 5.mp4
│       ├── sample.mp4
│       ├── sample1.mp4
│       └── sample2.mp4
│
├── docs/
│   ├── CHOICES.md
│   └── DESIGN.md
│
├── pipeline/
│   ├── __init__.py
│   ├── analytics.py
│   ├── conversion.py
│   ├── detect.py
│   ├── dwell.py
│   ├── journey.py
│   ├── load_pos.py
│   ├── purchase_analytics.py
│   ├── send_dwell_event.py
│   ├── send_event.py
│   ├── send_zone_event.py
│   └── zones.py
│
├── templates/
│   └── dashboard.html
│
├── tests/
│
├── .gitignore
├── docker-compose.yml
├── README.md
├── requirements.txt
├── store_intelligence.db
├── yolov8n.pt
```

```

---

# How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

## Open Dashboard

```text
http://127.0.0.1:8000/dashboard
```

---

# Current Status

## Completed

* YOLO Detection
* Multi-Object Tracking
* Entry Analytics
* Zone Analytics
* Journey Analytics
* Dwell Analytics
* Conversion Analytics
* POS Integration
* Brand Revenue Analytics
* SQLite Persistence
* Dashboard UI

---

# Future Improvements

* Multi-Camera Fusion
* PostgreSQL Integration
* Real-Time Streaming
* Heatmaps
* Staff Analytics
* Predictive Analytics
* Cloud Deployment

---

# Business Impact

Store Intelligence System transforms raw CCTV footage into actionable retail insights by connecting customer behavior with purchase outcomes.

Retail teams can identify:

* High-performing brands
* High-engagement zones
* Revenue-driving categories
* Conversion opportunities

This enables data-driven store optimization and improved customer experience.

---

## Purplle Tech Challenge 2026

Built as a retail intelligence platform combining Computer Vision, Analytics, and Business Intelligence.
