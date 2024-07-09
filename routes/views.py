from fastapi.templating import Jinja2Templates
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    print("request", request)
    return templates.TemplateResponse("index.html", {"request": request, "content": "hello world"})