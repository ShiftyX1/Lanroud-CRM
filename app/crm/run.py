from fastapi import FastAPI

from app.config.config import settings

from database import database

def start_application():
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
    )
    database.connect_database(app=app)
    return app

crm = start_application()
