import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Test logging
with open(ROOT / 'config' / 'settings.yaml', 'r') as f:
    _cfg = yaml.safe_load(f)

RAW_PATH = ROOT / _cfg["storage_loc"]["raw"]
BRONZE_PATH = ROOT / _cfg["storage_loc"]["bronze"]
SILVER_PATH = ROOT / _cfg["storage_loc"]["silver"]
GOLD_PATH = ROOT / _cfg["storage_loc"]["gold"]
FAILED_PATH = ROOT / _cfg["storage_loc"]["failed"]

MAX_RETRIES = ROOT / _cfg["max_retries"]
RETRY_DELAY = ROOT / _cfg["retry_delay"]
BATCH_SIZE = ROOT / _cfg["batch_size"]
MAX_MAP_POINTS = ROOT / _cfg["max_map_points"]

LOG_LEVEL = ROOT / _cfg["logging"]["log_level"]
LOG_FILE = ROOT / _cfg["logging"]["log_file"]
