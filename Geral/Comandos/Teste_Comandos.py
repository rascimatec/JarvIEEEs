import _thread
from Geral.Comandos.Comandos import *
# from Comandos import *
import datetime
from datetime import date, datetime, time, timedelta
from time import sleep
import sys

#fala_jarvieees("I3é")
#fala_jarvieees("I três é")
# from Alarme import *
# import Comandos.Alarme
#os.startfile('www.google.com')
print("Iniciando...")
#sleep(3)
if __name__ == '__main__':  # é a conexão com o banco.
    banco_de_dados = ConnectBancoDados()  # inicio da conexao
    voice_setup()         # Configura a voz do assistente
    main_stdby()
