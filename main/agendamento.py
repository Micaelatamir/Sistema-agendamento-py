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
    print('Cancelar de agendamento')
    


