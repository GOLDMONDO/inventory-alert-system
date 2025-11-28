import pandas as pd
import random

def generate_sample_data():
    products = [f"Producto_{i}" for i in range(1, 101)]
    data = {
        "product_id": [f"P{i:03d}" for i in range(1, 101)],
        "product_name": products,
        "current_stock": [random.randint(0, 50) for _ in range(100)],
        "min_stock": [random.randint(5, 15) for _ in range(100)],
        "last_updated": pd.date_range(start="2024-01-01", periods=100, freq='D')
    }
    df = pd.DataFrame(data)
    df.to_csv("C:/Users/Nico Aldazaba/PycharmProjects/RemoteJobGo/Github Project/inventory_alert_system/data/inventory.csv", index=False)
    print("Archivo 'inventory.csv' generado exitosamente.")

if __name__ == "__main__":
    generate_sample_data()
