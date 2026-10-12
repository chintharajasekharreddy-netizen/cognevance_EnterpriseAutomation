"""Central configuration."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "data", "input")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
ARCHIVE_DIR = os.path.join(BASE_DIR, "data", "archive")
LOG_DIR = os.path.join(BASE_DIR, "logs")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
DB_PATH = os.environ.get("ENTERPRISE_DB", os.path.join(BASE_DIR, "data", "enterprise.db"))

# External API (public test API; falls back to offline sample data if unreachable)
API_URL = "https://jsonplaceholder.typicode.com/posts?_limit=10"
API_TIMEOUT = 10
API_RETRIES = 3

# Multithreading
MAX_WORKERS = 4

# Scheduling (seconds)
FILE_JOB_INTERVAL = 60
API_JOB_INTERVAL = 300
REPORT_JOB_INTERVAL = 600

# Email notifications (disabled by default; set env var EMAIL_PASSWORD to enable)
EMAIL = {
    "enabled": False,
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 587,
    "sender": "your_email@gmail.com",
    "password": os.environ.get("EMAIL_PASSWORD", ""),
    "receiver": "receiver@example.com",
}

DASHBOARD_PORT = 8050
