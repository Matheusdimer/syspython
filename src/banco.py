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

    def update(self, tabela, registro, campo_valores):
        upd = f"UPDATE {tabela} SET "
        for campo in campo_valores:
            upd += f"{campo[0]} = '{campo[1]}'"
            if not campo[0] == campo_valores[-1][0]:
                upd += ", "
        
        upd += f" WHERE CODIGO = {registro}"
        try:
            self.c.execute(upd)
            self.conn.commit()
            return True
        except:
            return False

    def delete(self, tabela, registro):
        delet = f"DELETE FROM {tabela} WHERE CODIGO = {registro}"
        try:
            self.c.execute(delet)
            self.conn.commit()
            return True
        except:
            return False
        
