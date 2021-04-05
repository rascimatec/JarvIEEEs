import psycopg2
import os
from Geral.Comandos.Comandos import *
#from Geral.Auxiliar.Ponte import *


#IMPORTAÇAO DA BIBLIOTECA PSYCOPG2
#from Geral.Auxiliar.ponte import *("Utilizem essa importaçao levar os codigo para o arquivo que vc quiser")
#no momento o Banco ainda nao esta completamente povoado por isso as chamadas que ja estao no banco
# com os parametro de retornos corretos sao:
#"abra o facebook"; "abra o google"; "abra o youtube";"abra o trello"
#VALE DIZER que vcs podem colocar qualquer texto antes ou depois da consulta
#precisa apenas que estas palavras estajam em ordem  EX: "paige se nao for incomodo ABRA O YOUTUBE porfavor"
#elas retornaram o url salvo desses sites
#
#if __name__ == '__main__': #é a conexão com o banco.
#    banco_de_dados = ConnectBancoDados() #inicio da conexao
#    retorno = banco_de_dados.consulta("Paige se nao for incomodo abra o youtube porfavor")
#    print(retorno)
#
#retorno = banco_de_dados.consulta("abra o youtube")
#print(retorno)
#
#   SEMPRE QUE FOREM FAZER UMA CONSULTA SERA NESCESSARIO ESSE IF
#   (Somente pela primeira vez, nas demais a consulta pode ser realizada como no exemplo de baixo)
#   JA QUE A FUNÇAO CONSULTA TEM RETORNO VCS PRECISAM GUARDA-LA EM UM VARIAVEL DE SEU INTERESSE
#   O PRINT PODE SAIR DALI ELE ESTA APENAS PARA EFEITOS DE TESTE
#

class ConnectBancoDados:
    def __init__(self): #são os parametros para a conexão com o banco de dados
        try:
            self.connection = psycopg2.connect(
                "dbname='upsaude19' user='upsaude19' host='pgsql.upsaude.net.br' password='080901' port='5432'")
            self.connection.autocommit = True #update do banco automaticamente 
            self.cursor = self.connection.cursor() 
        except:
            print("Nao foi possivel conectar ao banco de dados")


    def insert_record (self): #função para adicionar elementos as tabelas.
        #tabela 1 = Aplicativo, tabela 2 = comando, tabela 3 = dicionario
        try:
            bla = 'bla'
            while True:
                if bla == 'n':
                    break
                r1 = input("Deseja fazer um cadastro completo ? ex: comando+palavra de ligaçao+aplicativo (s/n) ?").lower().strip()
                r2 = input("Deseja cadastrar apenas um novo aplicativo (s/n) ?").lower().strip()



                if r1 == 's':# Cadastro completo

                    comando = input('Por favor, digite o comando desejado. (Ex:Abra, feche)').lower().strip()
                    palavra = comando
                    sinonimo = input('Por favor, digite um sinonimo para o comando listado. (Ex:Abrir, fechar)').lower().strip()
                    sinonimo_2 = input('Por favor, digite outro sinonimo, pode ser em outras linguas se desejar').lower().strip()
                    parametro = input('Por favor, digite o parametro para esse comando (Ex:os.starfile)').lower().strip()
                    aplicativo = input('Por favor, digite o nome da aplicação. (Ex:facebook, youtube)').lower().strip()
                    id_comando = input('Por favor, digite o nome do comando que deseja atribuir a esse aplicativo. (use o salvo na tabela comando)').lower().strip()
                    caminho = input('Por favor, digite o caminho do aplicativo. (Ex: https:youtube.com)').lower().strip()
                    artigo = input('Por favor, digite um palavra de ligação para frase. (Ex:Abra ''O'' youtube)').lower().strip()
                    id_dicionario = id_comando

                    insert_command = "INSERT INTO comando(comando, acao) VALUES('" + comando + "','" + bla + "') INSERT INTO dicionario(palavra, sinonimo, sinonimo_2, parametro) VALUES('" + palavra + "','" + sinonimo + "','" + sinonimo_2 + "','" + parametro + "') INSERT INTO aplicativo(id_comando, aplicativo, caminho, artigo, id_dicionario) VALUES('SELECT id_comando FROM comando where comando =" + id_comando + "','" + aplicativo + "','" + caminho + "','" + artigo + "','SELECT id_dicionario FROM dicionario where palavra =" + id_dicionario + "')"

                elif r2 == 's':#cadastro aplicativo

                    aplicativo = input('Por favor, digite o nome da aplicação. (Ex:facebook, youtube)').lower().strip()
                    id_comando = input('Por favor, digite o nome do comando que deseja atribuir a esse aplicativo. (use o salvo na tabela comando)').lower().strip()
                    caminho = input('Por favor, digite o caminho do aplicativo. (Ex: https:youtube.com)').lower().strip()
                    artigo = input('Por favor, digite um verbo de ligação para frase. (Ex:Abra ''O'' youtube)').lower().strip()
                    id_dicionario = id_comando

                    insert_command = "INSERT INTO aplicativo(id_comando, aplicativo, caminho, artigo, id_dicionario) VALUES('SELECT id_comando FROM comando where comando =" + id_comando + "','" + aplicativo + "','" + caminho + "','" + artigo + "','SELECT id_dicionario FROM dicionario where palavra =" + id_dicionario +"')"

                elif r1 and r2 == 'n':
                    break

                else:
                    while True:
                        p = input('porfavor digite apenas "s" ou "n" deseja tentar novamente ?' ).lower().strip()

                        if p == 's':
                            break
                        elif p == 'n':
                            bla = 'n'
                            break


            self.cursor.execute(insert_command) #execuçao do comando em SQL

        except:
            print('nao foi possivel realizar o cadastro no banco de dados, tente novamente.')

    def consulta (self, msg): #funçao de consulta com o banco de dados

        try:
            x = msg.strip() #strip vai tirar espaço desnecessário (a mais)
            x = x.lower() #deixa toda string minuscula
            x = x.split() #separa a string por palavra em uma lista
            y = len(x) #conta os elementos da lista
            n = 0 # variável auxiliar do while

            while(n != y): # percorre todos os elementos da lista e comparando com o banco de dados


                self.cursor.execute(
                    f"SELECT caminho FROM comando JOIN aplicativo ON comando.id_comando = aplicativo.id_comando JOIN dicionario ON aplicativo.id_dicionario = dicionario.id_dicionario WHERE comando.comando = '{x[n]}' AND aplicativo.artigo ='{x[n + 1]}' AND aplicativo.aplicativo = '{x[n + 2]}' OR dicionario.sinonimo = '{x[n]}' AND aplicativo.artigo = '{x[n + 1]}' AND aplicativo.aplicativo = '{x[n + 2]}' OR dicionario.sinonimo_2 = '{x[n]}' AND aplicativo.artigo = '{x[n + 1]}' AND aplicativo.aplicativo = '{x[n + 2]}' OR comando.comando = '{x[n]}' AND aplicativo.aplicativo = '{x[n + 1]}' OR dicionario.sinonimo = '{x[n]}' AND aplicativo.aplicativo = '{x[n + 1]}' OR dicionario.sinonimo_2 = '{x[n]}' AND aplicativo.aplicativo = '{x[n + 1]}'")
                rows = self.cursor.fetchall()
            
                #Select é o comando em sql para realizar consultas
                #O mesmo esta consultando a açao e o comando e retornando o caminho/parametro

                for row in rows:
                    retorno = row[0]
                    if retorno == "pesq":       #Processo feito apenas para pesquisar, ja que ela precisam
                        x = msg.strip()         #de um retorno diferente de um aplicativo
                        x = x.lower()
                        y = x.find("google")    #Verificando se o google encontrase na frase
                        if y == -1:
                            y = x.find("mozila")#Verificando se o mozila
                            if y == -1:
                                y = x.find("opera")#Verificando o Opera
                                if y == -1:        #o Retorno da funçao find quando nao encotrado é sempre -1
                                    break
                                else:
                                    y = y + 6      #ajustando a frase para pegar apenas a pesquisa
                                    retorno = x[y:]
                            else:
                                y = y + 7          #ajustando a frase para pegar apenas a pesquisa
                                retorno = x[y:]
                        else:
                            y = y + 7              #ajustando a frase para pegar apenas a pesquisa
                            retorno = x[y:]

                    return(retorno)

                n = n + 1
                    #For apenas para selecionar e armazenar o retorno do banco

        except:     #Existe apenas para evitar erros e travamentos no codigo
            print("Sinto muito mas nao sei oque responder")
            '''fala_jarvieees("Sinto muito mas nao sei oque responder, gostaria que eu pesquise sobre isso ?")
            reposta = comando()
            resposta = reposta.lower()
            if resposta == 'sim' or 'claro' or 'faça':
                os.startfile('https://www.google.com.br/search?q=' + msg)'''


    def consulta_parametro (self, msg):
        try:
            x = msg.strip() #strip vai tirar espaço desnecessário (a mais)
            x = x.lower() #deixa toda string minuscula
            x = x.split() #separa a string por palavra em uma lista
            y = len(x) #conta os elementos da lista
            n = 0 # variável auxiliar do while

            while (n != y):  # percorre todos os elementos da lista e comparando com o banco de dados

                self.cursor.execute(
                    f"SELECT parametro FROM dicionario WHERE palavra = '{x[n]}' OR sinonimo = '{x[n]}' OR sinonimo_2 = '{x[n]}'")
                rows = self.cursor.fetchall()

                # Select é o comando em sql para realizar consultas
                # O mesmo esta consultando a açao e o comando e retornando o caminho/parametro

                for row in rows:
                    retorno = row[0]
                    return (retorno)

                n = n + 1
        except:
            print("n")

    def showdonw (self): #exibe a tabela do banco de dados


        while True: #vizualizaçao do banco de dados via terminal python
                    

            fala_jarvieees("Qual tabela deseja exibir (comando, dicionario, aplicativo) ? :")
            while True:
                tabela = comando()

                if 'comando' in tabela:
                    self.cursor.execute("SELECT * FROM comando")
                    tabela = "comando"
                    break

                elif 'dicionario' in tabela:
                    self.cursor.execute("SELECT * FROM dicionario")
                    tabela = "dicionario"
                    break

                elif 'aplicativo' in tabela:
                    self.cursor.execute("SELECT * FROM aplicativo")
                    tabela = "aplicativo"
                    break

                else:
                    print("Nao entendi, poderia repetir qual tabela deseja vizualizar ?")


            cats = self.cursor.fetchall()

            for cat in cats:
                print(f"each {tabela} : {cat}")


#Podem Retirar as # para realizarem consultas nas tabelas sendo elas (COMANDO tabela 1, APLICATIVO tabela 3 e DICIONARIO tabale 2) use numerico de 1 a 3 para selecionar

if __name__ == '__main__':
    banco_de_dados = ConnectBancoDados()
#   banco_de_dados.showdonw()