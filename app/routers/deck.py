
from fastapi import APIRouter, HTTPException, Body
from ..config import settings

router = APIRouter()

@router.post("/unlock")
def unlock(payload: dict = Body(...)):
    if payload.get("password") != settings.LIVE_DECK_PASSWORD:
        raise HTTPException(401, "Invalid password")
    return {"ok": True}
