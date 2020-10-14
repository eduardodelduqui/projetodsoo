from categoria import Categoria
from loja import Loja
from cliente import Cliente
from produto import Produto
from datetime import datetime, date
import uuid

class Pedido:
    
    def __init__(self,loja: Loja,cliente: Cliente, produto: Produto):

        self.__codigo = uuid.uuid4().hex
        self.__produto = produto
        self.__loja = loja
        self.__cliente = cliente
        self.__data = date.today
        self.__horario = datetime.now().strftime("%H:%M:%S")
    
    def imprime(self):

        return dict(pedido = self.__codigo,
                    loja = self.__loja.nome,
                    cliente = self.__cliente.nome,
                    produto = self.__produto.nome,
                    data = self.__data,
                    horario = self.__horario)