
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "")
engine = create_engine(DATABASE_URL, pool_pre_ping=True) if DATABASE_URL else None
SessionLocal = sessionmaker(bind=engine) if engine else None

DDL = '''
CREATE TABLE IF NOT EXISTS events (
  id SERIAL PRIMARY KEY,
  type VARCHAR(64) NOT NULL,
  email VARCHAR(320),
  project_id VARCHAR(64),
  ts BIGINT,
  meta_json TEXT
);
'''

def ensure_schema():
    if engine is None: 
        return
    with engine.begin() as conn:
        conn.execute(text(DDL))
