"""Vercel entrypoint for the FastAPI application."""

import sys
from pathlib import Path

# Add project root directory to sys.path so main.py and local files can be resolved
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from main import app

__all__ = ["app"]

