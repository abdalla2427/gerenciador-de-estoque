import sqlite3

conn = sqlite3.connect('./banco.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao, item_excluido)
VALUES ('Celular', '3500', 'celular brabo','10-10-2010', NULL)
""")

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao, item_excluido)
VALUES ('Cabide', '30', 'cabide','10-10-2010', NULL)
""")

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao, item_excluido)
VALUES ('Carro', '100000', 'barrin','10-10-2010', NULL)
""")

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao, item_excluido)
VALUES ('Batata', '2', 'batatinha','10-10-2010', NULL)
""")


conn.commit()

conn.close()