from pydantic import BaseModel, EmailStr
from datetime import datetime

class AgendamentoCreate(BaseModel):
    titulo: str
    data_hora: datetime


class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
