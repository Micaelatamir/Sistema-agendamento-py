from pydantic import BaseModel
from datetime import datetime


# --------- USUÁRIOS ---------
class UserBase(BaseModel):
    nome: str
    email: str

class UserCreate(UserBase):
    senha: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2


# --------- AGENDAMENTOS ---------
class AgendamentoBase(BaseModel):
    titulo: str
    data_hora: datetime

class AgendamentoCreate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True
