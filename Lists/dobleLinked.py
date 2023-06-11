from Nodes.NodoDoble import NodoDoble
from Objects.pelis import Pelicula
import xml.etree.ElementTree as ET

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def add(self, data):
        nuevo_nodo = NodoDoble(data)
        if self.cabeza is None:
            nuevo_nodo.next = nuevo_nodo
            nuevo_nodo.back = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.back
            nuevo_nodo.next = self.cabeza
            nuevo_nodo.back = ultimo
            self.cabeza.back = nuevo_nodo
            ultimo.next = nuevo_nodo

    
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

    def CargarXML_LDC(self):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/peliculas.xml')
        root = tree.getroot()

        for indice, personas in enumerate(root.findall('persona')):
            codigo = personas.find('codigo').text
            nombre = personas.find('nombre').text
            edad = personas.find('edad').text
            encargado = personas.find('encargado').text
            raza = personas.find('raza').text

            objeto = Pelicula(codigo, nombre, edad, encargado, raza)
            self.add(objeto)