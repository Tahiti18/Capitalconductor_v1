
from fastapi import APIRouter, Body
from sqlalchemy import text
from ..db import engine

router = APIRouter()

@router.post("/track")
def track(event: dict = Body(...)):
    # event fields
    etype = str(event.get("type","event"))[:64]
    email = (event.get("email") or None)
    project_id = (event.get("project_id") or None)
    ts = int(event.get("ts") or 0)
    meta = event
    if engine:
        with engine.begin() as conn:
            conn.execute(text("INSERT INTO events(type,email,project_id,ts,meta_json) VALUES (:t,:e,:p,:ts,:m)"),
                         {"t": etype, "e": email, "p": project_id, "ts": ts, "m": str(meta)})
    return {"ok": True}
