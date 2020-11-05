import pyttsx3
import speech_recognition as sr
#import datetime
import wikipedia
import webbrowser
import os
from datetime import datetime, timedelta
from time import sleep
import keyboard
from Geral.Auxiliar.Ponte import *

if __name__ == '__main__': #é a conexão com o banco.
    banco_de_dados = ConnectBancoDados() #inicio da conexao
    retorno = banco_de_dados.consulta("Paige abra trello porfavor")
    print(retorno)

# print('Inicializando Jarvieees')

# Variaveis globais do código
nome_assistente = 'assistente'     # nome do assistente
senhor = 'senhor'       # Como o assistente chamará o usuário
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
    engineSPK.setProperty('voice', voices[0].id)


def fala_jarvieees(resposta):  # Recebe uma string e responde com a mesma em forma de áudio
    print(nome_assistente + ': ' + resposta)
    engineSPK.say(resposta)
    engineSPK.runAndWait()


def saudacao():  # Serve para que o assistente realize uma saudação
    hour = int(datetime.now().hour)

    if 0 <= hour < 12:
        fala_jarvieees('Bom dia ' + senhor)

    elif 12 <= hour < 18:
        fala_jarvieees('Boa tarde ' + senhor)

    else:
        fala_jarvieees('Boa noite ' + senhor)

    fala_jarvieees('Eu sou Jarviees. Como eu poderia te ajudar?')


def info_data():
    # INCOMPLETO
    number_to_day = {
        '00': 'meia noite',
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
    # INCOMPLETO

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
    #r = sr.Recognizer()
    while True:  # Continuará neste loop até que a fala seja entendida
        r = sr.Recognizer()  # essa linha de código foi movida a fim de testar mudanças na velocidade
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

    return pergunta


def comando_stdby():  # Serve para ouvir uma frase e retorná-la como uma string
    #r = sr.Recognizer()
    while True:  # Continuará neste loop até que a fala seja entendida
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, 0.75)  # Se 'adapta' aos ruídos externos
            audio = r.listen(source)

        try:
            pergunta = r.recognize_google(audio, language='pt')
            break

        except Exception as e:  # Caso não compreenda o que foi dito
            erro = 'Fale de novo por favor'  # Substituir por mensagens de erro do banco
    return pergunta


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


# Apenas ideias ainda não implementadas
def write_notepad():
    keyboard.press_and_release('shift, space')
    frase = ''
    keyboard.write(frase) # A frase vem aqui

    # Blocks until you press esc.
    keyboard.wait('esc')

    # Block forever, like `while True`.
    keyboard.wait()


# função para finalizar um processo em execução

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


def acoes(pergunta):  # Possíveis ações que o assistente pode executar
    pergunta = pergunta.lower()  # Torna todas as letras minúsculas
    if 'wikipedia' in pergunta:
        fala_jarvieees('Pesquisando no wikipedia...')
        pergunta = pergunta.replace('wikipedia', '')
        results = wikipedia.summary(pergunta, sentences=2)
        print(results)
        fala_jarvieees(results)
        print('Pesquisa concluida' + senhor)

    # uma versão alternativa da ação acima, mas, não exige que a palavra chave é 'pesquise' ao invés
    # de 'wikipedia'
    elif 'pesquise' in pergunta:
        fala_jarvieees('Pesquisando no wikipedia...')
        pergunta = pergunta.replace('pesquise', '')
        results = wikipedia.summary(pergunta, sentences=2)
        print(results)
        fala_jarvieees(results)
        print('Pesquisa concluida' + senhor)

    elif 'abrir youtube' in pergunta:
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        print('O youtube foi aberto senhor' + senhor)

    elif 'abrir google' in pergunta:
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'abrir facebook' in pergunta:
        url = 'facebook.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'abrir portal do aluno' in pergunta:
        url = 'senaiweb6.fieb.org.br:8080/web/app/edu/PortalEducacional/login/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'tocar musica' in pergunta:
        musicas_diretorio = 'pasta com musicas'
        musicas: os.listdir(musicas_diretorio)
        print(musicas)
        os.startfile(os.path.join(musicas, musicas[0]))

    elif 'abrir bloco de notas' in pergunta:
        os.startfile('notepad.exe')

    elif 'fechar' in pergunta:
        p = str(input('digite o nome do processo: ')) # definir o nome do processo a ser finalizado.
        os.system('taskkill /im '+(p)) #os.system permite que você digite diretamente no cmd. taskkill /im (nome do processo) é um comando do cmd que finaliza processos.

    elif 'desligar computador' in pergunta:
        os.system('shutdown /s') #os.system permite que você digite diretamente no cmd. shutdown /s é um comando do cmd para desligar a máquina.

    elif 'reiniciar computador' in pergunta:
        os.system('shutdown /r /t 0') #shutdown /r /t 0 é um comando do cmd para reiniciar a máquina.

    elif 'hibernar computador' in pergunta:
        os.system('shutdown /h') #shutdown /h é um comando do cmd para hiberna a máquina.

    elif 'finalizar' in pergunta:
        despedida()

    elif 'timer' in pergunta:
        timer(pergunta)

    elif nome_assistente in pergunta:
        fala_jarvieees('Estou aqui ' + senhor)

    elif pergunta == 'que dia é hoje':  # não é uma boa solução porque só aceita essa frase como chave
        info_data()

    elif pergunta == 'que horas são':
        info_hora()

    else:  # Ação não impementada ou conversação
        fala_jarvieees('Sinto muito, ainda não sei como responder isso')  # Mensagem provisória de erro
        print('Sinto muito, ainda não sei como responder isso')


def main():
    saudacao()
    pergunta = comando()
    print(pergunta)  # Apenas para que seja possível ver o que o assistente entedeu
    acoes(pergunta)


# Função semelhante a função main(), com a diferença da aplicação do funcionamento em stand-by
def main_stdby():
    start = True   # Estado inicial do assistente: ativo(True) ou standby(False)
    fim = False     # Se um dos comandos de finalização for dito o programa é incerrado
    #saudacao()
    while not fim:
        if start:
            pergunta = comando()
        else:
            pergunta = comando_stdby()

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


voice_setup()                # Configura a voz do assistente
