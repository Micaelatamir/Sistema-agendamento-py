
usuarios = []


def criar_usuario() :
 nome = input('Digite o nome do usuário: ')
 data_nasc  = input(' Digite a data de nascimento: ')
 usuario_novo = {
     "nome": nome,
     "data_nasc": data_nasc
}
 usuarios.append(usuario_novo)
 print(f'Usuario {nome} criado com sucesso!')

def lista_usuario():
    print('Listar de usuarios')
def  buscar_usuario():
    print('Buscar pelo usuario')
def deletar_usuario():
    print('Deletar usuario')    

