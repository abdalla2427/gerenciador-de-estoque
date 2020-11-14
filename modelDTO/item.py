from datetime import date

class ItemDTO:
    def __init__(self, nome: str, preco: float, descricao: str):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.data_inclusao = date.today()
