
from fastapi import APIRouter, Body, HTTPException
from ..config import settings

router = APIRouter()

@router.post("/unlock")
def unlock(payload: dict = Body(...)):
    pwd = (payload.get("password") or "").strip()
    expected = (settings.LIVE_DECK_PASSWORD or "").strip()
    if pwd.lower() != expected.lower():
        raise HTTPException(401, "Invalid password")
    return {"ok": True}
