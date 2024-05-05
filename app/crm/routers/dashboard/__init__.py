from fastapi import APIRouter

from app.crm.routers.dashboard.views import views_router
from app.crm.routers.dashboard.api import api_router


dashboard_router = APIRouter()

dashboard_router.include_router(router=views_router, prefix='', tags=['Views'])
dashboard_router.include_router(router=api_router, prefix='/api')
