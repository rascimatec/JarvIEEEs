from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer     # permite a inicialização de um bot já treinado
# Create a new chat bot named Charlie
nome = 'Charlie'
chatbot = ChatBot(nome)

'''
# Dessa forma o treinamento se dará inteiramento com a lista abaixo e as interações
trainer = ListTrainer(chat_name)
trainer.train([
    "Olá!",
    "Oi, como vai?",
    "Vou bem e você?"
])'''

trainer = ChatterBotCorpusTrainer(chatbot)
# treina o chatbot com listas já feitas (em português)
trainer.train("chatterbot.corpus.portuguese")

# Retorna uma resposta para o texto digitado
while True:
    request = str(input("Você: "))
    response = chatbot.get_response(request)
    print(f'{nome}: {response}')
