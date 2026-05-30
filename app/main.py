from fastapi import FastAPI
from app.models import Event

app = FastAPI(
    title="Store Intelligence API"
)

# Temporary in-memory storage
events_db = []

@app.get("/")
def home():

    return {
        "message": "Store Intelligence API Running"
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

@app.post("/events/ingest")
def ingest_event(event: Event):

    event_data = event.model_dump()

    events_db.append(event_data)

    print("=" * 50)
    print("EVENT RECEIVED")
    print(event_data)
    print(f"TOTAL EVENTS: {len(events_db)}")
    print("=" * 50)

    return {
        "message": "Event Ingested",
        "total_events": len(events_db)
    }
@app.get("/events")
def get_events():

    return {
        "count": len(events_db),
        "events": events_db
    }

@app.get("/metrics")
def metrics():

    total_entries = sum(
        1
        for e in events_db
        if e["event_type"] == "ENTRY"
    )

    total_exits = sum(
        1
        for e in events_db
        if e["event_type"] == "EXIT"
    )

    active_visitors = total_entries - total_exits

    return {
        "total_entries": total_entries,
        "total_exits": total_exits,
        "active_visitors": active_visitors,
        "total_events": len(events_db)
    }

@app.get("/funnel")
def funnel():

    entries = sum(
        1 for e in events_db
        if e["event_type"] == "ENTRY"
    )

    zone_visits = sum(
        1 for e in events_db
        if e["event_type"] == "ZONE_ENTER"
    )

    purchases = sum(
        1 for e in events_db
        if e["event_type"] == "PURCHASE"
    )

    conversion_rate = 0

    if entries > 0:
        conversion_rate = (
            purchases / entries
        ) * 100

    return {
        "entered_store": entries,
        "visited_zone": zone_visits,
        "purchases": purchases,
        "conversion_rate": round(
            conversion_rate,
            2
        )
    }

@app.get("/anomalies")
def anomalies():

    anomalies = []

    entries = sum(
        1 for e in events_db
        if e["event_type"] == "ENTRY"
    )

    purchases = sum(
        1 for e in events_db
        if e["event_type"] == "PURCHASE"
    )

    if purchases > entries:

        anomalies.append(
            "Purchases exceed entries"
        )

    return {
        "anomalies": anomalies
    }