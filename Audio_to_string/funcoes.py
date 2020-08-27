import speech_recognition as sr
import pyttsx3
from random import choice
from Banco_de_Respostas import *

version = "0.0.1"
reproducao = pyttsx3.init('sapi5')



def fala_jarvieees(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()


def reconhecimento():
    inicializacao = choice(lista_inicializacao)
    resposta_erro = choice(lista_erros)

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        # rec.adjust_for_ambient_noise(source)
        rec.adjust_for_ambient_noise(source, 0.75)
        print(inicializacao)
        fala_jarvieees(inicializacao)  # Está lento
        print('ok')
        audio = rec.listen(source)

        while True:
            try:
                print('Processando dados...')
                texto = rec.recognize_google(audio, language='pt-BR')
                return texto.capitalize()
            except sr.UnknownValueError:
                return resposta_erro


def intro():
    msg = f'Assistente versão {version}'
    print(f'{"-"*len(msg)}\n{msg}\n{"-"*len(msg)}')


#Está dando erro daqui pra baixo
def verifica_nome(user_name):
    if user_name.starwith("Meu nome é"):
        user_name.replace("Meu nome é", "")

    if user_name.starwith("Eu me chamo"):
        user_name.replace("Eu me chamo", "")

    return user_name


def verifica_nome_existe(nome):
    dados = open("JarvIEEEs/nomes.txt", "r")
    nome_list = dados.readlines()
    if not nome_list:
        vazio = open("JarvIEEEs/nomes.txt", "r")
        conteudo = vazio.readlines()
        conteudo.append(f'{nome}')
        vazio = open("JarvIEEEs/nomes.txt", "w")
        vazio.writelines(conteudo)
        vazio.close()

        return f'Prazer em te conhecer {nome}!'

    for linha in nome_list:
        if nome == linha:
            return f'Bem vindo de volta {nome}'

    vazio = open("JarvIEEEs/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append(f'\n{nome}')
    vazio = open("JarvIEEEs/nomes.txt", "w")
    vazio.writelines(conteudo)
    vazio.close()

    return f'Prazer em te conhecer {nome}!'


def lista_nomes():
    try:
        nome = open("JarvIEEEs/nomes.txt", "r")
        nome.close()
    except FileNotFoundError:
        nome = open("JarvIEEEs/nomes.txt", "w")
        nome.close()


def apresentacao():
    fala = reconhecimento()
    fala = verifica_nome(fala)
    lista_nomes()
    verifica_nome_existe(fala)

