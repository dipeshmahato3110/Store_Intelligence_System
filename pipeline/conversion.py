# pipeline/conversion.py

total_visitors = set()

checkout_visitors = set()


def add_visitor(track_id):
    total_visitors.add(track_id)


def add_checkout(track_id):
    checkout_visitors.add(track_id)


def get_conversion_rate():

    if len(total_visitors) == 0:
        return 0

    return (
        len(checkout_visitors)
        / len(total_visitors)
    ) * 100


def print_metrics():

    print("\n===== CONVERSION METRICS =====")

    print(
        f"Total Visitors: {len(total_visitors)}"
    )

    print(
        f"Checkout Visitors: {len(checkout_visitors)}"
    )

    print(
        f"Conversion Rate: "
        f"{get_conversion_rate():.2f}%"
    )

    print("==============================\n")