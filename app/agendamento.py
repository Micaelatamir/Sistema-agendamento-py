from fastapi import FastAPI, Depends, HTTPException, status, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from app.database import engine, Base, get_db
from app import schemas, crud
from app.models import Usuario
from passlib.context import CryptContext
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco
Base.metadata.create_all(bind=engine)

# Hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Templates e static
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Página inicial
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    usuario_id = request.cookies.get("usuario_id")
    return templates.TemplateResponse("index.html", {"request": request, "usuario_id": usuario_id})

# Cadastro
@app.get("/cadastro", response_class=HTMLResponse)
def form_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/usuarios")
def criar_usuario(email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = schemas.UserCreate(email=email, senha=senha)
    db_usuario = crud.buscar_usuario_por_email(db, usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    crud.criar_usuario(db, usuario)
    return RedirectResponse(url="/login", status_code=303)

# Login
@app.get("/login", response_class=HTMLResponse)
def form_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(response: Response, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = crud.buscar_usuario_por_email(db, email)
    if not usuario or not pwd_context.verify(senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Salva o ID do usuário como cookie
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(key="usuario_id", value=str(usuario.id))
    return response

# Logout
@app.get("/logout")
def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("usuario_id")
    return response

# Routers
from usuario import router as usuario_router
from agendamento import router as agendamento_router

app.include_router(usuario_router)
app.include_router(agendamento_router)
