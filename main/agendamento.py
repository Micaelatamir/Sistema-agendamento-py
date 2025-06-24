agendamentos =[]

def criar_agendamento() :
 nome = input('nome do evento: ')
 data = input('data do evento:')
 agendamento_novo = {
         'nome': nome, 
         'data': data 
 }

 agendamentos.append(agendamento_novo)
 print('Evento criado com sucesso')

def listar_agendamento():
 print('Lista de agendamentos')
 for agendamento in agendamentos :
   print(f'{agendamento["nome"]} e data do evento{agendamento["data"]} ')


def cancelar_agendamento():
 cancelar_agendamento = input( 'Digite o nome do usuario para deletar :')
 encontrado = False
 for agendamento in agendamentos:
  if agendamento['nome'] == cancelar_agendamento:
     agendamentos.remove(agendamento)   
     print(f' usuario{cancelar_agendamento} com sucesso!')
     encontrado = True
     break
 if not encontrado :
   print('Evento inexistente')



