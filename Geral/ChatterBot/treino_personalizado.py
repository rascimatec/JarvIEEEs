from chatterbot.trainers import ListTrainer

ieee_ref = [
    "Qual melhor ramo do IEEE?",
    "O RAS",

    "O que significa IEEE?",
    "Significa Instituto de Engenheiros Eletricistas e Eletrônicos",

    "O que é o IEEE?",
    "É a maior organização técnica do mundo. Nunca ouviu falar?",
    
    "Quais os valores do IEEE?",
    "Honestidade, Confiança, Sinergia, Proatividade e Networking"

    "O que significa RAS?",
    "Significa Sociedade de Robótica e Automação",

    "O que significa PES?",
    "Significa Sociedade de Potência e Energia",

    "O que significa EMBS?",
    "Significa Sociedade de Engenharia de Medicina e Biologia",

    "Quais foram os presidentes do RAS?",
    "Boa pergunta"                                     # Listar quais foram

]

ieee_pronuncia = "i3é"  # Define como o assistente fará a pronuncia do IEEE
trocadIEEElhos = [

]

engenharia = [
    "O que é derivada?",
    "É a taxa de variação instatânea de um ponto de uma função",

    "O que é integral?",
    "A integral representa a área sobre a curva de uma função"
]


def treinar(chatbot):
    # chatbot -> instância do chatterbot criada com o ChatBot('nome')
    trainer_custom = ListTrainer(chatbot)

    trainer_custom.train(
        ieee_ref.__str__()
    )

    trainer_custom.train(
        engenharia.__str__()
    )
