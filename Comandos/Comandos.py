import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

print('Inicializando Jarvieees')

senhor = 'Léo'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def falar(text):
    engine.say(text)
    engine.runAndwait()

def desejo():
    hour = int(datetime.datetime.now().hour)

    if (hour >= 0 and hour < 12):
        speak('Bom dia' + senhor)

    elif (hour >= 12 and hour < 18):
        speak('Boa tarde' + senhor)

    else:
        speak('Boa noite' + senhor)

    speak('Eu sou Jarviees. Como eu poderia te ajudar?')

def comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo...')
        audio = r.listen(source)

    try:
        print('Reconhecendo...')
        pergunta = r.recognize_google(audio, language= 'pt')
        print('Voce disse:{}'.format(pergunta))

    except Exception as e:
        print('Fale de novo por favor')
        pergunta = None

    return pergunta


def main():

    desejo()
    pergunta = comando()

    if 'wikipedia' in pergunta.lower():
        speak('Pesquisando no wikipedia...')
        pergunta = pergunta.replace('wikipedia', '')
        results = wikipedia.summary(pergunta, sentence=2)
        print(results)
        speak(results)
        print('Pesquisa concluida' + senhor)

    elif 'abrir youtube' in pergunta.lower():
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        print('O youtube foi aberto senhor' + senhor)


    elif 'abrir google' in pergunta.lower():
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'abrir facebook' in pergunta.lower():
        url = 'facebook.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'abrir portal do aluno':
        url = 'senaiweb6.fieb.org.br:8080/web/app/edu/PortalEducacional/login/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'tocar musica' in pergunta.lower():
        musicas_diretorio = 'pasta com musicas'
        musicas: os.listdir(musicas_diretorio)
        print(musicas)
        os.startfile(os.path.join(musicas, musicas[0]))

    elif 'abrir bloco de notas' in pergunta.lower:
        os.startfile('notepad.exe')


