import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# print('Inicializando Jarvieees')

senhor = 'senhor'
engineSPK = pyttsx3.init('sapi5')


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
    engineSPK.say(resposta)
    engineSPK.runAndWait()


def saudacao():  # Serve para que o assistente realize uma saudação
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        fala_jarvieees('Bom dia' + senhor)

    elif 12 <= hour < 18:
        fala_jarvieees('Boa tarde' + senhor)

    else:
        fala_jarvieees('Boa noite' + senhor)

    fala_jarvieees('Eu sou Jarviees. Como eu poderia te ajudar?')


def comando():  # Serve para ouvir uma frase e retorná-la como uma string
    r = sr.Recognizer()
    while True:  # Continuará neste loop até que a fala seja entendida
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, 0.75)  # Se 'adapta' aos ruídos externos
            print('Ouvindo...')
            audio = r.listen(source)

        try:
            print('Reconhecendo...')
            pergunta = r.recognize_google(audio, language='pt')
            print('Voce disse:{}'.format(pergunta))
            break

        except Exception as e:  # Caso não compreenda o que foi dito
            erro = 'Fale de novo por favor'  # Substituir por mensagens de erro do banco
            fala_jarvieees(erro)
            print(erro)

    return pergunta


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
        fala_jarvieees('Adeus!')
        return
    else:  # Ação não impementada ou conversação
        fala_jarvieees('Sinto muito, ainda não sei como responder isso')  # Mensagem provisória de erro
        print('Sinto muito, ainda não sei como responder isso')


def main():
    saudacao()
    pergunta = comando()
    print(pergunta)  # Apenas para que seja possível ver o que o assistente entedeu
    acoes(pergunta)


voice_setup()