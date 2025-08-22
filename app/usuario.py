from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserCreate  
from app.crud import criar_usuario
from app import models

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# FORMULÁRIO PARA CRIAR USUÁRIO
@router.get("/criar_usuario", response_class=HTMLResponse)
def exibir_formulario_usuario(request: Request):
    return templates.TemplateResponse("criar_usuario.html", {"request": request})


# CRIAR USUÁRIO
@router.post("/criar_usuario")
def criar_usuario_post(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = UserCreate(email=email, senha=senha)
    criar_usuario(db, usuario)
    return RedirectResponse(url="/", status_code=303)  # Volta pro menu inicial


# LISTAR USUÁRIOS
@router.get("/listar_usuarios", response_class=HTMLResponse)
def listar_usuarios(request: Request, db: Session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return templates.TemplateResponse("listar_usuarios.html", {"request": request, "usuarios": usuarios})


# FORMULÁRIO DE BUSCAR USUÁRIO
@router.get("/buscar_usuario", response_class=HTMLResponse)
def form_buscar_usuario(request: Request):
    return templates.TemplateResponse("buscar_usuario.html", {"request": request})


# BUSCAR USUÁRIO
@router.post("/buscar_usuario", response_class=HTMLResponse)
def buscar_usuario(request: Request, nome: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.nome == nome).first()
    if usuario:
        return templates.TemplateResponse("buscar_usuario.html", {"request": request, "usuario_encontrado": usuario})
    else:
        return templates.TemplateResponse("buscar_usuario.html", {"request": request, "mensagem": "Usuário não encontrado"})


# FORMULÁRIO DE DELETAR USUÁRIO
@router.get("/deletar_usuario", response_class=HTMLResponse)
def form_deletar_usuario(request: Request):
    return templates.TemplateResponse("deletar_usuario.html", {"request": request})


# DELETAR USUÁRIO
@router.post("/deletar_usuario")
def deletar_usuario(nome: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.nome == nome).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return RedirectResponse(url="/listar_usuarios", status_code=303)
