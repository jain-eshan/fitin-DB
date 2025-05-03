import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

NEON_DATABASE_URL = os.getenv("NEON_DATABASE_URL")

async def get_db_connection():
    conn = await asyncpg.connect(NEON_DATABASE_URL)
    return conn
