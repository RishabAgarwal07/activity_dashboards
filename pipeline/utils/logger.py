"""
Logger for the pipeline.
This module sets up the logging configuration for the pipeline,
allowing for consistent and structured logging throughout the codebase.
"""

import logging
from pathlib import Path
from datetime import date
from config.config import LOG_LEVEL, LOG_FILE

def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)

    log_file = LOG_FILE.format(date=date.today().strftime("%Y-%m-%d"))
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(LOG_LEVEL)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)

    # --- Formatter ---
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
