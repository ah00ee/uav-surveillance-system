from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/map")
async def client(request: Request):
    return templates.TemplateResponse("base.html", {"request":request})

@app.get("/")
async def map(request: Request):
    return templates.TemplateResponse("map.html", {"request":request})