import os

API_KEY = os.getenv("API_KEY", "change-me-please")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
