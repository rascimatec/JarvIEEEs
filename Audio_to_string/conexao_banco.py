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
        #tabela 2 = comando, tabela 3 = dicionario

        while True:

            tabela = int(input("Qual tabela deseja modificar ? :"))

            if tabela == 1:
                record = input(int("Digite qual comando deseja atribuir :"))
                record1 = input("Digite o nome do aplicativo :")
                record2 = input("Digite o caminho do aplicativo :")
                insert_command = "INSERT INTO aplicativo(id_comando, aplicativo, caminho) VALUES('" + record +"','" + record1 + "','" + record2 + "') "

            elif tabela == 2:
                record = input("Digite o comando desejado :")
                record1 = input("Digite a ação desejada :")
                insert_command = "INSERT INTO comando(comando, acao) VALUES('" + record + "','" + record1 + "')"
                break

            elif tabela == 3:
                record = input("Dicionario aberto digite:")
                record1 = input("Dicionario ainda aberto:")
                record2 = input("Dicionario ultima fechando:")
                insert_command = "INSERT INTO dicionario(palavra, sinonimo, sinonimo_2) VALUES('" + record + "','" + record1 + "','" + record2 + "')"
                break

            else:
                print("Tabela invalida, use numerico de 1 a 3")
            
        self.cursor.execute(insert_command)
    
    def consulta (self, msg):

        x = msg.strip()
        x = x.lower()
        x = x.split()
        y = len(x)
        n = 0

        while(n != y):

            self.cursor.execute(f"SELECT caminho FROM comando JOIN aplicativo ON comando.id_comando = aplicativo.id_comando WHERE comando.comando = '{x[n]}' AND aplicativo.aplicativo = '{x[n+1]}'")
            rows = self.cursor.fetchall()

            for row in rows:
                retorno = row[0]
                return(retorno)

            n = n + 1

    def showdonw (self):

        while True:

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
    
if __name__ == '__main__':
    banco_de_dados = ConnectBancoDados()
    retorno = banco_de_dados.consulta("Paige abra facebook porfavor")
    banco_de_dados.connection.close()
    print(retorno)