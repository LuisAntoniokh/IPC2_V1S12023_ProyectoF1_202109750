class Salas():
    def __init__(self, sala, numero, asiento):
        self.sala = sala
        self.numero = numero
        self.asiento = asiento

    def imprimir(self):
        print(f"Sala: {self.sala}, Numero: {self.numero}, Asiento: {self.asiento}")
        