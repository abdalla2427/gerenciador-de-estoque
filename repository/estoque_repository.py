from model.item import Item
from typing import List
import sqlite3

class EstoqueRepository:

    def adicionar_item(self, item: Item) -> bool:
        try:
            conn = sqlite3.connect('./banco.db')
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO estoque (nome, preco, descricao, data_inclusao)
            VALUES (?, ?, ?, ?)
            """, (item.nome, item.preco,item.descricao, item.data_inclusao))
            conn.commit()
            conn.close()
        
        except Exception as err:
            print(err)
            return False

        return True

    def recuperar_itens_por_nome(self, nome: str):
        conn = sqlite3.connect('./banco.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT * 
        FROM estoque
        WHERE nome = '{nome}';
        """)

        resultados_cursor = cursor.fetchall()
        conn.close()
        return resultados_cursor

    def obter_todo_estoque(self):
        conn = sqlite3.connect('./banco.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM estoque;
        """)

        resultados_cursor = cursor.fetchall()
        conn.close()
        return resultados_cursor
    
    def retirar_do_estoque_por_nome(self, nome: str) -> bool:
        try:
            conn = sqlite3.connect('./banco.db')
            cursor = conn.cursor()
            cursor.execute(f"""
            UPDATE estoque
            SET item_excluido = 1
            WHERE id = (
                SELECT id
                FROM estoque 
                WHERE nome='{nome}'
                AND item_excluido = NULL
                LIMIT 1)
            """)
            conn.commit()
            conn.close()
    
        except Exception as err:
            print(err)
            return False

        return True