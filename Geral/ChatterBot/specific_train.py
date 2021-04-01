from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer     # permite a inicialização de um bot já treinado
#from Geral.ChatterBot.treino_personalizado import *

# Create a new chat bot named Charlie
nome = 'Charlie'
chatbot = ChatBot(nome)

# A lista de dialogos do corpus:
# https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/portuguese
trainer = ChatterBotCorpusTrainer(chatbot)
# treina o chatbot com listas já feitas (em português)
# importa tudo com exceção da lista de elogios e frases sobre a unilab

# Treina o bot com as lista do arquivo treino_personalizado
# treinar(chatbot)

'''trainer.train(
    "chatterbot.corpus.portuguese.conversations",
    #"chatterbot.corpus.portuguese.games",
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.linguistic_knowledge",
    #"chatterbot.corpus.portuguese.money",
    "chatterbot.corpus.portuguese.proverbs",
    "chatterbot.corpus.portuguese.suggestions",
    "chatterbot.corpus.portuguese.trivia",
)'''

trainer.train(
    #"C:/Users/jgabr/Documents/GitHub/JarvIEEEs/Geral/ChatterBot/ieee.yml"
    #"chatterbot.corpus.portuguese.custom.ieee"
    "chatterbot.corpus.portuguese"
)


# Os pacotes colocados como comentários pertencem a novas versões da biblioteca, ou seja, não temos

while True:
    request = str(input("Você: "))
    response = chatbot.get_response(request)
    print(f'{nome}: {response}')

# https://chatterbot.readthedocs.io/en/stable/training.html
