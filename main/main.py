import usuario
import agendamento

print('Menu')
print('Escolhe a função que deseja: ')
print('(1)Criar usuario')
print('(2) Agendar compromisso')
print('(3) Sair do sistema')
opcao = input('Escolha uma opção:')

if opcao == "1":
  usuario = print(' Menu usuario: ')
  print('(1 )criar usuario')
  print('(2)listar')
  print('(3)buscar')
  print('(4)delentar')
  escolha_do_usuario = input(' Escolha uma opção')

if escolha_do_usuario == "1" :
  criar_usuario = input('Criar usuario: ')
elif escolha_do_usuario == "2" :
  listar = input('lista:  ')
elif escolha_do_usuario == "3" :
  escolha = input( 'escolha: ')
elif escolha_do_usuario == "4" :
  deletar = input('deletar usuario')  



elif opcao == "2" :
 agendar = input(' Agendar compromisso: ')
elif opcao == "3" :
  encerramento = input(' Sair do sistema')
  print('Até mais!')
else:
 print('Erro')

