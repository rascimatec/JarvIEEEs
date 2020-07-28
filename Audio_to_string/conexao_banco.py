import psycopg2

class ConnectBancoDados:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='upsaude19' user='upsaude19' host='pgsql.upsaude.net.br' password='080901' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
                print("Nao foi possivel conectar ao banco de dados")

    def insert_record (self):
        #tabela 1 = acao , tabela 2 = comando, tabela 3 = dicionario

        while True:

            tabela = int(input("Qual tabela deseja modificar ? :"))

            if  tabela == 1:
                record = input("Digite a ação desejada :")
                insert_command = "INSERT INTO acao(acoes) VALUES('" + record[0] + "')"
                break

            elif tabela == 2:
                record = input("Digite o comando desejado :")
                insert_command = "INSERT INTO comando(comando) VALUES('" + record[0] + "')"
                break

            elif tabela == 3:
                record = input("Dicionario aberto digite:")
                insert_command = "INSERT INTO dicionario(palavras, sinonimos) VALUES('" + record[0] + "','" + record[1] + "')"
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")
            
        self.cursor.execute(insert_command)
    

    def update_record (self):
        while True:

            tabela = int(input("Qual tabela deseja modificar ? :"))

            if tabela == 1:
                mod = input("Digite o novo texto :")
                i = int(input("Digite o ID do item desejado"))
                update_command = (f"UPDATE acao SET acoes={mod} WHERE id_acoa={i}")            
                break

            elif tabela == 2:
                mod = input("Digite o novo texto :")
                i = int(input("Digite o ID do item desejado"))
                update_command = (f"UPDATE comando SET comando={mod} WHERE id_comando={i}")            
                break

            elif tabela == 3:
                campo = input("Qual campo da tabela deseja alterar")
                mod = input("Digite o novo texto :")
                i = int(input("Digite o ID do item desejado"))
                update_command = (f"UPDATE dicionario SET {campo}={mod} WHERE id_dicionario={i}")            
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")

        self.cursor.execute(update_command)            


    def showdonw (self):

        while True:

            tabela = int(input("Qual tabela deseja exibir ? :"))

            if tabela == 1:
                self.cursor.execute("SELECT * FROM acao")
                cats = self.cursor.fetchall()
                tabela = "acao"
                break

            elif tabela == 2:
                self.cursor.execute("SELECT * FROM comando")
                cats = self.cursor.fetchall()
                tabela = "comando"
                break

            elif tabela == 3:
                self.cursor.execute("SELECT * FROM dicionario")
                cats = self.cursor.fetchall()
                tabela = "dicionario"
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")

        for cat in cats:
            print(f"each {tabela} : {cat}")
    
if __name__ == '__main__':
    banco_de_dados = ConnectBancoDados()
    