"""
Movie Recommender Application Entrypoint.

Native FastAPI web application serving both the REST API and the interactive UI.
"""

import importlib
import os
import sys
from pathlib import Path

# Ensure root directory is on sys.path for IDEs and serverless environments
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from main import app

__all__ = ["app"]

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"🎬 Starting Movie Recommender web app at http://localhost:{port}")
    uvicorn = importlib.import_module("uvicorn")
    uvicorn.run(app, host="0.0.0.0", port=port)
