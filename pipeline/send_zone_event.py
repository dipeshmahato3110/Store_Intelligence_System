import requests
from datetime import datetime


def send_zone_event(track_id, zone):

    payload = {
        "event_id": f"zone_{track_id}_{zone}",
        "store_id": "STORE_BLR_001",
        "camera_id": "CAM_02",
        "visitor_id": f"VIS_{track_id}",
        "event_type": "ZONE_ENTER",
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": zone,
        "dwell_ms": 0,
        "is_staff": False,
        "confidence": 0.95,
        "metadata": {}
    }

    requests.post(
        "http://127.0.0.1:8000/events/ingest",
        json=payload
    )