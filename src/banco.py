import sqlite3 as sql


class Banco:
    def __init__(self, banco):
        self.conn = sql.connect(banco)
        self.c = self.conn.cursor()

    def cadastro(self, table, dados):
        try:
            query = f"INSERT INTO {table} VALUES("
            cont = 1
            for valor in dados:
                if len(valor) == 0:
                    return False
                query += f"'{valor}'"
                if cont != len(dados):
                    query += ", "
                    cont += 1
            query += ")"
            self.c.execute(query)
            self.conn.commit()
            return True
        except:
            return False
        

    def consulta(self, tabela, campo=None, pesquisa=None):
        if pesquisa and campo:
            if campo == "CODIGO":
                query = f"SELECT * FROM {tabela} WHERE CODIGO = {pesquisa}"
            else:
                query = "SELECT * FROM {} WHERE {} LIKE '%{}%'".format(tabela, campo, pesquisa)
        else:
            query = "SELECT * FROM {}".format(tabela)
        
        result = self.c.execute(query)
        self.conn.commit()
        return result.fetchall()
