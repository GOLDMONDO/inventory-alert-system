import pandas as pd
from datetime import datetime
import os
from pathlib import Path

def log_alert(product_id, product_name, stock):
    log_entry = {
        "timestamp": datetime.now(),
        "product_id": product_id,
        "product_name": product_name,
        "current_stock": stock
    }
    log_df = pd.DataFrame([log_entry])

    # log file path
    log_file = Path("data") / "alerts_log.csv"

    # Check if the file already exists
    if not os.path.exists(log_file):
        # Si no existe, crearlo con encabezados
        log_df.to_csv(log_file, mode='w', header=True, index=False)
        print(f"File '{log_file}' Created and first alert registered.")
    else:
        # If it already exists, add the new alert without headers
        log_df.to_csv(log_file, mode='a', header=False, index=False)
        print(f"Alert registered in '{log_file}'.")