import pandas as pd
from src.email_sender import send_email
from src.logger import log_alert
from pathlib import Path

def check_inventory_and_alert():
    df = pd.read_csv(Path("data") / "inventory.csv")
    low_stock = df[df['current_stock'] < df['min_stock']]

    if low_stock.empty:
        print("There are no products with low inventory.")
    else:
        print(f"They were detected {len(low_stock)} products with low stock.")

        # Create email body with all products
        body_lines = ["Products with low inventory:\n"]
        for _, row in low_stock.iterrows():
            line = f"- {row['product_name']} (ID: {row['product_id']}) - Stock actual: {row['current_stock']}, Mínimo: {row['min_stock']}"
            body_lines.append(line)
            # Record each alert
            log_alert(row['product_id'], row['product_name'], row['current_stock'])

        body = "\n".join(body_lines)
        subject = f"ALERT: {len(low_stock)} products with low stock"

        # Send a single email with all the products
        send_email(subject, body, "inventory@company.com")
        print("Alert email sent with all low stock products.")