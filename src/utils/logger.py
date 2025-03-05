import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Define log file path
now = datetime.now()
now_str = now.strftime("%Y%m%d%H%M%S")
log_file = os.path.join(log_dir, f"{now_str}.log")

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Capture all log levels

# Formatter for logs
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler (writes to file)
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Stream handler (prints to terminal)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Add both handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
