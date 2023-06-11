from Nodes.NodoDoble import NodoDoble
from Objects.pelis import Pelicula
import xml.etree.ElementTree as ET

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None
        self.elemento_cargado = set()

    def existe_pelicula_titulo(self, titulo):
        if self.cabeza is None:
            return False
        nodo_actual = self.cabeza
        while True:
            if nodo_actual.data.Titulo == titulo:
                return True
            nodo_actual = nodo_actual.next
            if nodo_actual == self.cabeza:
                break
            if nodo_actual == self.cabeza.next:
                break
        return False

    def add(self, data):
        titulo = data.Titulo
        if titulo not in self.elemento_cargado:
            nuevo_nodo = NodoDoble(data)
            if self.cabeza is None:
                nuevo_nodo.next = nuevo_nodo
                nuevo_nodo.back = nuevo_nodo
                self.cabeza = nuevo_nodo
            else:
                nodo_actual = self.cabeza
                while True:
                    if nodo_actual.data == data:
                        print("El dato ya se encuentra cargado en la lista")
                        return  # No se agrega el nodo duplicado
                    nodo_actual = nodo_actual.next
                    if nodo_actual == self.cabeza:
                        break
                ultimo = self.cabeza.back
                nuevo_nodo.next = self.cabeza
                nuevo_nodo.back = ultimo
                self.cabeza.back = nuevo_nodo
                ultimo.next = nuevo_nodo
            self.elemento_cargado.add(titulo)
            
    def modify(self, data_nuevo, index):
        if self.cabeza is None:
            return

        nodo_actual = self.cabeza
        indice = 0

        while True:
            if indice == index:
                nodo_actual.data = data_nuevo
                return

            nodo_actual = nodo_actual.next
            if nodo_actual == self.cabeza:
                break

            indice += 1

    def delete(self, correo):
        if self.cabeza is None:
            return

        if self.cabeza.data.correo == correo:
            if self.cabeza.next == self.cabeza:
                self.cabeza = None
            else:
                ultimo = self.cabeza.back
                self.cabeza = self.cabeza.next
                self.cabeza.back = ultimo
                ultimo.next = self.cabeza
            return

        nodo_actual = self.cabeza
        while True:
            if nodo_actual.next.data.correo == correo:
                nodo_siguiente = nodo_actual.next
                nodo_actual.next = nodo_siguiente.next
                nodo_siguiente.next.back = nodo_actual
                return

            nodo_actual = nodo_actual.next
            if nodo_actual == self.cabeza:
                break


    def Imprimir_LDC(self):
        if self.cabeza is None:
            print("La lista esta vacía")
        else:
            nodo_actual = self.cabeza
            while True:
                nodo_actual.data.imprimir()
                nodo_actual = nodo_actual.next
                if nodo_actual == self.cabeza:
                    break

    def CargarXML_LDC(self, operacion):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/peliculas.xml')
        root = tree.getroot()

        for categoria in root.findall("categoria"):
            categor = categoria.find('nombre').text
            pelicula = categoria.find('peliculas')

            for indice, peli in enumerate(pelicula.findall('pelicula')):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora = peli.find('hora').text

                objeto = Pelicula(categor, titulo, director, anio, fecha, hora)

                if not self.existe_pelicula_titulo(objeto):
                    if operacion == 1:
                        self.add(objeto)
                    elif operacion == 2:
                        self.modify(objeto, indice)
                    elif operacion == 3:
                        self.delete(objeto)
                else:
                    print(f"La película '{titulo}' ya está cargada en la lista.")
    