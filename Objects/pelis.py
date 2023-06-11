class Pelicula():
    def __init__(self, Categoria, Titulo, Director, Anio, Fecha, Hora):
        self.Categoria = Categoria
        self.Titulo = Titulo
        self.Director = Director
        self.Anio = Anio
        self.Fecha = Fecha
        self.Hora = Hora

    def imprimir(self):
        print(f"Categoria: {self.Categoria}, Titulo: {self.Titulo}, Director: {self.Director}, Año: {self.Anio}, Fecha: {self.Fecha}, Hora: {self.Hora}")
        