
from fastapi import APIRouter, Body
import os, json, time

router = APIRouter()

def _try_post_ghl(url, payload):
    import httpx
    try:
        with httpx.Client(timeout=10) as c:
            r = c.post(url, json=payload)
            r.raise_for_status()
        return None
    except Exception as e:
        return str(e)

def _try_append_sheet(sheet_id, sa_path, row):
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(sa_path, scopes=scopes)
        gc = gspread.authorize(creds)
        sh = gc.open_by_key(sheet_id)
        ws = sh.sheet1
        ws.append_row(row, value_input_option="RAW")
        return None
    except Exception as e:
        return str(e)

@router.post("/track")
def track(event: dict = Body(...)):
    ok = True
    errors = []
    ts = int(event.get("ts") or time.time() * 1000)
    email = event.get("email", "")
    eid = event.get("id", "")
    etype = event.get("type", "event")

    # Google Sheets (optional, fail‑soft)
    sheet_id = os.getenv("SHEET_ID", "")
    sa_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if sheet_id and sa_path and os.path.exists(sa_path):
        err = _try_append_sheet(sheet_id, sa_path, [etype, eid, email, ts, json.dumps(event)])
        if err: errors.append(f"sheets:{err}")

    # GoHighLevel Incoming Webhook (optional, fail‑soft)
    ghl = os.getenv("GHL_INCOMING_WEBHOOK_URL", "")
    if ghl:
        err = _try_post_ghl(ghl, event)
        if err: errors.append(f"ghl:{err}")

    return {"ok": ok, "errors": errors}
