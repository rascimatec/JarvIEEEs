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
#    retorno = banco_de_dados.consulta("Paige abra o trello porfavor")
#    print(retorno)
#
#   SEMPRE QUE FOREM FAZER UMA CONSULTA SERA NESCESSARIO ESSE IF
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
            x = x.split() #se para por palavra em uma lista
            y = len(x) #conta os elementos da lista
            n = 0 # variável auxiliar do while (linha 53)

            while(n != y): # percorre todos os elementos da lista e comparando com o banco de dados


                self.cursor.execute(
                    f"SELECT caminho FROM comando JOIN aplicativo ON comando.id_comando = aplicativo.id_comando WHERE comando.comando = '{x[n]}' AND aplicativo.aplicativo = '{x[n + 2]}' AND aplicativo.artigo = '{x[n + 1]}'")
                rows = self.cursor.fetchall()
            
                #Select é o comando em sql para realizar consultas
                #O mesmo esta consultando a açao e o comando e retornando o caminho/parametro

                for row in rows:
                    retorno = row[0]
                    return(retorno)

                n = n + 1
                    #For apenas para selecionar e armazenar o retorno do banco

        except:     #Existe apenas para evitar erros e travamentos no codigo
            print("Nada foi encontrado em meu banco de dados")



    def showdonw (self): #exibe a tabela do banco de dados


        while True: #Nao ira permanecer estou usando apenas por enquanto pois minha conexao com o banco é lenta devido a internet
                    
            tabela = int(input("Qual tabela deseja exibir ? :"))

            if tabela == 1:
                self.cursor.execute("SELECT * FROM comando")
                tabela = "comando"
                break

            elif tabela == 2:
                self.cursor.execute("SELECT * FROM dicionario")
                tabela = "dicionario"
                break

            elif tabela == 3:
                self.cursor.execute("SELECT * FROM aplicativo")
                tabela = "aplicativo"
                break
            else:
                print("Tabela invalida, use numerico de 1 a 3")

        cats = self.cursor.fetchall()

        for cat in cats:
            print(f"each {tabela} : {cat}")



