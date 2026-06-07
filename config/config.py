import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Test logging
with open(ROOT / 'config' / 'settings.yaml', 'r') as f:
    _cfg = yaml.safe_load(f)

RAW_PATH = _cfg["storage_loc"]["raw"]
BRONZE_PATH = _cfg["storage_loc"]["bronze"]
SILVER_PATH = _cfg["storage_loc"]["silver"]
GOLD_PATH = _cfg["storage_loc"]["gold"]
FAILED_PATH = _cfg["storage_loc"]["failed"]

MAX_RETRIES = _cfg["max_retries"]
RETRY_DELAY = _cfg["retry_delay"]
