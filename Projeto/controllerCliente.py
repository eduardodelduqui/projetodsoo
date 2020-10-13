from cliente import Cliente

class ControllerCliente:
    def __init__(self):
        self.__clientes: []

    
    @property
    def clientes(self):
        return self.__clientes

    def adiciona_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and cliente not in self.__clientes:
            self.__clientes.append(cliente)


    def remove_cliente(self, cliente: Cliente):
        self.__clientes.remove(cliente)