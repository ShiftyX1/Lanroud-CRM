from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config.config import settings

#------IMPORT ROUTERS HERE--------
from app.crm.routers.auth.views import auth_router
#---------------------------------

from database import database

def start_application(routers: list):
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
    )
    database.connect_database(app=app)
    
    if routers == []:
        print("No routers included!")
    
    for router_elem in routers:
        app.include_router(router=router_elem["router"], prefix=router_elem["prefix"])

    app.mount("/css", StaticFiles(directory="app/crm/static/css"), name="css")
    app.mount("/script", StaticFiles(directory="app/crm/static/script"), name="script")
    app.mount("/img", StaticFiles(directory="app/crm/static/img"), name="img")
    return app

routers = [
    {"router": auth_router, "prefix": ""},
]

crm = start_application(routers=routers)
