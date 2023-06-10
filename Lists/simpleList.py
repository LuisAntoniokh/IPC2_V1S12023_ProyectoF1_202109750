from Nodes.NodoSimple import NodoSimple
from Objects.user import Usuario
import xml.etree.ElementTree as ET

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def add(self, data):        
        nuevo = NodoSimple(data)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo

    def modify(self, data_nuevo, index):
        actual = self.cabeza
        indice = 0

        while actual is not None:
            if indice == index:
                actual.data = data_nuevo
                return
            indice += 1
            actual = actual.next

    def Imprimir(self):
        actual = self.cabeza
        actual.data.imprimir()
        while actual.next is not None:
            actual = actual.next
            actual.data.imprimir()

    def CargarXML(self, operacion):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')
        root = tree.getroot()

        for indice, usuarios in enumerate(root.findall('usuario')):
            rol = usuarios.find('rol').text
            nombre = usuarios.find('nombre').text
            apellido = usuarios.find('apellido').text
            telefono = usuarios.find('telefono').text
            correo = usuarios.find('correo').text
            contraseña = usuarios.find('contrasena').text

            objeto = Usuario(rol, nombre, apellido, telefono, correo, contraseña)
            
            if operacion == 1: # agregar datas a lista
                self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)

            #print(f"codigo: {codigo} nombre: {nombre}")

    def editarXML(self):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')
        root = tree.getroot()

        nombre1 = root.find("persona[1]/nombre")
        nombre1.text = "Fido"

        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')
        
        self.CargarXML(2)