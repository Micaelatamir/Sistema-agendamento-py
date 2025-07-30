from sqlalchemy.orm import Session
from models import Usuario, Agendamento
from schemas import UsuarioCreate, AgendamentoCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criar usuário
def criar_usuario(db: Session, usuario: UsuarioCreate):
    senha_hash = pwd_context.hash(usuario.senha)
    db_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=senha_hash)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Buscar usuário por e-mail
def buscar_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

# Criar agendamento
def criar_agendamento(db: Session, agendamento: AgendamentoCreate, usuario_id: int):
    db_agendamento = Agendamento(titulo=agendamento.titulo, data_hora=agendamento.data_hora, usuario_id=usuario_id)
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

# Listar agendamentos por usuário
def listar_agendamentos(db: Session, usuario_id: int):
    return db.query(Agendamento).filter(Agendamento.usuario_id == usuario_id).all()
