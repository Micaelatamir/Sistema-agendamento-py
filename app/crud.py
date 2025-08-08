from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def criar_usuario(db: Session, usuario: schemas.UserCreate):
    senha_hash = pwd_context.hash(usuario.senha)
    db_usuario = models.Usuario(email=usuario.email, senha=senha_hash, nome="Usuário")
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def buscar_usuario_por_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def criar_agendamento(db: Session, agendamento: schemas.AgendamentoCreate, usuario_id: int):
    db_agendamento = models.Agendamento(**agendamento.dict(), usuario_id=usuario_id)
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

def listar_agendamentos(db: Session, usuario_id: int):
    return db.query(models.Agendamento).filter(models.Agendamento.usuario_id == usuario_id).all()
