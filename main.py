from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from views.hello import router as hello_router
from views.items import router as items_router
from views.users.views import router as users_router

app = FastAPI()
app.include_router(hello_router)
app.include_router(items_router)
app.include_router(users_router)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
