import usuario
import agendamento

print('Menu')
print('Escolhe a função que deseja: ')
print('(1)Criar usuario')
print('(2) Agendar compromisso')
print('(3) Sair do sistema')
opcao = input('Escolha uma opcao:')

if opcao == "1" :
  usuario = input('Criar usuario: ')
  print(f'Seja bem-vinda {usuario}')
elif opcao == "2" :
 agendar = input(' Agendar compromisso: ')
elif opcao == "3" :
  encerramento = input(' Sair do sistema')
  print('Até mais!')
else:
 print('Erro')

