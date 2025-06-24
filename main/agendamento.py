agendamentos =[]

def criar_agendamento() :
 nome = input('nome do evento: ')
 data = input('data do evento:')
 agendamento_novo = {
         'evento': nome, 
         'data_evento': data 
 }

 agendamentos.append(agendamento_novo)
 print('Evento criado com sucesso')

def listar_agendamento():
 print('Lista de agendamentos')
 for agendamento in agendamentos :
   print(f'{agendamento['nome']} e data do evento{agendamento['Data']} ')


def cancelar_agendamento():
 cancelar_agendamento = input( 'Digite o nome do usuario para deletar :')
 for agendamento in agendamentos:
   if agendamento == cancelar_agendamento:
    agendamentos.remove(agendamento)   
   print(f' usuario{cancelar_agendamento} com sucesso!')
   return
print('usuario inexistente')


