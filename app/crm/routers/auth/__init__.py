from fastapi import APIRouter

from app.crm.routers.auth.views import views_router
from app.crm.routers.auth.api import api_router


auth_router = APIRouter()

auth_router.include_router(router=views_router, prefix='', tags=['Views'])
auth_router.include_router(router=api_router, prefix='/api')
