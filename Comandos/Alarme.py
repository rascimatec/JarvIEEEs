import os 
import datetime
from playsound import playsound


h = int(input('Digite as horas:')) #setar a hora que o alarme toca
m = int(input('Digite os minutos:')) #setar os minutos que o alarme toca

print('Esperando pelo alarme...', h, m) #print para verificar que foi setado

while True:
    if(h == datetime.datetime.now().hour and m == datetime.datetime.now().minute): #conficional para o alarme tocar.
        print('Está na hora!') 
        playsound('Som-alarme.mp3') #faz o arquivo mp3 tocar.
        break

#Não tá pronta