"""
Logger for the pipeline.
This module sets up the logging configuration for the pipeline,
allowing for consistent and structured logging throughout the codebase.
"""

import logging

class Logger:
    """
    A Logger class that encapsulates the logging configuration for the pipeline.
    """
    def __init__(self, logger_name:str, log_level, log_file:str):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        # Create a file handler for logging to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Create a formatter and set it for the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """Returns the configured logger instance."""
        return self.logger
