import psycopg2

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

        while True:

            tabela = int("Qual tabela deseja modificar ? :")

            if tabela == 1: #tabela aplicativo
                record = input(int("Digite qual comando deseja atribuir :"))
                if(record == 'abrir' or record == 'abra'):
                    record = 1
                elif (record == 'desligar' or record == 'desligue'):
                    record = 2
                elif(record == 'fechar' or record == 'feche'):
                    record = 3
                elif(record == 'pesquise' or record == 'pesquisa'):
                    record = 4

                record1 = input("Digite o nome do aplicativo :")
                record2 = input("Digite o caminho do aplicativo :")
                insert_command = "INSERT INTO aplicativo(id_comando, aplicativo, caminho) VALUES('" + record + "','" + record1 + "','" + record2 + "') "
                break

            elif tabela == 2:#tabela comando
                record = input("Digite o comando desejado :")
                record1 = input("Digite a ação desejada :")
                insert_command = "INSERT INTO comando(comando, acao) VALUES('" + record + "','" + record1 + "')"
                break

            elif tabela == 3: #tabela dicionario
                record = input("Dicionario aberto digite:")
                record1 = input("Dicionario ainda aberto:")
                record2 = input("Dicionario ultima fechando:")
                insert_command = "INSERT INTO dicionario(palavra, sinonimo, sinonimo_2) VALUES('" + record + "','" + record1 + "','" + record2 + "')"
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")
        self.cursor.execute(insert_command) #execuçao do comando em SQL


    def consulta (self, msg): #funçao de consulta com o banco de dados

        try:
            x = msg.strip() #strip vai tirar espaço desnecessário (a mais)
            x = x.lower() #deixa toda string minuscula
            x = x.split() #separa a string por palavra em uma lista
            y = len(x) #conta os elementos da lista
            n = 0 # variável auxiliar do while

            while(n != y): # percorre todos os elementos da lista e comparando com o banco de dados


                self.cursor.execute(
                    f"SELECT caminho FROM comando JOIN aplicativo ON comando.id_comando = aplicativo.id_comando JOIN dicionario ON aplicativo.id_dicionario = dicionario.id_dicionario WHERE comando.comando = '{x[n]}' AND aplicativo.aplicativo = '{x[n + 2]}' AND aplicativo.artigo ='{x[n + 1]}' OR dicionario.sinonimo = '{x[n]}' AND aplicativo.artigo = '{x[n + 1]}' AND aplicativo.aplicativo = '{x[n + 2]}'")
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
            print("o")

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


        while True: #Nao ira permanecer estou usando apenas por enquanto pois minha conexao com o banco é lenta devido a internet
                    
            tabela = int(input("Qual tabela deseja exibir ? :"))

            if tabela == 1:
                self.cursor.execute("SELECT * FROM comando")
                tabela = "comando"

            elif tabela == 2:
                self.cursor.execute("SELECT * FROM dicionario")
                tabela = "dicionario"

            elif tabela == 3:
                self.cursor.execute("SELECT * FROM aplicativo")
                tabela = "aplicativo"

            else:
                print("Tabela invalida, use numerico de 1 a 3")

            cats = self.cursor.fetchall()

            for cat in cats:
                print(f"each {tabela} : {cat}")

            c = int(input('\ndeseja vizualizar outra tabela (1-sim/2-nao) ? :\n'))
            if c == 2:
                break

#Podem Retirar as # para realizarem consultas nas tabelas sendo elas (COMANDO tabela 1, APLICATIVO tabela 2 e DICIONARIO tabale 3) use numerico de 1 a 3 para selecionar

if __name__ == '__main__':
    banco_de_dados = ConnectBancoDados()
    banco_de_dados.showdonw()