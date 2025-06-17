import usuario
import agendamento

print('Menu')
print('Escolhe a função que deseja: ')
print('(1) Criar usuário')
print('(2) Agendar compromisso')
print('(3) Sair do sistema')
opcao = input('Escolha uma opção:')

if opcao == "1":
  print(' Menu usuário: ')
  print('(1) Criar usuário')
  print('(2) Listar usuário')
  print('(3) Buscar usuário')
  print('(4) deletar usuário')
  usuario = input(' Escolha uma opção')

if usuario == "1" :
  criar_usuario = input()
elif usuario == "2" :
  listar_usuario = input()
elif usuario == "3" :
  escolha = input( )
elif usuario == "4" :
  deletar_usuario = input()  
elif opcao == "2" :
 agendar = input('Agendar compromisso: ')
elif opcao == "3" :
  encerramento = input(' Sair do sistema')
  print('Até mais!')
else:
 print('Erro')

