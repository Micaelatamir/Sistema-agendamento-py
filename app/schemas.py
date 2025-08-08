from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    senha: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class AgendamentoBase(BaseModel):
    titulo: str
    data_hora: datetime

class AgendamentoCreate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True
