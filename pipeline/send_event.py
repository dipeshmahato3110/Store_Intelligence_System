import requests
import uuid
from datetime import datetime

def send_entry_event(visitor_id):

    event = {
        "event_id": str(uuid.uuid4()),
        "store_id": "STORE_BLR_001",
        "camera_id": "CAM_ENTRY_01",
        "visitor_id": f"VIS_{visitor_id}",
        "event_type": "ENTRY",
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": None,
        "dwell_ms": 0,
        "is_staff": False,
        "confidence": 0.95,
        "metadata": {}
    }

    response = requests.post(
        "http://127.0.0.1:8000/events/ingest",
        json=event
    )

    print(response.json())