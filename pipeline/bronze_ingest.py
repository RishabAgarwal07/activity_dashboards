import yaml
from utils.logger import Logger

# Test logging
with open('config/settings.yaml', 'r') as f:
    config = yaml.safe_load(f)

date_str = "2024-06-01"  # Example date string for testing
logger = Logger(logger_name=config["bronze"]["logger_name"], log_level=config["bronze"]["log_level"], log_file=config["bronze"]["log_file"].format(date_str)).get_logger()

logger.info("This is an info message for testing the logger.")
logger.warning("This is a warning message for testing the logger.")
logger.error("This is an error message for testing the logger.")