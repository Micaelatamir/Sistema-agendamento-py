from fastapi import FastAPI
from database import SessionLocal, engine, Base
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.usuario import usuarios, Usuario
from app.agendamento import agendamentos, Agendamento


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Conexão com PostgreSQL funcionando!"}

# Criar o app FastAPI
app = FastAPI()

# Montar arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Página inicial
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Formulário de criar usuário
@app.get("/criar_usuario", response_class=HTMLResponse)
def exibir_formulario_usuario(request: Request):
    return templates.TemplateResponse("criar_usuario.html", {"request": request})

# Salvando usuário
@app.post("/criar_usuario")
def salvar_usuario(nome: str = Form(...), email: str = Form(...)):
    novo_usuario = Usuario(nome=nome, email=email)
    usuarios.append(novo_usuario)
    return RedirectResponse(url="/listar_usuarios", status_code=303)

# Listando usuários
@app.get("/listar_usuarios", response_class=HTMLResponse)
def listar_usuarios(request: Request):
    return templates.TemplateResponse("listar_usuarios.html", {"request": request, "usuarios": usuarios})

# Formulário de criar agendamento
@app.get("/criar_agendamento", response_class=HTMLResponse)
def exibir_formulario_agendamento(request: Request):
    return templates.TemplateResponse("criar_agendamento.html", {"request": request})

# Salvando agendamento
@app.post("/criar_agendamento")
def salvar_agendamento(usuario: str = Form(...), servico: str = Form(...)):
    novo_agendamento = Agendamento(usuario=usuario, servico=servico)
    agendamentos.append(novo_agendamento)
    return RedirectResponse(url="/listar_agendamentos", status_code=303)

# Listando agendamentos
@app.get("/listar_agendamentos", response_class=HTMLResponse)
def listar_agendamentos(request: Request):
    return templates.TemplateResponse("listar_agendamentos.html", {"request": request, "agendamentos": agendamentos})
