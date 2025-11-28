import pandas as pd
from src.email_sender import send_email
from src.logger import log_alert


def check_inventory_and_alert():
    df = pd.read_csv(
        "C:/Users/Nico Aldazaba/PycharmProjects/RemoteJobGo/Github Project/inventory_alert_system/data/inventory.csv")
    low_stock = df[df['current_stock'] < df['min_stock']]

    if low_stock.empty:
        print("No hay productos con bajo inventario.")
    else:
        print(f"Se detectaron {len(low_stock)} productos con bajo stock.")

        # Crear cuerpo del correo con todos los productos
        body_lines = ["Productos con bajo inventario:\n"]
        for _, row in low_stock.iterrows():
            line = f"- {row['product_name']} (ID: {row['product_id']}) - Stock actual: {row['current_stock']}, Mínimo: {row['min_stock']}"
            body_lines.append(line)
            # Registrar cada alerta
            log_alert(row['product_id'], row['product_name'], row['current_stock'])

        body = "\n".join(body_lines)
        subject = f"ALERTA: {len(low_stock)} productos con bajo inventario"

        # Enviar un solo correo con todos los productos
        send_email(subject, body, "nikodemus2025@gmail.com")
        print("Correo de alerta enviado con todos los productos con bajo stock.")