
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from .config import settings
from .db import ensure_schema
from .routers import deck, analytics, events, invites

if settings.SENTRY_DSN:
    sentry_sdk.init(dsn=settings.SENTRY_DSN, integrations=[FastApiIntegration()])

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="CapitalConductor API", version="1.1.0")
app.state.limiter = limiter
app.add_exception_handler(limiter.rate_limit_exceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def _startup():
    ensure_schema()

@app.get("/health")
def health():
    return {"ok": True, "service": "CapitalConductor API"}

app.include_router(deck.router, prefix="/deck", tags=["deck"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(invites.router, prefix="/invites", tags=["invites"])
