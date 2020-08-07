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

            if tabela == 2:
                record = input("Digite o comando desejado :")
                insert_command = "INSERT INTO comando(comando) VALUES('" + record + "')"
                break

            elif tabela == 3:
                record = input("Dicionario aberto digite:")
                record1 = input("Dicionario ainda aberto:")
                record2 = input("Dicionario ultima fechando:")
                insert_command = "INSERT INTO dicionario(palavra, sinonimo, antonimo) VALUES('" + record + "','" + record1 + "','" + record2 + "')"
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")
            
        self.cursor.execute(insert_command)
    

    def update_record (self):
        while True:

            tabela = int(input("Qual tabela deseja modificar ? :"))

            if tabela == 2:
                i = int(input("Digite o ID do item desejado :"))
                mod = input("Digite o novo texto :")
                update_command = (f"UPDATE comando SET comando={mod} WHERE id_comando={i}")            
                break

            elif tabela == 3:
                i = int(input("Digite o ID do item desejado :"))
                campo = input("Qual campo da tabela deseja alterar :")
                mod = input("Digite o novo texto :")
                update_command = (f"UPDATE dicionario SET {campo}={mod} WHERE id_dicionario={i}")            
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")

        self.cursor.execute(update_command)            

    def consulta (self):
        #é nescessario que antes da chamada dessa funçao ja se tenha dado um comando ao assistente
        #fala é apenas a variavel que iremos consultar no banco 

        self.cursor.execute(f"SELECT comando FROM comando WHERE comando='{fala}'")
        rows = self.cursor.fetchall()

        for row in rows:
            retorno = row[0]
        print(retorno)        

    def showdonw (self):

        while True:

            tabela = int(input("Qual tabela deseja exibir ? :"))

            if tabela == 2:
                self.cursor.execute("SELECT * FROM comando")
                tabela = "comando"
                break

            elif tabela == 3:
                self.cursor.execute("SELECT * FROM dicionario")
                tabela = "dicionario"
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")

            cats = self.cursor.fetchall()

        for cat in cats:
            print(f"each {tabela} : {cat}")
    
if __name__ == '__main__':
    banco_de_dados = ConnectBancoDados()
    #banco_de_dados.showdonw()
    #banco_de_dados.update_record()
    #banco_de_dados.insert_record()
    banco_de_dados.consulta()