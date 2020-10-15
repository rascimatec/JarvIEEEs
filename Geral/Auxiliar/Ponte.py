from Geral.DataBase.conexao_banco import *
from Geral.Audio_to_string.funcoes import *
from Geral.Comandos.Comandos import *


#Arquivo ponte para importaçoes

if __name__ == '__main__': #é a conexão com o banco.
    banco_de_dados = ConnectBancoDados() #inicio da conexao
    retorno = banco_de_dados.consulta("Paige abra o trello porfavor")
    print(retorno)
