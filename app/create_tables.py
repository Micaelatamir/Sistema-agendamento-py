from database import engine
from models import Base

print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
