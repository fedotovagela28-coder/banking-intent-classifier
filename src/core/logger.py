import logging
from pathlib import Path

from src.core.config import config

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"

def setup_logger(name: str) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(config.log_level)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger