from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


views_router = APIRouter()

templates = Jinja2Templates(directory='app/crm/templates/')


@views_router.get('/')
def auth_page(request: Request):
    return templates.TemplateResponse(request=request, name='default/auth/auth.jinja2')
