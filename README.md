# Inventory Alert System

This project sends email alerts when inventory levels fall below the minimum threshold. It reads inventory data from a CSV file, detects low stock items, and sends a **single email** containing all problematic products. It also logs all alerts to a CSV file for tracking.

## Features

- Reads inventory data from a CSV file.
- Automatically detects products with stock levels below the minimum threshold.
- Sends a **single daily/weekly email** summarizing all low-stock items.
- Logs all alerts to a separate CSV file (`alerts_log.csv`).
- Runs automatically on a scheduled basis (daily or weekly) using Task Scheduler (Windows) or CRON (Linux/macOS).
- Uses relative paths for portability.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/GOLDMONDO/inventory-alert-system.git
    cd inventory-alert-system
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On Linux/macOS:
      ```bash
      source venv/bin/activate
      ```

4.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure your email credentials:**

    - Create a `.env` file in the root directory of the project.
    - Add your email address and app password (for Gmail, you need an App Password, not your regular password):
      ```
      EMAIL_USER=your_email@gmail.com
      EMAIL_PASS=your_app_password
      ```
    - **Important:** Never commit the `.env` file to version control. It's already included in `.gitignore`.

6.  **Generate sample inventory data (optional):**

    ```bash
    python src/generate_data.py
    ```
    This will create a `data/inventory.csv` file with sample inventory information.

7.  **Run the alert system manually:**

    ```bash
    python run.py
    ```
    This command will execute the inventory check, detect low stock, send an email (if configured correctly), and log the alerts.

## Automation (Scheduling)

### On Windows (Task Scheduler)

1.  Create a batch file (`run_inventory_alert.bat`) to run the script:
    ```batch
    @echo off
    cd /d "%~dp0"
    call ".venv\Scripts\activate.bat"
    python run.py
    pause
    ```
2.  Use the Windows Task Scheduler to run this `.bat` file at your desired frequency (e.g., daily at 9 AM).

### On Linux/macOS (CRON)

1.  Create a shell script (`run_inventory_alert.sh`) to run the script:
    ```bash
    #!/bin/bash
    cd /path/to/your/inventory-alert-system
    source venv/bin/activate
    python run.py
    ```
2.  Make the script executable:
    ```bash
    chmod +x run_inventory_alert.sh
    ```
3.  Edit your crontab (`crontab -e`) and add a line to schedule the script. For example, to run daily at 9 AM:
    ```bash
    0 9 * * * /full/path/to/run_inventory_alert.sh
    ```

## Project Structure

inventory_alert_system/
│
├── data/ # Directory for inventory and log files
│ ├── inventory.csv # Input file containing inventory data
│ └── alerts_log.csv # Output file logging sent alerts
├── src/ # Source code files
│ ├── generate_data.py # Script to create sample inventory data
│ ├── inventory_checker.py # Main logic for checking inventory levels
│ ├── email_sender.py # Module for sending emails via SMTP
│ └── logger.py # Module for logging alerts to CSV
├── config/ # (Optional) Configuration files (currently empty or not used)
├── .env # (Not tracked) Contains sensitive email credentials
├── .gitignore # Specifies files and directories to ignore in Git
├── README.md # This file
├── requirements.txt # List of Python dependencies
├── run.py # Main entry point to run the entire system
├── run_inventory_alert.bat # (Windows) Script for scheduled execution
└── run_inventory_alert.sh # (Linux/macOS) Script for scheduled execution


## Dependencies

- `pandas`: For reading and writing CSV files.
- `python-dotenv`: For loading environment variables from the `.env` file.

## License

MIT
