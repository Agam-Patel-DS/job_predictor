import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        """Initialize the logger and create a separate log file for each run."""
        os.makedirs(log_dir, exist_ok=True)
        log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
        log_filepath = os.path.join(log_dir, log_filename)

        # Create logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # File handler
        file_handler = logging.FileHandler(log_filepath)
        file_handler.setLevel(logging.DEBUG)

        # Console handler (optional)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """Return the logger instance."""
        return self.logger
