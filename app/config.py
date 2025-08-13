
import os

class Settings:
    LIVE_DECK_PASSWORD = os.getenv("LIVE_DECK_PASSWORD", "conductor2025")
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    ALLOWED_ORIGINS = [o for o in os.getenv("ALLOWED_ORIGINS", "*").split(",") if o]
    SENTRY_DSN = os.getenv("SENTRY_DSN", "")
    JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
    GHL_INCOMING_WEBHOOK_URL = os.getenv("GHL_INCOMING_WEBHOOK_URL", "")

settings = Settings()
