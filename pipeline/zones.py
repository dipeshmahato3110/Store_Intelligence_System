# pipeline/zones.py

ZONES = {

    "MAYBELLINE": (
        0, 450,
        350, 900
    ),

    "GOOD_VIBES": (
        350, 450,
        650, 900
    ),

    "DERMDOC": (
        650, 450,
        950, 900
    ),

    "MINIMALIST": (
        950, 450,
        1250, 900
    ),

    "FACES_CANADA": (
        1250, 450,
        1550, 900
    ),

    "CASH_COUNTER": (
        1550, 450,
        1920, 900
    )
}


def get_zone(x, y):

    for zone, (x1, y1, x2, y2) in ZONES.items():

        if x1 <= x <= x2 and y1 <= y <= y2:
            return zone

    return None