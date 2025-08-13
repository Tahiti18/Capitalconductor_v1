
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import deck, analytics

app = FastAPI(title="CapitalConductor API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True, "service": "CapitalConductor API"}

app.include_router(deck.router, prefix="/deck", tags=["deck"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
