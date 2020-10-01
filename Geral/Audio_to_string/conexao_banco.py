import psycopg2 


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
        #tabela 2 = comando, tabela 3 = dicionario

        while True:

            tabela = int(input("Qual tabela deseja modificar ? :"))

            if tabela == 1: #tabela aplicativo
                record = input(int("Digite qual comando deseja atribuir :"))
                record1 = input("Digite o nome do aplicativo :")
                record2 = input("Digite o caminho do aplicativo :")
                insert_command = "INSERT INTO aplicativo(id_comando, aplicativo, caminho) VALUES('" + record + "','" + record1 + "','" + record2 + "') "

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
        x = msg.strip() #strip vai tirar espaço desnecessário (a mais)
        x = x.lower() #deixa toda string minuscula
        x = x.split() #se para por palavra em uma lista
        y = len(x) #conta os elementos da lista
        n = 0 # variável auxiliar do while (linha 53)

        while(n != y): # percorre todos os elementos da lista e comparando com o banco de dados


            self.cursor.execute(
                f"SELECT caminho FROM comando JOIN aplicativo ON comando.id_comando = aplicativo.id_comando WHERE comando.comando = '{x[n]}' AND aplicativo.aplicativo = '{x[n + 1]}'")
            rows = self.cursor.fetchall()
            
            #Select é o comando em sql para realizar consultas 
            #O mesmo esta consultando a açao e o comando e retornando o caminho/parametro

            for row in rows:
                retorno = row[0]
                return(retorno)
            
            #For apenas para selecionar e armazenar o retorno do banco

            n = n + 1

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


if __name__ == '__main__': #é a conexão com o banco.
    banco_de_dados = ConnectBancoDados() #inicio da conexao  
    retorno = banco_de_dados.consulta("Paige abra facebook porfavor")
    print(retorno)
