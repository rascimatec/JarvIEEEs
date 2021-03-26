import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from datetime import datetime, timedelta
from time import sleep
from Geral.Auxiliar.Ponte import *



# print('Inicializando Jarvieees')

# Variaveis globais do código
nome_assistente = 'assistente'     # nome do assistente
senhor = ' senhor'       # Como o assistente chamará o usuário
version = "1.0.0"       # apenas um valor arbitrário para indicar a versão atual do software
finalizacao = ["adeus", "finalizar", "tchau"]  # Lista de comandos usados para hibernar o assistente
engineSPK = pyttsx3.init('sapi5')


def intro():
    msg = f'Assistente versão {version}'
    print(f'{"-"*len(msg)}\n{msg}\n{"-"*len(msg)}')


def voice_setup():
    """RATE"""
    rate = engineSPK.getProperty('rate')
    engineSPK.setProperty('rate', 180)  # Configura a velocidade da fala

    """VOLUME"""
    volume = engineSPK.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engineSPK.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engineSPK.getProperty('voices')
    # Por algum motivo o indice '1' altera o idioma e não a voz
    # EASTER EGG ->
    engineSPK.setProperty('voice', voices[0].id)


def fala_jarvieees(resposta):  # Recebe uma string e responde com a mesma em forma de áudio
    print(nome_assistente + ': ' + resposta)
    engineSPK.say(resposta)
    engineSPK.runAndWait()


def saudacao():  # Serve para que o assistente realize uma saudação
    hour = int(datetime.now().hour)

    if 0 <= hour < 12:
        fala_jarvieees('Bom dia' + senhor)

    elif 12 <= hour < 18:
        fala_jarvieees('Boa tarde' + senhor)

    else:
        fala_jarvieees('Boa noite' + senhor)

    fala_jarvieees('Eu sou Jarviees. Como eu poderia te ajudar?')


def info_data():
    number_to_day = {
        '01': 'primeiro',
        '02': 'dois',
        '03': 'três',
        '04': 'quatro',
        '05': 'cinco',
        '06': 'seis',
        '07': 'sete',
        '08': 'oito',
        '09': 'nove',
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'catorze',
        '15': 'quinze',
        '17': 'dezeseis',
        '18': 'dezoito',
        '19': 'dezenove',
        '20': 'vinte',
        '21': 'vinte e um',
        '22': 'vinte e dois',
        '23': 'vinte e três',
        '24': 'vinte e quatro',
        '25': 'vinte e cinco',
        '26': 'vinte e seis',
        '27': 'vinte e sete',
        '28': 'vinte e oite',
        '29': 'vinte e nove',
        '30': 'trinta',
        '31': 'trinta e um'
    }

    number_to_month = {
        '01': 'janeiro',
        '02': 'fevereiro',
        '03': 'março',
        '04': 'abril',
        '05': 'maio',
        '06': 'junho',
        '07': 'julho',
        '08': 'agosto',
        '09': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }
    data = str(datetime.now().date())
    # fatiamento da string original para separar informações e conversão dos algarismos em palavras
    # Original: YEAR-MT-DY (ano-mês-dia)
    dia = number_to_day[data[8:]]  # 2 últimos caracteres
    mes = number_to_month[data[5:7]]    # 5° e 6° dígito da data
    ano = data[0:4]     # Primeiros 4 caracteres
    frase = f'hoje é {dia} de {mes} de {ano}'
    fala_jarvieees(frase)


def info_hora():
    tempo = str(datetime.now().time())
    hora = tempo[:2]
    minuto = tempo[3:5]
    frase = f'são {hora} e {minuto}'
    fala_jarvieees(frase)


def despedida():        # Serve apenas para o assistente se depedir
    fala_jarvieees('Adeus!')


def comando():  # Serve para ouvir uma frase e retorná-la como uma string
    try:
        r = sr.Recognizer()
        while True:  # Continuará neste loop até que a fala seja entendida
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, 0.75)  # Se 'adapta' aos ruídos externos
                print('Ouvindo...')
                audio = r.listen(source)

            try:
                print('Reconhecendo...')
                pergunta = r.recognize_google(audio, language='pt')
                #print('Voce disse:{}'.format(pergunta))
                break

            except Exception as e:  # Caso não compreenda o que foi dito
                erro = 'Fale de novo por favor'  # Substituir por mensagens de erro do banco
                #fala_jarvieees(erro)
                print(erro)

        return str(pergunta)
    except:
        fala_jarvieees("Conecte um microfone")
        comando()


def comando_stdby():  # Serve para ouvir uma frase e retorná-la como uma string
    try:
        r = sr.Recognizer()
        while True:  # Continuará neste loop até que a fala seja entendida
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, 0.75)  # Se 'adapta' aos ruídos externos
                audio = r.listen(source)

            try:
                pergunta = r.recognize_google(audio, language='pt')
                break

            except Exception as e:  # Caso não compreenda o que foi dito
                erro = 'Fale de novo por favor'  # Substituir por mensagens de erro do banco
        print(pergunta)
        return str(pergunta)
    except:
        fala_jarvieees("Conecte um microfone")
        comando_stdby()


# erro para números de duas ou mais palavra ex: vinte e um
def string_to_int(frase):
    # adaptado de https://www.geeksforgeeks.org/python-convert-numeric-words-to-numbers/
    help_dict = {
        'um': '1',
        'uma': '1',
        'dois' : '2',
        'duas': '2',
        'três': '3',
        'quatro': '4',
        'cinco': '5',
        'seis': '6',
        'sete': '7',
        'oito': '8',
        'nove': '9',
        'dez': '10',
        'onze': '11',
        'doze': '12',
        'treze': '13',
        'catorze': '14',
        'quinze': '15',
        'dezeseis': '17',
        'dezoito': '18',
        'dezenove': '19',
        'vinte': '20',
        'vinte e um': '21',
    }

    # Convert numeric words to numbers
    # Using join() + split()
    res = ""  # retorna essa frase caso não haja um número
    for ele in frase.split():
        if ele in help_dict:
            res += help_dict[ele] + ' '
    return res


def pkill(process_name):
    processos = os.popen('tasklist').readlines()
    for i in processos:
        # print(i[0:27])
        palavra = ''
        for n in i:
            if n != ' ':
                palavra += n
            else:
                break
        print(f'palavra:{palavra}  i:{i}')
        if process_name.strip() == palavra.strip():
            print('\n\nkill process\n\n')
        else:
            #processo não encontrado
            return 0
    try:
        killed = os.system('taskkill /im ' + process_name)
    except Exception as e:
        print('Erro!!')
        killed = 0
    return killed


# Seria mais interessante se essa função funcionasse em paralelo e não interrompesse todo o programa
def timer(frase):
    now = datetime.now().time()
    tempo = int(string_to_int(frase))
    print(tempo)
    if tempo != "sem numero":
        # Just use January the first, 2000
        d1 = datetime(2000, 1, 1, now.hour, now.minute, now.second)
        d2 = d1 + timedelta(hours=0, minutes=0, seconds=tempo)  # Deve ser substituido pelo tempo dito
        fala_jarvieees(f'Te aviso quando der {d2.hour} e {d2.minute}')
        print(d2.time())

        while True:
            now = datetime.now().time()
            time = datetime(2000, 1, 1, now.hour, now.minute, now.second)
            print(d2 - time)
            if d2 - time <= timedelta(0, 0, 0, 0, 0, 0):
                break
            sleep(1)
        fala_jarvieees('Timer concluído!')


def acoes(pergunta):  # Possíveis ações que o assistente pode executar
    try:

        parametro = banco_de_dados.consulta_parametro(pergunta)  #consulta de procedimento a ser realizado EX: (abrir arq ou pesquisa)
        path = banco_de_dados.consulta(pergunta)                 #consulta de Aplicativo EX: (abrir oque ? ou pesquisar oque ?)
        if 'search' in path:  #o modelo de pesquisa foi mantido sendo somente adapitado para o banco
            os.startfile(path + pergunta)

        elif 'startfile' in parametro: #aqui ocorrem todas aberturas de programas e sites
            os.startfile(path)

        elif 'system' in parametro:    #aqui ocorrem todos os comandos em cmd
            os.system(path)

        #elif pergunta == 'que dia é hoje':  # não é uma boa solução porque só aceita essa frase como chave
        #info_data()
                                                                        #deixei elas comentadas pois por hora nao encaixam bem
        #elif pergunta == 'que horas são':
        #info_hora()

    except:                            # Anti-Erro
        print("no")


def main():

    pergunta = comando()
    print(pergunta)  # Apenas para que seja possível ver o que o assistente entedeu
    acoes(pergunta)


# Função semelhante a função main(), com a diferença da aplicação do funcionamento em stand-by
def main_stdby():
    start = True    # Estado inicial do assistente: ativo(True) ou standby(False)
    fim = False     # Se um dos comandos de finalização for dito o programa é incerrado
    #saudacao()
    while not fim:
        if start:
            pergunta = comando()
        else:
            pergunta = comando_stdby()

        if pergunta is str:
            print("É string")
        if nome_assistente in pergunta:    # Se o nome do assistente for dito
            start = True

        if 'valeu' in pergunta:
            fala_jarvieees('Me chame novamente se precisar')
            start = False

        if start and not fim:   # Se não estiver em standby nem em finalização
            for c in finalizacao:
                if c in pergunta:
                    fim = True
                    despedida()
                    return

            print(pergunta)  # Apenas para que seja possível ver o que o assistente entedeu
            acoes(pergunta)  # Função principal responsável pela maior parte das ações


if __name__ == '__main__':  # é a conexão com o banco.
    banco_de_dados = ConnectBancoDados()  # inicio da conexao
    voice_setup()         # Configura a voz do assistente
    main_stdby()
