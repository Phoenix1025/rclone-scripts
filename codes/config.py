import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DEFAULT_PORT = int(os.getenv("DEFAULT_PORT", 8080))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Constants
ROOT_DIR = Path(__file__).parent.parent
CONFIG_DIR = ROOT_DIR / "data"
CONFIG_DIR.mkdir(exist_ok=True)
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
CONFIG_FILE = CONFIG_DIR / "config.json"
LOG_FILE = LOG_DIR / "rclone_scripts.log"
BACKENDS = ["FTP", "WebDAV"]
DEFAULT_CONFIG = {
    "flags": {
        "drive": {},
        "mega": {},
        "google photos": {}
    }
}


def configure_logging() -> None:
    """Configures logging with file rotation and console output."""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3),
            logging.StreamHandler(sys.stdout)
        ]
    )
