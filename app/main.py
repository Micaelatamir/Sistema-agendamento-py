from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from app.database import engine, Base
from app.usuario import router as usuario_router
from app.agendamento import router as agendamento_router

# Criar as tabelas no banco 
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Registrar rotas
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(agendamento_router, prefix="/agendamentos", tags=["Agendamentos"])

# Página inicial
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
