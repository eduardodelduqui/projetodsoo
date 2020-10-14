from controle.controller_loja import ControllerLoja

class TelaLoja:

    def __init__(self, controlador: ControllerLoja):
        self.__controlador = controlador



    def mostra_tela_opcoes(self):
        print("*-------------- Cadastro de Lojas --------------")
        print('1 - Adicionar')
        print('2 - Remover')
        print('3 - Listar')
        print('0 - Voltar')
        opcao = input('Escolha a Opção: ')
        # Precisa incluir
        return opcao

