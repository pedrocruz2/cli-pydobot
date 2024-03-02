from serial.tools import list_ports
import inquirer
import typer
from classes.comandosbase import Comandos
# Cria uma instância da aplicação
app = typer.Typer()
# Estado da ferramenta
def startup():
    global porta_escolhida
    available_ports = list_ports.comports()
    porta_escolhida = inquirer.prompt([
    inquirer.List("porta",
                message="Escolha a porta serial",
                choices=[x.device for x in available_ports])
    ])["porta"]
startup()
# Cria um quarto comando do CLI
@app.command()
def inicio():
    modo = Comandos(porta_escolhida)
    print(f"Porta escolhida: {porta_escolhida}")
    modo.mainmenu()
    # realiza lista de perguntas para o usuário
if __name__ == "__main__":
    app()