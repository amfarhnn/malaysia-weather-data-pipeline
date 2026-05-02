from sqlalchemy import create_engine, text
from src.config import Config

print('POSTGRES_URL=', Config.POSTGRES_URL)

try:
    engine = create_engine(Config.POSTGRES_URL)
    with engine.connect() as conn:
        r = conn.execute(text('SELECT 1'))
        print('Connection OK, result=', r.scalar())
except Exception as e:
    print('Connection FAILED:', e)
