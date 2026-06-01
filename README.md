# Purplle Tech Challenge 2026 – Store Intelligence System

## Overview

Store Intelligence System is an AI-powered retail analytics platform that converts CCTV footage into actionable business intelligence.

The system uses Computer Vision, Event-Driven Architecture, and POS Analytics to track customer movement, analyze engagement, measure dwell time, and generate store performance insights.

---

## Problem Statement

Retail stores generate large volumes of customer interaction data, but most of it remains unused.

The objective is to:

* Track customer movement inside stores
* Measure zone engagement
* Generate customer journeys
* Calculate dwell times
* Analyze conversions
* Connect in-store behavior with POS sales data

---

## Features

### Computer Vision

* YOLOv8 Person Detection
* Multi-Object Tracking
* Entry Detection
* Zone Detection
* Customer Journey Tracking
* Dwell Time Analytics
* Zone Stability Filtering

### Event Processing

* ENTRY Events
* ZONE_ENTER Events
* DWELL Events
* Event Ingestion API
* Real-Time Analytics

### Business Analytics

* Customer Journeys
* Footfall Metrics
* Zone Performance Analytics
* Revenue Analytics
* Brand Analytics
* Conversion Analytics
* Top Brand Analysis

### POS Integration

* Purchase Data Loading
* Revenue Analysis
* Brand Revenue Mapping
* Zone Revenue Analytics

---

## Architecture

CCTV Cameras
→ YOLOv8 Detection
→ Multi Object Tracking
→ Zone Detection
→ Event Generation
→ FastAPI Backend
→ Analytics Engine
→ Business Intelligence APIs

---

## Tech Stack

* Python
* YOLOv8
* OpenCV
* FastAPI
* Pandas
* Pydantic

---

## APIs

### Analytics APIs

* /journeys
* /dwell-v2
* /conversion
* /revenue
* /top-brands
* /zone-brand-revenue
* /zone-performance-v2

### System APIs

* /events
* /metrics
* /health

---

## Results

* Customer Journey Tracking
* Zone Engagement Measurement
* Revenue Intelligence
* Brand Performance Analytics
* Event Driven Retail Analytics

---

## Future Improvements

* Multi-Camera Analytics
* Cross-Camera Re-Identification
* PostgreSQL Persistence
* Real-Time Dashboard
* Predictive Store Analytics

---

## Challenge

Purplle Tech Challenge 2026

Store Intelligence System using CCTV Analytics and Real-Time Event Processing.
