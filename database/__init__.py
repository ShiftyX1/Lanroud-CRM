from dotenv import load_dotenv
from database.database_connection import Database
import os

from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

database = Database(host=os.getenv("DB_HOST"), 
                    port=os.getenv("DB_PORT"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASS"),
                    database=os.getenv("DB_NAME"),
                    engine='tortoise.backends.asyncpg'
                    )

TORTOISE_ORM = database.get_config()
