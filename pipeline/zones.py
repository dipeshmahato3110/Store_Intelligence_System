# pipeline/zones.py

ZONES = {
    "GOOD_VIBES": (100, 100, 250, 250),
    "DERMDOC": (260, 100, 420, 250),
    "MINIMALIST": (430, 100, 600, 250),
    "MAYBELLINE": (100, 500, 250, 650),
    "FACES_CANADA": (260, 500, 450, 650),
    "CASH_COUNTER": (800, 250, 950, 500),
}

def get_zone(x, y):
    for zone, (x1, y1, x2, y2) in ZONES.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            return zone

    return None