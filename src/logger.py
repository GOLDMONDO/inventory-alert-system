import pandas as pd
from datetime import datetime
import os

def log_alert(product_id, product_name, stock):
    log_entry = {
        "timestamp": datetime.now(),
        "product_id": product_id,
        "product_name": product_name,
        "current_stock": stock
    }
    log_df = pd.DataFrame([log_entry])

    # Ruta del archivo log
    log_file = "C:/Users/Nico Aldazaba/PycharmProjects/RemoteJobGo/Github Project/inventory_alert_system/data/alerts_log.csv"

    # Verificar si el archivo ya existe
    if not os.path.exists(log_file):
        # Si no existe, crearlo con encabezados
        log_df.to_csv(log_file, mode='w', header=True, index=False)
        print(f"Archivo '{log_file}' creado y primera alerta registrada.")
    else:
        # Si ya existe, añadir la nueva alerta sin encabezados
        log_df.to_csv(log_file, mode='a', header=False, index=False)
        print(f"Alerta registrada en '{log_file}'.")