import asyncio
from database.postgres import init_db

asyncio.run(init_db())