"""Library for logging."""
import sys
import logging
import json_log_formatter

class Logger:
    """Class for logging"""
    def __init__(self):
        pass
    def get_logger(self,log_path):
        """Function for logging"""
        self.log_path = log_path
        logger = logging.getLogger(__name__)
        try:
            logger.setLevel(logging.INFO)
            if not logger.hasHandlers():
                formatter = json_log_formatter.VerboseJSONFormatter()
                file_handler = logging.FileHandler(self.log_path)
                stream_handler = logging.StreamHandler(sys.stdout)
                file_handler.setFormatter(formatter)
                stream_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                logger.addHandler(stream_handler)
            return logger
        except FileNotFoundError:
            logger.error("Unable to find log file %s", self.log_path)
            sys.exit()

            return None
            