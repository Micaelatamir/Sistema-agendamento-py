from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

usuarios = []

@router.get("/criar_usuario", response_class=HTMLResponse)
def form_criar_usuario(request: Request):
    return templates.TemplateResponse("criar_usuario.html", {"request": request})

@router.post("/criar_usuario")
def criar_usuario(nome: str = Form(...), email: str = Form(...)):
    novo_usuario = {
        "nome": nome,
        "email": email
    }
    usuarios.append(novo_usuario)
    return RedirectResponse(url="/listar_usuarios", status_code=303)

@router.get("/listar_usuarios", response_class=HTMLResponse)
def listar_usuarios(request: Request):
    return templates.TemplateResponse("listar_usuarios.html", {"request": request, "usuarios": usuarios})

@router.get("/buscar_usuario", response_class=HTMLResponse)
def form_buscar_usuario(request: Request):
    return templates.TemplateResponse("buscar_usuario.html", {"request": request})

@router.post("/buscar_usuario", response_class=HTMLResponse)
def buscar_usuario(request: Request, nome: str = Form(...)):
    for usuario in usuarios:
        if usuario["nome"] == nome:
            return templates.TemplateResponse("buscar_usuario.html", {
                "request": request,
                "usuario_encontrado": usuario
            })
    return templates.TemplateResponse("buscar_usuario.html", {
        "request": request,
        "mensagem": "Usuário não encontrado"
    })

@router.get("/deletar_usuario", response_class=HTMLResponse)
def form_deletar_usuario(request: Request):
    return templates.TemplateResponse("deletar_usuario.html", {"request": request})

@router.post("/deletar_usuario")
def deletar_usuario(nome: str = Form(...)):
    for usuario in usuarios:
        if usuario["nome"] == nome:
            usuarios.remove(usuario)
            break
    return RedirectResponse(url="/listar_usuarios", status_code=303)
