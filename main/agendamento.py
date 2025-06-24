agendamentos =[]

def criar_agendamento() :
 compromisso = input('nome do evento: ')
 data_compromisso = input('data do evento:')
 agendamento_novo = {
         'evento': compromisso, 
         'data':  data_compromisso
 
 }

 agendamentos.append(agendamento_novo)
 print('Evento criado com sucesso')

def listar_agendamento():
  nomel = input('Digite o nome :') 
  data_evento = input()
def cancelar_agendamento():
    print('Cancelar de agendamento')
    


