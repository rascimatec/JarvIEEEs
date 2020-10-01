"""import os
import datetime
from playsound import playsound


h = int(input('Digite as horas:')) #setar a hora que o alarme toca
m = int(input('Digite os minutos:')) #setar os minutos que o alarme toca

print('Esperando pelo alarme...', h, m) #print para verificar que foi setado

while True:
    if(h == datetime.datetime.now().hour and m == datetime.datetime.now().minute): #condicional para o alarme tocar.
        print('Está na hora!') 
        playsound('Som-alarme.mp3') #faz o arquivo mp3 tocar.
        break

#Não tá pronta"""

import _thread
import time

num_thread = 0
max_loop = 5
thread_started = False


def timer(hora=0, minuto=0, segundo=0):
    global num_thread   # número de funções em paralelas sendo executadas
    global thread_started   # Indica se a função já foi iniciada ou não
    thread_started = True  # Informa que a função foi iniciada
    num_thread += 1     # Indica que mais uma operação em paralelo foi iniciada
    delay = hora * 3600 + minuto * 60 + segundo  # Converte o tempo informado para segundos e o soma
    if delay > 0:
        delay -= 1  # apenas uma correção que busca compensar o tempo de processamento
    print("Timer iniciado")
    time.sleep(delay)  # entra em modo 'sleep' pelo tempo em segundos informado
    num_thread -= 1    # indica que um processo foi finalizado
    print('Está na hora!')
    print(num_thread)


#_thread.start_new_thread(timer, (0, 0, 4))

#Se importar com essas 4 linhas dá problema
#Encontrar outra solução ou implementar diferente
'''
while not thread_started:   # não permite que o programa finalize antes de executar a thread
    pass
while num_thread > 0:       # não permite que o programa finalize se houver alguma thread em execução
    pass'''
