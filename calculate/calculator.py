# Simulador de dados.
import random
import PySimpleGUI as sg


class SimulateTheDice:
    def __init__(self):
        self.min_value = 1

        self.filename = sg.popup_get_file(
            'Enter the file you wish to process'),
        self.layout_cardapio = [
            [sg.popup('You entered', self.filename)]
        ]

    def Iniciar(self):

        # criação da janela
        self.janela = sg.Window('Simulador de Dados',
                                layout=self.layout_cardapio)

        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()

        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.LayoutCardapio()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print("Por favor, digite sim ou não!")
        except:
            print("Ocorreu um erro ao receber sua resposta")


simulate = SimulateTheDice()
simulate.Iniciar()
