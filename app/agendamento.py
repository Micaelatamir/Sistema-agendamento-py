from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

agendamentos = []

@router.get("/criar_agendamento", response_class=HTMLResponse)
def form_criar_agendamento(request: Request):
    return templates.TemplateResponse("criar_agendamento.html", {"request": request})

@router.post("/criar_agendamento")
def criar_agendamento(nome: str = Form(...), data_txt: str = Form(...)):
    try:
        data = datetime.strptime(data_txt, "%d/%m/%Y")
    except ValueError:
        return RedirectResponse(url="/criar_agendamento", status_code=303)

    agendamento_novo = {
        "nome": nome,
        "data": data_txt
    }
    agendamentos.append(agendamento_novo)
    return RedirectResponse(url="/listar_agendamentos", status_code=303)

@router.get("/listar_agendamentos", response_class=HTMLResponse)
def listar_agendamentos(request: Request):
    return templates.TemplateResponse("listar_agendamentos.html", {
        "request": request,
        "agendamentos": agendamentos
    })

@router.get("/cancelar_agendamento", response_class=HTMLResponse)
def form_cancelar_agendamento(request: Request):
    return templates.TemplateResponse("cancelar_agendamento.html", {"request": request})

@router.post("/cancelar_agendamento")
def cancelar_agendamento(nome: str = Form(...)):
    for agendamento in agendamentos:
        if agendamento["nome"] == nome:
            agendamentos.remove(agendamento)
            break
    return RedirectResponse(url="/listar_agendamentos", status_code=303)
