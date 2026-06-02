from app.database import get_connection


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        event_id TEXT,
        visitor_id TEXT,
        event_type TEXT,
        zone_id TEXT,
        dwell_ms INTEGER,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()