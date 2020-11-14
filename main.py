from business.estoque_business import EstoqueBusiness
from modelDTO.item import ItemDTO

if __name__ == "__main__":
    item = ItemDTO("abroba", 3000, "aaaaa")
    estoque_business = EstoqueBusiness()
    estoque_business.obter_todo_estoque()
    #estoque_business.adicionar_item(item)
    estoque_business.obter_todo_estoque()
    print(estoque_business.recuperar_itens_por_nome("abroba"))
    print(estoque_business.retirar_do_estoque_por_nome("abroba"))