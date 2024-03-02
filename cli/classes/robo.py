import pydobot

class Robo: 
    def __init__(self,port: str) -> None:
        self.port = port
        self.robo = pydobot.Dobot(port=port, verbose=False)
        self.posicaohome = self.robo.pose()
    def home(self):
        (x, y, z, r, j1, j2, j3, j4) = self.posicaohome
        self.robo.move_to(x=x,y=y,z=z,r=r)
    def mover(self):
        direcao = input("Digite a direção que deseja mover: ").upper()
        distancia = float(input("Digite a distância que deseja mover: "))
        (x, y, z, r, j1, j2, j3, j4) = self.robo.pose()
        match(direcao):
            case "X":
                self.robo.move_to(x=x + distancia, y=y,z=z,r=r)
            case "Y":
                self.robo.move_to(x=x,y=y+ distancia,z=z,r=r)
            case "Z":
                self.robo.move_to(x=x,y=y,z=z+distancia,r=r)
            case _:
                print('Forneça uma direção válida, como "x", "y" ou "z"')
                return self.mover()
    def sugar(self,x: bool):
        self.robo.suck(x)
    def atual(self):
        (x, y, z, r, j1, j2, j3, j4) = self.robo.pose()
        print(f'Posição atual: x={x}, y={y}, z={z}')
        