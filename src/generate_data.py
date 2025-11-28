import pandas as pd
import random
from pathlib import Path

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
    file_path = Path("data") / "inventory.csv"
    df.to_csv(file_path, index=False)
    print("File 'inventory.csv' generated successfully.")

if __name__ == "__main__":
    generate_sample_data()
