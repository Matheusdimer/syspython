import sqlite3 as sql


class Banco:
    def __init__(self, banco):
        self.conn = sql.connect(banco)
        self.c = self.conn.cursor()

    def cadastro(self, table, dados):
        try:
            querry = f"INSERT INTO {table} VALUES("
            cont = 1
            for valor in dados:
                if len(valor) == 0:
                    return False
                querry += f"'{valor}'"
                if cont != len(dados):
                    querry += ", "
                    cont += 1
            querry += ")"
            self.c.execute(querry)
            self.conn.commit()
            return True
        except:
            return False
        

    def consulta(self, tabela, campo="", pesquisa=""):
        if pesquisa == "" and campo == "":
            querry = "SELECT * FROM {}".format(tabela)
            result = self.c.execute(querry)
        else:
            querry = "SELECT * FROM {} WHERE {} LIKE '%{}%'".format(tabela, campo, pesquisa)
            result = self.c.execute(querry)
        self.conn.commit()
        return result.fetchall()
