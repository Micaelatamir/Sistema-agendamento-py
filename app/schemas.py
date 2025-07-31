from pydantic import BaseModel, EmailStr
from datetime import datetime

class AgendamentoCreate(BaseModel):
    titulo: str
    data_hora: datetime



class UserBase(BaseModel):
    nome: str  
    email: EmailStr

class UserCreate(UserBase):
    senha: str 

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
