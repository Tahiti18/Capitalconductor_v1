
from fastapi import APIRouter, HTTPException, Query
from ..security import sign_invite, verify_invite

router = APIRouter()

@router.get("/sign")
def sign(email: str, project_id: str):
    return {"token": sign_invite(email, project_id)}

@router.get("/verify")
def verify(token: str = Query(...)):
    data = verify_invite(token)
    if not data:
        raise HTTPException(400, "Invalid token")
    return {"ok": True, "data": data}
