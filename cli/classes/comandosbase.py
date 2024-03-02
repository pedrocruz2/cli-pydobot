import inquirer
from classes.robo import Robo
class Comandos():
    def __init__(self,port): 
        self.port = port
        self.robo = Robo(self.port)
    def mainmenu(self):
        perguntas = [inquirer.List(
        name="escolha", 
        message="Qual comando deseja realizar?", 
        choices=[
            "home",
            "ligar ferramenta",
            "desligar ferramenta",
            "mover",
            "atual",
            "sair"
        ]
        )]
        respostas = inquirer.prompt(perguntas)
        return self.processar(respostas)
    
    def processar(self, resposta):
        escolha = resposta["escolha"]
        match(escolha):
            case "home":
                self.robo.home()
                return self.mainmenu()
            case "ligar ferramenta":
                self.robo.sugar(True)
                return self.mainmenu()
            case "desligar ferramenta":
                self.robo.sugar(False)
                return self.mainmenu()
            case "mover":
                self.robo.mover()
                return self.mainmenu()
            case "atual":
                self.robo.atual()
                return self.mainmenu()
            case "sair":
                print("Fechando aplicação")
    
    