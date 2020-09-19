import _thread
from Comandos import *
import datetime
from datetime import date, datetime, time, timedelta
from time import sleep
from Alarme import *
#import Comandos.Alarme


'''env = {'HOME': 'C:\Program Files (x86)\Dev-Cpp'}
exec_path = os.get_exec_path(env)

# Print the list
print("Following paths will be searched for a named executable:")
print(exec_path)'''
#os.startfile('Timer.exe')
#print(1 + int(string_to_int('catorze')))
#timer('catorze minutos')
#tempo = string_to_int('vinte')
_thread.start_new_thread(timer, (0, 0, 4))
#print(tempo)
#main()
print('Finalizou')
