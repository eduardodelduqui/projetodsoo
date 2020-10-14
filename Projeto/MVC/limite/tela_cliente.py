from controle.controller_cliente import ControllerCliente

class TelaCliente:
    def __init__(self, controlador: ControllerCliente):
        self.__controlador = controlador



    def mostra_tela_opcoes(self):
        print("*-------------- Cadastro de Clientes --------------")
        print('1 - Adicionar')
        print('2 - Remover')
        print('3 - Listar')
        print('0 - Voltar')
        opcao = input('Escolha a Opção: ')
        # Precisa incluir
        return opcao

