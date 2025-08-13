
from dataclasses import dataclass

@dataclass
class EventIn:
    type: str
    email: str|None = None
    project_id: str|None = None
    ts: int|None = None
    meta: dict|None = None
