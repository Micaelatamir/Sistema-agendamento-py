from datetime import datetime

usuarios = []


def criar_usuario() :
 nome = input('Digite o nome do usuário: ')
 data_txt  = input(' Digite a data de nascimento:(%d/%m/%Y) ')
 datetime.strptime(data_txt, "%d/%m/%Y")
 
 usuario_novo = {
     "nome": nome,
     "data_nasc": data_txt
}
 usuarios.append(usuario_novo)
 print(f'Usuario {nome} criado com sucesso!')

def lista_usuario():
   print('Lista de usuarios')
   for usuario in usuarios :
     print(f'{usuario['nome']}, nascido em {usuario['data_nasc']}')

def  buscar_usuario():
 buscar = input(' Digite o nome de usuario que deseja encontrar: ')  
 for usuario in usuarios :
   if usuario['nome'] == buscar_usuario :
     print(f' usuario{usuario['nome']}, e Data de nascimento{usuario['data_nasc']}')
     return
   print('Usuário não encontrado')

def deletar_usuario():
 deletar_usuario = input( 'Digite o nome do usuario para deletar :')
 for usuario in usuarios:
   if usuario == deletar_usuario:
    usuarios.remove(usuario)   
    print(f' usuario{deletar_usuario} com sucesso!')
   return
print('usuario inexistente')
