# pipeline/load_pos.py

import pandas as pd

from pipeline.purchase_analytics import (
    purchase_events,
    brand_sales
)

CSV_FILE = (
    "data/pos/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)


def load_pos_data():

    df = pd.read_csv(CSV_FILE)

    for _, row in df.iterrows():

        purchase = {
            "order_id": str(row["order_id"]),
            "date": str(row["order_date"]),
            "time": str(row["order_time"]),
            "product": str(row["product_name"]),
            "brand": str(row["brand_name"]),
            "qty": int(row["qty"]),
            "gmv": float(row["GMV"]),
            "salesperson": str(row["salesperson_name"])
        }

        purchase_events.append(purchase)

        brand = row["brand_name"]

        if brand not in brand_sales:
            brand_sales[brand] = 0

        brand_sales[brand] += float(row["GMV"])

    print(
        f"Loaded {len(purchase_events)} purchases"
    )
