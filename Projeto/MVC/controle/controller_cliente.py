from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControllerCliente:
    def __init__(self):
        self.__tela_cliente = TelaCliente(self)        
        self.__clientes: []


    def inicia(self):
        # self.abre_tela_inicial()
        pass

    def adiciona_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and cliente not in self.__clientes:
            self.__clientes.append(cliente)

    def remove_cliente(self, cliente: Cliente):
        self.__clientes.remove(cliente)

    def lista_cliente(self):
        return self.__clientes

    def finalizar(self):
        exit(0)

    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.lista_cliente}

        while True:
            opcao = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
