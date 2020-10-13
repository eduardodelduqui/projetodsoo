from loja import Loja

class ControllerLoja:
    def __init__(self):
        self.__lojas = []
    

    @property
    def lojas(self):
        return self.__lojas

    def adiciona_loja(self, loja: Loja):
        if isinstance(loja, Loja) and loja not in self.__lojas:
            self.__lojas.append(loja)

    def remove_loja(self, loja: Loja):
        self.__lojas.remove(loja)
