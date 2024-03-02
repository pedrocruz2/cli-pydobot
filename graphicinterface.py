import flet as ft
from cli.classes.robo import Robo 
from serial.tools import list_ports

def command_handler(command,page: ft.Page):
    match command:
        case "home":
            # Lógica para enviar o robô para a posição inicial
            print("Enviando robô para a posição inicial")
        case "ligar ferramenta":
            # Lógica para ligar a ferramenta
            print("Ferramenta ligada")
        case "desligar ferramenta":
            # Lógica para desligar a ferramenta
            print("Ferramenta desligada")
        case "mover":
            # Lógica para mover o robô (você pode adicionar parâmetros adicionais conforme necessário)
            print("Movendo o robô")
        case "atual":
            # Lógica para obter a posição atual do robô
            print("Obtendo posição atual do robô")
        case "sair":
            # Lógica para fechar a aplicação
            print("Fechando aplicação")
        case _:
            print("Comando não reconhecido")
def main(page: ft.Page):
    page.title = "Controle do Robô PyDobot"
    page.vertical_alignment = ft.MainAxisAlignment.START
    def on_port_selected(e):
        global porta_escolhida
        porta_escolhida = e.control.value
        print(f"Porta escolhida: {porta_escolhida}")
    available_ports = list_ports.comports()
    port_options = [ft.dropdown.Option(port.device, port.device) for port in available_ports]

    # Criação do menu dropdown para seleção de portas
    port_dropdown = ft.Dropdown(
        label="Escolha a porta serial",
        options=port_options,
        on_change=on_port_selected
    )
    dropdown = ft.Dropdown(
        label="Selecione um comando",
        options=[
            ft.dropdown.Option("home", "Home"),
            ft.dropdown.Option("ligar ferramenta", "Ligar Ferramenta"),
            ft.dropdown.Option("desligar ferramenta", "Desligar Ferramenta"),
            ft.dropdown.Option("mover", "Mover"),
            ft.dropdown.Option("atual", "Atual"),
            ft.dropdown.Option("sair", "Sair")
        ],
        on_change=lambda e: command_handler(e.control.value,page),
    )
    page.add(port_dropdown)
    page.add(dropdown)
    

if __name__ == "__main__":
    ft.app(target=main)
