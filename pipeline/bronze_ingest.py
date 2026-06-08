from pipeline.utils.logger import get_logger
from config.config import RAW_PATH, BRONZE_PATH, BATCH_SIZE, MAX_MAP_POINTS

logger = get_logger(__name__)


logger.info("This is an info message for testing the logger.")
logger.warning("This is a warning message for testing the logger.")
logger.error("This is an error message for testing the logger.")

logger.info(f"RAW_PATH: {RAW_PATH}")
logger.info(f"BRONZE_PATH: {BRONZE_PATH}")
logger.info(f"BATCH_SIZE: {BATCH_SIZE}")
logger.info(f"MAX_MAP_POINTS: {MAX_MAP_POINTS}")