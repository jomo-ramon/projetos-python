# Simulador de dados.
import random
import PySimpleGUI as sg


class SimulateTheDice:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para  o dado?'

        # Layout
        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):

        # criação da janela
        self.janela = sg.Window('Simulador de Dados', layout=self.layout)

        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()

        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.ValueDice()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print("Por favor, digite sim ou não!")
        except:
            print("Occorou um erro ao receber sua resposta")

    def ValueDice(self):
        print(random.randint(self.min_value, self.max_value))


simulate = SimulateTheDice()
simulate.Iniciar()
