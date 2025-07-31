from fastapi import FastAPI, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from database import engine, Base, get_db
import schemas, crud
from models import Usuario
from passlib.context import CryptContext
import os


# Criar app FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conectar banco
Base.metadata.create_all(bind=engine)

# Hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configurar templates e static
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Rota: Página inicial
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota: Formulário de cadastro
@app.get("/cadastro", response_class=HTMLResponse)
def form_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# Rota: Formulário de login
@app.get("/login", response_class=HTMLResponse)
def form_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Rota POST: Criar usuário
@app.post("/usuarios")
def criar_usuario(email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = schemas.UserCreate(email=email, senha=senha)
    db_usuario = crud.buscar_usuario_por_email(db, usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    crud.criar_usuario(db, usuario)
    return RedirectResponse(url="/login", status_code=303)

# Rota POST: Login
@app.post("/login")
def login(email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = crud.buscar_usuario_por_email(db, email)
    if not usuario or not pwd_context.verify(senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return RedirectResponse(url="/", status_code=303)


@app.post("/usuarios/{usuario_id}/agendamentos")
def criar_agendamento(
    usuario_id: int,
    titulo: str = Form(...),
    data_hora: str = Form(...),  
    db: Session = Depends(get_db)
):
    agendamento = schemas.AgendamentoCreate(titulo=titulo, data_hora=data_hora)
    return crud.criar_agendamento(db, agendamento, usuario_id)

# Rota GET: Listar agendamentos
@app.get("/usuarios/{usuario_id}/agendamentos")
def listar_agendamentos(usuario_id: int, db: Session = Depends(get_db)):
    return crud.listar_agendamentos(db, usuario_id)

from usuario import router as usuario_router
from agendamento import router as agendamento_router

app.include_router(usuario_router)
app.include_router(agendamento_router)
