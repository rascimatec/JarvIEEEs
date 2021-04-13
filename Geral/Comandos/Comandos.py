import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from datetime import datetime, timedelta
from time import sleep
import requests as rq
from Geral.Auxiliar.Ponte import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer     # permite a inicialização de um bot já treinado
from chatterbot import trainers


# Variaveis globais do código
nome_assistente = 'assistente'     # nome do assistente
chatbot = ChatBot(nome_assistente)
senhor = ' senhor'       # Como o assistente chamará o usuário
version = "1.0.0"       # apenas um valor arbitrário para indicar a versão atual do software
finalizacao = ["adeus", "finalizar", "tchau"]  # Lista de comandos usados para hibernar o assistente
engineSPK = pyttsx3.init('sapi5')


def intro():
    msg = f'Assistente versão {version}'
    print('Inicializando Jarvieees')
    print(f'{"-"*len(msg)}\n{msg}\n{"-"*len(msg)}')
    saudacao()


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


def comando(imprimir=1):  # Serve para ouvir uma frase e retorná-la como uma string
    try:
        r = sr.Recognizer()
        while True:  # Continuará neste loop até que a fala seja entendida
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, 0.75)  # Se 'adapta' aos ruídos externos
                if imprimir == 1:
                    print('Ouvindo...')
                audio = r.listen(source)

            try:
                if imprimir == 1:
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


def chatter_setup():
    # A lista de dialogos do corpus:
    # https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/portuguese
    trainer = ChatterBotCorpusTrainer(chatbot)
    # treina o chatbot com listas já feitas (em português)
    # importa tudo com exceção da lista de elogios e frases sobre a unilab

    # Treina o bot com as lista do arquivo treino_personalizado
    # treinar(chatbot)

    trainer.train(
        "chatterbot.corpus.portuguese.conversations",
        #"chatterbot.corpus.portuguese.games",
        "chatterbot.corpus.portuguese.greetings",
        "chatterbot.corpus.portuguese.linguistic_knowledge",
        #"chatterbot.corpus.portuguese.money",
        "chatterbot.corpus.portuguese.proverbs",
        "chatterbot.corpus.portuguese.suggestions",
        "chatterbot.corpus.portuguese.trivia",
        "chatterbot.corpus.portuguese.custom"
    )
    #trainer.train(
    #    "chatterbot.corpus.portuguese"
    #)



def chatter_answer(request):
    response = chatbot.get_response(request)
    print(f'{nome_assistente}: {response}')
    fala_jarvieees(response)
    return response


def acoes(pergunta):  # Possíveis ações que o assistente pode executar
    pergunta = pergunta.lower()
    try:
        if ('hoje' in pergunta and 'dia' in pergunta) or ('data' in pergunta and 'hoje' in pergunta):  # não é uma boa solução porque só aceita essa frase como chave
            info_data()
            return

        elif 'hora' in pergunta or 'horário' in pergunta or 'horas' in pergunta:
            info_hora()
            return

        parametro = banco_de_dados.consulta_parametro(pergunta)  #consulta de procedimento a ser realizado EX: (abrir arq ou pesquisa)
        path = banco_de_dados.consulta(pergunta)                 #consulta de Aplicativo EX: (abrir oque ? ou pesquisar oque ?)

        if 'search' in path:  #o modelo de pesquisa foi mantido sendo somente adapitado para o banco
            os.startfile(path + pergunta)

        elif 'startfile' in parametro: #aqui ocorrem todas aberturas de programas e sites
            os.startfile(path)

        elif 'system' in parametro:    #aqui ocorrem todos os comandos em cmd
            os.system(path)

        elif 'leitura_tempo' in parametro:
            parametro(path)

        elif pergunta.lower() == 'que dia é hoje':  # não é uma boa solução porque só aceita essa frase como chave
            info_data()

        elif 'showdonw' in parametro:
            banco_de_dados.showdonw()

        elif 'conversa' in path: #aqui é condicional para que entrea função de chatbot
            fala_jarvieees('Ativando modo conversa')
            while True:
                #print('entrou')
                request = comando()
                if 'tchau' in request or 'adeus' in request:
                    break
                response = chatbot.get_response(request)
                print(f'Você: {request}')
                print(f'{nome_assistente}: {response}')
                engineSPK.say(response)
                engineSPK.runAndWait()
            fala_jarvieees('Desativando modo conversa')
            os.system('cls')
                #print('aqui')                                                       #deixei elas comentadas pois por hora nao encaixam bem

    except:                            # Anti-Erro
        print("no")


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


def leitura_tempo(msg):
    z = msg
    y = len(z)

    if y > 8:
        fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius, a pressão atmosferica é de {z[3]:.2f} atm, a umidade relativa é de {z[5]:.2f}% e a velocidade dos ventos é de {z[7]:.2f} km/h')

    elif y > 6:
        if 'r' in z and 'a' in z and 's' in z:
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius, a pressão atmosferica é de {z[3]:.2f} atm e a umidade relativa é de {z[5]:.2f}%')
        elif 'r' in z and 'a' in z and 'S' in z:
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius, a pressão atmosferica é de {z[3]:.2f} atm e a velocidade dos ventos é de {z[5]:.2f} km/h')
        elif 'r' in z and 's' in z and 'S' in z:
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius, a umidade relativa é de {z[3]:.2f}% e a velocidade do vento é de {z[5]:.2f} km/h')
        elif 'a' in z and 's' in z and 'S' in z:
            fala_jarvieees(f'A pressão atmosferica em {z[0]} é de {z[1]:.2f} atm, a umidade relativa é de {z[3]:.2f}% e a velocidade dos ventos é de {z[5]:.2f} km/h')

    elif y > 4:
        if 'r' in z and 'a' in z:
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius e a pressão atmosferica é de {z[3]:.2f} atm')
        elif 'r' in z and 's' in z:
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius e a umidade relativa é de {z[3]:.2f}%')
        elif 'r' in z and 'S' in z:
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius e a velocidade do vento é de {z[3]:.2f} km/h')
        elif 'a' in z and 's' in z:
            fala_jarvieees(f'A pressão atmosferica em {z[0]} é de {z[1]:.2f} atm e a umidade relativa é de {z[3]:.2f}%')
        elif 'a' in z and 'S' in z:
            fala_jarvieees(f'A pressão atmosferica em {z[0]} é de {z[1]:.2f} atm e a velocidade dos ventos é de {z[3]:.2f} km/h')
        elif 's' in z and 'S' in z:
            fala_jarvieees(f'A umidade relativa de {z[0]} é de {z[1]:.2f}% e a velocidade do vento é de {z[3]:.2f} km/h')

    elif y > 2:
        if 'r' in z :
            fala_jarvieees(f'A temperatuda de {z[0]} é de {z[1]:.2f} graus celsius')
        elif 'a' in z:
            fala_jarvieees(f'A pressão atmosferica de {z[0]} é de {z[1]:.2f}atm')
        elif 's' in z:
            fala_jarvieees(f'A umidade relativa de {z[0]} é de {z[1]:.2f}%')
        elif 'S' in z:
            fala_jarvieees(f'A velocidade dos ventos de {z[0]} é de {z[1]:.2f} km/h')


def clima_tempo():
    endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=5600ff2f7fb3d163a1b20079b9a063dc&q="
    fala_jarvieees('me diga oque voce gostaria de saber ?')
    resultado = comando()
    fala_jarvieees('tudo bem, qual a cidade ?')  # fala_jarvies#
    msg = comando()

    x = msg.strip()  # strip vai tirar espaço desnecessário (a mais)
    x = x.lower()  # deixa toda string minuscula
    x = x.split()  # separa a string por palavra em uma lista
    y = len(x)  # conta os elementos da lista
    n = 0  # variável auxiliar do while

    while True:
        if y > 1:
            cidade = x[n] + '+' + x[n + 1]
        else:
            cidade = x[n]
            url = endereco_api + cidade
            infos = rq.get(url).json()

    temp = infos['main']['temp'] - 273.15  # Kelvin para Celsius
    pressao_atm = infos['main']['pressure'] / 1013.25  # rLibas para ATM
    umidade = infos['main']['humidity']  # Recebe em porcentagem

    v_speed = infos['wind']['speed']  # km/ h

    x = resultado.strip()  # strip vai tirar espaço desnecessário (a mais)
    x = x.lower()  # deixa toda string minuscula
    x = x.split()  # separa a string por palavra em uma lista
    y = len(x)  # conta os elementos da lista
    n = 0  # auxiliar do while
    lis = [msg]  # lista que faz a magica

    while (n != y):
        if 'tem' in x[n]:
            lis = lis + [temp, 'r']
        elif 'p' in x[n]:
            lis = lis + [pressao_atm, 'a']
        elif 'u' in x[n]:
            lis = lis + [umidade, 's']
        elif 'v' in x[n]:
            lis = lis + [v_speed, 'S']
            n = n + 1


    return lis

#leitura_tempo(clima_tempo())


if __name__ == '__main__':  # é a conexão com o banco.
    banco_de_dados = ConnectBancoDados()  # inicio da conexao
    voice_setup()         # Configura a voz do assistente
    chatter_setup()
    os.system('cls')
   # intro()
    main_stdby()

