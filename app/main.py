from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.database import get_connection
from collections import defaultdict
from pipeline.load_pos import load_pos_data
from collections import defaultdict
from pipeline.purchase_analytics import (
    purchase_events,
    brand_sales,
    brand_purchases
)

from app.db_models import create_tables

create_tables()

from fastapi import FastAPI
from app.models import Event
from pipeline.analytics import (
    visitor_journeys,
    visitor_dwell,
    total_visitors,
    checkout_visitors
)

app = FastAPI(
    title="Store Intelligence API"
)

templates = Jinja2Templates(
    directory="templates"
)

print(templates)

load_pos_data()

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

@app.get("/journeys")
def get_journeys():

    journeys = {}

    for event in events_db:

        if event["event_type"] != "ZONE_ENTER":
            continue

        visitor = event["visitor_id"]
        zone = event["zone_id"]

        if visitor not in journeys:
            journeys[visitor] = []

        if (
            len(journeys[visitor]) == 0
            or journeys[visitor][-1] != zone
        ):
            journeys[visitor].append(zone)

    return {
        "count": len(journeys),
        "journeys": journeys
    }

@app.get("/dwell")
def get_dwell():

    dwell_records = []

    for event in events_db:

        if event["event_type"] == "DWELL":

            dwell_records.append(
                {
                    "visitor_id":
                        event["visitor_id"],

                    "zone":
                        event["zone_id"],

                    "seconds":
                        round(
                            event["dwell_ms"]
                            / 1000,
                            2
                        )
                }
            )

    return {
        "count": len(
            dwell_records
        ),
        "records": dwell_records
    }

@app.get("/conversion")
def get_conversion():

    visitors = set()
    checkout_visitors = set()

    for event in events_db:

        if event["event_type"] == "ENTRY":

            visitors.add(
                event["visitor_id"]
            )

        if (
            event["event_type"] == "ZONE_ENTER"
            and event["zone_id"] == "CASH_COUNTER"
        ):

            checkout_visitors.add(
                event["visitor_id"]
            )

    total = len(visitors)

    checkout = len(
        checkout_visitors
    )

    rate = 0

    if total > 0:

        rate = (
            checkout / total
        ) * 100

    return {
        "total_visitors": total,
        "checkout_visitors": checkout,
        "conversion_rate": round(
            rate,
            2
        )
    }



@app.post("/events/ingest")
def ingest_event(event: Event):

    event_data = event.model_dump()

    events_db.append(event_data)

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events(
            event_id,
            visitor_id,
            event_type,
            zone_id,
            dwell_ms,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            event.event_id,
            event.visitor_id,
            event.event_type,
            event.zone_id,
            event.dwell_ms,
            event.timestamp
        )
    )

    conn.commit()

    cursor.execute(
        "SELECT COUNT(*) FROM events"
    )

    total_events = cursor.fetchone()[0]

    print("=" * 50)
    print("EVENT RECEIVED")
    print(event_data)
    print(f"TOTAL EVENTS: {total_events}")
    print("=" * 50)

    conn.close()

    return {
        "message": "Event Ingested",
        "total_events": total_events
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

@app.get("/purchases")
def get_purchases():

    print(type(purchase_events[0]))

    print(purchase_events[0])

    return {
        "count": len(purchase_events),
        "purchases": purchase_events[:5]
    }

@app.get("/brands")
def get_brands():

    return brand_sales

@app.get("/revenue")
def get_revenue():

    total_revenue = 0

    total_orders = len(
        purchase_events
    )

    for purchase in purchase_events:

        total_revenue += (
            purchase["gmv"]
        )

    avg_order_value = 0

    if total_orders > 0:

        avg_order_value = (
            total_revenue
            / total_orders
        )

    return {
        "total_revenue": round(
            total_revenue,
            2
        ),
        "total_orders": total_orders,
        "avg_order_value": round(
            avg_order_value,
            2
        )
    }


@app.get("/brand-conversion")
def get_brand_conversion():

    result = {}

    for brand in brand_sales:

        revenue = brand_sales.get(
            brand,
            0
        )

        purchases = brand_purchases.get(
            brand,
            0
        )

        avg_sale = 0

        if purchases > 0:

            avg_sale = (
                revenue
                / purchases
            )

        result[brand] = {
            "purchases": purchases,
            "revenue": round(
                revenue,
                2
            ),
            "avg_sale": round(
                avg_sale,
                2
            )
        }

    return result


@app.get("/top-brands")
def get_top_brands():

    sorted_brands = sorted(
        brand_sales.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = []

    for brand, revenue in sorted_brands:

        result.append(
            {
                "brand": brand,
                "revenue": revenue,
                "purchases":
                    brand_purchases.get(
                        brand,
                        0
                    )
            }
        )

    return result[:10]

@app.get("/zone-brand-revenue")
def zone_brand_revenue():

    mapping = {
        "GOOD_VIBES": "Good Vibes",
        "DERMDOC": "DERMDOC",
        "FACES_CANADA": "Faces Canada",
        "MAYBELLINE": "Maybelline"
    }

    result = {}

    for zone, brand in mapping.items():

        result[zone] = {
            "brand": brand,
            "revenue": round(
                brand_sales.get(
                    brand,
                    0
                ),
                2
            ),
            "purchases":
                brand_purchases.get(
                    brand,
                    0
                )
        }

    return result

@app.get("/zone-performance")
def zone_performance():

    mapping = {
        "GOOD_VIBES": "Good Vibes",
        "DERMDOC": "DERMDOC",
        "FACES_CANADA": "Faces Canada",
        "MAYBELLINE": "Maybelline"
    }

    zone_visitors = defaultdict(set)
    zone_dwell = defaultdict(list)

    for record in visitor_dwell:

        zone = record["zone"]

        zone_visitors[zone].add(
            record["visitor_id"]
        )

        zone_dwell[zone].append(
            record["seconds"]
        )

    result = {}

    for zone, brand in mapping.items():

        visitors = len(
            zone_visitors[zone]
        )

        avg_dwell = 0

        if len(zone_dwell[zone]) > 0:

            avg_dwell = (
                sum(zone_dwell[zone])
                /
                len(zone_dwell[zone])
            )

        result[zone] = {

            "visitors": visitors,

            "avg_dwell_seconds":
                round(
                    avg_dwell,
                    2
                ),

            "revenue":
                round(
                    brand_sales.get(
                        brand,
                        0
                    ),
                    2
                ),

            "purchases":
                brand_purchases.get(
                    brand,
                    0
                )
        }

    return result

@app.get("/dwell-v2")
def get_dwell_v2():

    dwell_events = []

    for event in events_db:

        if event["event_type"] == "DWELL":

            dwell_events.append(
                {
                    "visitor_id":
                        event["visitor_id"],

                    "zone":
                        event["zone_id"],

                    "seconds":
                        round(
                            event["dwell_ms"] / 1000,
                            2
                        )
                }
            )

    return {
        "count": len(dwell_events),
        "records": dwell_events
    }



@app.get("/zone-performance-v2")
def zone_performance_v2():

    mapping = {
        "GOOD_VIBES": "Good Vibes",
        "DERMDOC": "DERMDOC",
        "FACES_CANADA": "Faces Canada",
        "MAYBELLINE": "Maybelline"
    }

    zone_visitors = defaultdict(set)
    zone_dwell = defaultdict(list)

    for event in events_db:

        if event["event_type"] != "DWELL":
            continue

        zone = event["zone_id"]

        zone_visitors[zone].add(
            event["visitor_id"]
        )

        zone_dwell[zone].append(
            event["dwell_ms"] / 1000
        )

    result = {}

    for zone, brand in mapping.items():

        visitors = len(
            zone_visitors[zone]
        )

        avg_dwell = 0

        if len(zone_dwell[zone]) > 0:

            avg_dwell = (
                sum(zone_dwell[zone])
                /
                len(zone_dwell[zone])
            )

        result[zone] = {

            "visitors": visitors,

            "avg_dwell_seconds":
                round(
                    avg_dwell,
                    2
                ),

            "revenue":
                brand_sales.get(
                    brand,
                    0
                ),

            "purchases":
                brand_purchases.get(
                    brand,
                    0
                )
        }

    return result

@app.get("/events-db")
def get_events_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            event_id,
            visitor_id,
            event_type,
            zone_id,
            dwell_ms,
            timestamp
        FROM events
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return {
        "count": len(rows),
        "events": rows
    }

@app.get("/dashboard")
def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )

@app.get("/test-template")
def test_template(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )