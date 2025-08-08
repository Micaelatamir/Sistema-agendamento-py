from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="977310607",
        database="sistema_agendamento"
    )

templates = Jinja2Templates(directory="templates")
router = APIRouter()

# FORMULÁRIO PARA CRIAR USUÁRIO
@router.get("/criar_usuario", response_class=HTMLResponse)
def form_criar_usuario(request: Request):
    return templates.TemplateResponse("criar_usuario.html", {"request": request})

# CRIAR USUÁRIO
@router.post("/criar_usuario")
def criar_usuario(nome: str = Form(...), email: str = Form(...)):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conexao.commit()
    cursor.close()
    conexao.close()
    return RedirectResponse(url="/listar_usuarios", status_code=303)

# LISTAR USUÁRIOS
@router.get("/listar_usuarios", response_class=HTMLResponse)
def listar_usuarios(request: Request):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return templates.TemplateResponse("listar_usuarios.html", {"request": request, "usuarios": usuarios})

# FORMULÁRIO DE BUSCAR
@router.get("/buscar_usuario", response_class=HTMLResponse)
def form_buscar_usuario(request: Request):
    return templates.TemplateResponse("buscar_usuario.html", {"request": request})

# BUSCAR USUÁRIO
@router.post("/buscar_usuario", response_class=HTMLResponse)
def buscar_usuario(request: Request, nome: str = Form(...)):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE nome = %s", (nome,))
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()

    if usuario:
        return templates.TemplateResponse("buscar_usuario.html", {"request": request, "usuario_encontrado": usuario})
    else:
        return templates.TemplateResponse("buscar_usuario.html", {"request": request, "mensagem": "Usuário não encontrado"})

# FORMULÁRIO DE DELETAR
@router.get("/deletar_usuario", response_class=HTMLResponse)
def form_deletar_usuario(request: Request):
    return templates.TemplateResponse("deletar_usuario.html", {"request": request})

# DELETAR USUÁRIO
@router.post("/deletar_usuario")
def deletar_usuario(nome: str = Form(...)):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nome = %s", (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return RedirectResponse(url="/listar_usuarios", status_code=303)
