import usuario
import agendamento

while True : 

  print('Menu')
  print('Escolhe a função que deseja: ')
  print('(1) usuário')
  print('(2) Agendar compromisso')
  print('(3) Sair do sistema')

  opcao = input('Opção selecionada: ')

  if opcao == "1":
    print(' Menu usuário:')
    print('(1) Criar usuário')
    print('(2) Listar usuário')
    print('(3) Buscar usuário')
    print('(4) deletar usuário')
    escolha_usuario = input(' Escolha uma opção')

    if escolha_usuario == "1" :
      usuario.criar_usuario ()
    elif escolha_usuario == "2" :
      usuario.lista_usuario ()
    elif escolha_usuario == "3" :
      usuario.escolha ()
    elif escolha_usuario == "4" :
      usuario.deletar_usuario () 
    

  elif opcao == "2" :
   print('Menu de agendamento')
   print('(1) Criar agendamento')
   print('(2) Listar agendamento')
   print('(3) Cancelar agendamento')
   escolha_agendamento =input('escolha uma opção: ')


   if escolha_agendamento == "1" :
    agendamento.criar_agendamento()
   elif escolha_agendamento == "2" :
    agendamento.listar_agendamento()  
   elif escolha_agendamento == "3" :
    agendamento.cancelar_agendamento()  
    


   elif opcao == "3" :
    print('Até mais!')
 
  break

else:
  print('erro')

  
