from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
import schemas, crud
from models import Usuario
from passlib.context import CryptContext

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Permitir CORS (caso use frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Rota para criar usuário
@app.post("/usuarios", response_model=schemas.UserOut)
def criar_usuario(usuario: schemas.UserCreate, db: Session = Depends(get_db)):
    db_usuario = crud.buscar_usuario_por_email(db, usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.criar_usuario(db, usuario)

# Rota para login
@app.post("/login")
def login(email: str, senha: str, db: Session = Depends(get_db)):
    usuario = crud.buscar_usuario_por_email(db, email)
    if not usuario or not pwd_context.verify(senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"mensagem": "Login realizado com sucesso", "usuario_id": usuario.id}

# Rota para criar agendamento
@app.post("/usuarios/{usuario_id}/agendamentos")
def criar_agendamento(usuario_id: int, agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    return crud.criar_agendamento(db, agendamento, usuario_id)

# Rota para listar agendamentos de um usuário
@app.get("/usuarios/{usuario_id}/agendamentos")
def listar_agendamentos(usuario_id: int, db: Session = Depends(get_db)):
    return crud.listar_agendamentos(db, usuario_id)
