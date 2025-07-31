from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session
from crud import criar_agendamento, listar_agendamentos
from schemas import AgendamentoCreate
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Rota: Formulário de agendamento
@router.get("/criar_agendamento", response_class=HTMLResponse)
def form_criar_agendamento(request: Request):
    return templates.TemplateResponse("criar_agendamento.html", {"request": request})

# Rota POST: Salvar agendamento no PostgreSQL
@router.post("/criar_agendamento")
def salvar_agendamento(
    request: Request,
    titulo: str = Form(...),
    data_hora: str = Form(...),  # Formato esperado: "YYYY-MM-DDTHH:MM" (datetime-local)
    usuario_id: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # Converter a string para datetime
        data_hora_obj = datetime.strptime(data_hora, "%Y-%m-%dT%H:%M")
        agendamento = AgendamentoCreate(titulo=titulo, data_hora=data_hora_obj)
        criar_agendamento(db, agendamento, usuario_id)
        return RedirectResponse(url="/listar_agendamentos", status_code=303)
    except ValueError as e:
        return templates.TemplateResponse("criar_agendamento.html", {
            "request": request,
            "erro": f"Formato de data inválido: {e}"
        })

# Rota: Listar agendamentos
@router.get("/listar_agendamentos", response_class=HTMLResponse)
def mostrar_agendamentos(request: Request, db: Session = Depends(get_db)):
    agendamentos = listar_agendamentos(db, usuario_id=1)  # Substitua 1 pelo ID do usuário logado
    return templates.TemplateResponse("listar_agendamentos.html", {
        "request": request,
        "agendamentos": agendamentos
    })