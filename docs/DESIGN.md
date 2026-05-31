# design.md

## Date

2026-05-31

## Store Intelligence System Design

### High-Level Architecture

┌─────────────┐
│ CCTV Cameras│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ YOLOv8      │
│ Detection   │
│ Tracking    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Event Layer │
│ Entry Event │
│ Zone Event  │
│ Purchase    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ FastAPI     │
│ Ingestion   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Analytics   │
│ Metrics     │
│ Dwell Time  │
│ Conversion  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Dashboard   │
└─────────────┘

---

## Current Implementation Status

### Completed

#### Detection

* YOLOv8 person detection

#### Tracking

* Persistent visitor IDs

#### Entry Analytics

* Virtual line crossing
* Entry event generation

#### API Layer

* FastAPI service
* Health endpoint
* Event ingestion endpoint
* Events endpoint
* Metrics endpoint

#### Metrics

* Total entries
* Total exits
* Active visitors
* Total events

#### Zone Foundation

* Zone module created
* Zone lookup function created
* Zone labels rendered on tracked visitors

---

## Store Camera Layout

### CAM1

Purpose:

* Main customer interaction analytics

Brands:

* Maybelline
* Faces Canada
* Lakme
* Swiss Beauty
* Alps
* Mars

Outputs:

* Zone visit events
* Dwell analytics

---

### CAM2

Purpose:

* Skincare wall analytics

Brands:

* Face Shop
* Good Vibes
* Derma Co
* Minimalist
* Aqualogica

Outputs:

* Zone visit events
* Dwell analytics

---

### CAM3

Purpose:

* Store entry analytics

Outputs:

* Entry events
* Footfall counting

---

### CAM4

Purpose:

* Storage room

Status:

* Excluded from analytics

---

### CAM5

Purpose:

* Cash counter

Outputs:

* Purchase correlation
* Queue analytics

---

## Next Development Phase

### Zone Analytics

Implement:

* Real zone polygons
* Zone transitions
* Zone entry events

Example:

Visitor 101
→ MAYBELLINE
→ LAKME
→ PURCHASE

---

### Dwell Time Engine

Track:

visitor_id
zone_id
enter_time
exit_time
duration

Output:

Zone dwell reports

---

### POS Integration

Inputs:

* Transaction CSV
* SKU data
* Brand data
* GMV

Output:

Brand conversion metrics

---

### Final KPI Layer

Metrics:

* Footfall
* Unique visitors
* Zone visits
* Dwell time
* Purchase count
* Conversion rate
* Revenue by zone
* Revenue by brand

Goal:

Transform raw CCTV footage into actionable retail intelligence.


# Design Update - 2026-06-01

## Implemented

- Customer Journey Tracking
- Dwell Time Analytics
- Conversion Analytics
- Purchase Analytics
- Brand Sales Analytics
- Revenue Analytics

## API Endpoints

/health
/events
/journeys
/dwell
/conversion
/purchases
/brands
/revenue
