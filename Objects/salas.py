class Salas():
    def __init__(self, cine, num_sala, asiento):
        self.cine = cine
        self.num_sala = num_sala
        self.asiento = asiento

    def imprimir(self):
        print(f"Cine: {self.cine}, Numero de sala: {self.num_sala}, Asiento: {self.asiento}")
        