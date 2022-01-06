from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def client(request: Request):
    # /templates/base.html 파일 response
    return templates.TemplateResponse("base.html", {"request":request})