class Usuario():
    def __init__(self, rol, nombre, apellido, telefono, correo, contraseña):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contraseña = contraseña

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Rol: {self.rol}, Telefono: {self.telefono}, Correo: {self.correo}, Contraseña: {self.contraseña}")
        