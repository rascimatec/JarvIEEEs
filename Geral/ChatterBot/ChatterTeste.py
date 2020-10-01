#from __future__ import time
import nltk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.portuguese")

# Get a response to an input statement
chatbot.get_response("Olá")

chatbot2 = ChatBot('Ron Obvious2')

# Create a new trainer for the chatbot
trainer2 = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer2.train("chatterbot.corpus.portuguese")

# Get a response to an input statement
chatbot2.get_response("Olá")

# Get a response to the input text 'I would like to book a flight.'
pergunta = chatbot.get_response('Você quer destruir a humanidade?')
response = chatbot2.get_response('Marvel ou DC?')
while True:
    pergunta = chatbot.get_response(response)
    response = chatbot2.get_response(pergunta)
    print(f'Bot 1: {pergunta}\nBot 2: {response}\n')

    response = chatbot2.get_response(pergunta)# só tá repitindo
    pergunta = chatbot.get_response(response)

    print(f'Bot 1: {response}\nBot 2: {pergunta}\n')