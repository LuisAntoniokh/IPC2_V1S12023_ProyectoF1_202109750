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

    def delete(self, data):
        # Check if list is empty
        if self.cabeza is None:
            return

        # If the node to delete is the head node
        if self.cabeza.data == data:
            self.cabeza = self.cabeza.next
            return

        # Find the node to delete
        actual = self.cabeza
        while actual.next is not None:
            if actual.next.data == data:
                break
            actual = actual.next

        # If node was not found
        if actual.next is None:
            return

        # Unlink the node from linked list
        actual.next = actual.next.next

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
            elif operacion == 3:
                self.delete(objeto)

    def agregarXML(self, Nombre, Apellido, Telefono, Email, Password):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')
        root = tree.getroot()

        nuevo_cliente = ET.Element("usuario")

        rol = ET.SubElement(nuevo_cliente, 'rol')
        rol.text = 'Cliente'

        nombre = ET.SubElement(nuevo_cliente, 'nombre')
        nombre.text = Nombre

        apellido = ET.SubElement(nuevo_cliente, 'apellido')
        apellido.text = Apellido

        telefono = ET.SubElement(nuevo_cliente, 'telefono')
        telefono.text = Telefono

        correo = ET.SubElement(nuevo_cliente, 'correo')
        correo.text = Email

        contraseña = ET.SubElement(nuevo_cliente, 'contrasena')
        contraseña.text = Password

        objeto = Usuario(rol, nombre, apellido, telefono, correo, contraseña)
        self.add(objeto)

        root.append(nuevo_cliente)

        tree.write('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')

    def editarXML(self, new_rol, new_nombre, new_apellido, new_telefono, tmp_correo, new_contrasena):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')
        root = tree.getroot()

        for user in root.findall('usuario'):
            if user.find('correo').text == tmp_correo:
                rol = user.find('rol')
                rol.text = new_rol
                nombre = user.find('nombre')
                nombre.text = new_nombre
                apellido = user.find('apellido')
                apellido.text = new_apellido
                telefono = user.find('telefono')
                telefono.text = new_telefono
                correo = user.find('correo')
                correo.text = tmp_correo
                contrasena = user.find('contrasena')
                contrasena.text = new_contrasena
                break

        tree.write('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')

        self.CargarXML(2)

    def eliminarXML(self, tmp_correo):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')
        root = tree.getroot()

        for user in root.findall('usuario'):
            if user.find('correo').text == tmp_correo:
                root.remove(user)
                break

        tree.write('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/usuarios.xml')

        self.CargarXML(3)