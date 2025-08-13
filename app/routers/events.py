
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from sqlalchemy import text
from ..db import engine

router = APIRouter()

@router.get("/export.csv", response_class=PlainTextResponse)
def export_csv():
    if not engine:
        return "type,email,project_id,ts,meta_json"
    rows = []
    with engine.begin() as conn:
        res = conn.execute(text("SELECT type,email,project_id,ts,meta_json FROM events ORDER BY id DESC LIMIT 2000"))
        rows.append("type,email,project_id,ts,meta_json")
        for t,e,p,ts,m in res:
            # rudimentary CSV escaping
            def esc(x): 
                s = "" if x is None else str(x)
                s = s.replace('"','""')
                return f'"{s}"'
            rows.append(",".join([esc(t),esc(e),esc(p),esc(ts),esc(m)]))
    return "
".join(rows)
