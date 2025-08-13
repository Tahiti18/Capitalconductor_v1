
import os

class Settings:
    LIVE_DECK_PASSWORD = os.getenv("LIVE_DECK_PASSWORD", "Conductor2025")
    GHL_INCOMING_WEBHOOK_URL = os.getenv("GHL_INCOMING_WEBHOOK_URL", "")
    SHEET_ID = os.getenv("SHEET_ID", "")
    GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    CORS_ORIGINS = [o for o in os.getenv("CORS_ORIGINS", "*").split(",") if o]

settings = Settings()
