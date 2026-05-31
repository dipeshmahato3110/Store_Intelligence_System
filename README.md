# Purplle Tech Challenge 2026 – Store Intelligence System

## Overview

An AI-powered retail analytics platform that transforms CCTV footage into actionable store intelligence.

The system combines computer vision, event-driven architecture, customer journey analytics, dwell analytics, conversion analytics, and POS sales integration to generate real-time retail insights.

---

## Features

### Computer Vision

* YOLOv8 Person Detection
* Multi-Object Tracking
* Entry Detection
* Zone Detection
* Customer Journey Tracking

### Analytics

* Visitor Tracking
* Footfall Metrics
* Customer Journey Analytics
* Dwell Time Analytics
* Zone Analytics
* Conversion Analytics
* Brand Analytics
* Revenue Analytics
* Purchase Analytics

### Backend

* FastAPI
* Event Ingestion API
* Metrics API
* Funnel Analytics API
* Journey Analytics API
* Dwell Analytics API
* Conversion Analytics API
* Purchase Analytics API
* Brand Analytics API
* Revenue Analytics API

---

## Architecture

CCTV Cameras
→ YOLOv8 Detection
→ Person Tracking
→ Entry Detection
→ Zone Detection
→ Event Generation
→ FastAPI Backend
→ Analytics Layer
→ Business Intelligence APIs

---

## API Endpoints

### System

* GET /health

### Events

* GET /events
* POST /events/ingest

### Visitor Analytics

* GET /metrics
* GET /journeys
* GET /dwell
* GET /conversion

### POS Analytics

* GET /purchases
* GET /brands
* GET /revenue

### Business Analytics

* GET /funnel
* GET /anomalies

---

## Current Status

### Completed

* YOLOv8 Detection Pipeline
* Multi-Object Tracking
* Entry Event Detection
* Zone Detection
* Customer Journey Tracking
* Dwell Analytics
* Conversion Analytics
* FastAPI Backend
* Event Ingestion API
* Purchase Analytics
* Brand Analytics
* Revenue Analytics
* POS CSV Integration

### In Progress

* Brand Conversion Analytics
* Multi-Camera Analytics
* Zone Stability Filtering
* Dashboard Development

### Planned

* Multi-Camera Visitor Re-Identification
* Real-Time Dashboard
* Database Persistence
* Advanced Retail Insights

---

## Tech Stack

### AI / Computer Vision

* Python
* YOLOv8
* OpenCV

### Backend

* FastAPI
* Pydantic

### Analytics

* Pandas
* NumPy

### Data Sources

* CCTV Video Streams
* POS Transaction Data (CSV)

---

## Challenge

Purplle Tech Challenge 2026 – Round 2

Store Intelligence System using CCTV Analytics, Customer Journey Intelligence, POS Integration, and Real-Time Event Processing.
