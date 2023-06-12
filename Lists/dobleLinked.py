from Nodes.NodoDoble import NodoDoble
from Objects.salas import Salas
import xml.etree.ElementTree as ET

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.charged = False

    def esta_vacia(self):
        return self.cabeza is None

    def add(self, data):
        nuevo_nodo = NodoDoble(data)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nuevo_nodo
            nuevo_nodo.back = nodo_actual

    def mostrar(self):
        current = self.cabeza
        while current is not None:
            print(f"Cine: {current.data.cine}, Numero de sala: {current.data.num_sala}, Asiento: {current.data.asiento}")
            current = current.next

    def delete(self, data):
        if self.esta_vacia():
            return

        if self.cabeza.data == data:
            if self.cabeza.next is None:
                self.cabeza = None
            else:
                self.cabeza = self.cabeza.next
                self.cabeza.back = None
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.data == data:
                nodo_anterior = nodo_actual.back
                nodo_siguiente = nodo_actual.next
                nodo_anterior.next = nodo_siguiente
                if nodo_siguiente is not None:
                    nodo_siguiente.back = nodo_anterior
                return
            nodo_actual = nodo_actual.next

    def modify(self, data_vieja, data_nueva):
        if self.esta_vacia():
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.data.num_sala  == data_vieja: 
                nodo_actual.data.asiento = data_nueva
                return
            nodo_actual = nodo_actual.next

    def buscar(self, elemento):
        actual = self.cabeza

        while actual is not None:
            if actual.data == elemento:
                return True
            actual = actual.next

        return False

    def CargarXML_LED(self, operacion):
        if self.charged:
            return  # Si los datos ya han sido cargados, no se cargan de nuevo

        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')
        root = tree.getroot()

        numeros_sala_cargados = ListaDobleEnlazada()  # Lista para almacenar los números de sala cargados

        for cine in root.findall('cine'):
            nombre_cine = cine.find('nombre').text
            salas_cine = cine.find('salas')

            for indice, sala in enumerate(salas_cine.findall('sala')):
                numero_sala = sala.find('numero').text
                asientos_sala = sala.find('asientos').text

                # Verificar si el número de sala ya ha sido cargado
                #if numeros_sala_cargados.buscar(numero_sala):
                    #continue  # Omitir la sala si ya ha sido cargada

                objeto = Salas(nombre_cine, numero_sala, asientos_sala)

                if operacion == 1:
                    self.add(objeto)
                elif operacion == 2:
                    self.modify(numero_sala, asientos_sala)
                elif operacion == 3:
                    self.delete(objeto)

                numeros_sala_cargados.add(numero_sala)  # Agregar el número de sala a la lista enlazada doble

        self.charged = True

    def agregarXML_LED(self, Asientos):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')
        root = tree.getroot()

        nuevo_sala = ET.Element("sala")

        index = 3
        titulo_existe = False

        nodo_actual = self.cabeza

        while nodo_actual is not None:
            if nodo_actual.data.num_sala.startswith('#USACIPC2_202212333_'):
                titulo_existe = True
                break
            nodo_actual = nodo_actual.next

        while titulo_existe:
            index += 1
            titulo_existe = False
            nodo_actual = self.cabeza

            while nodo_actual is not None:
                if nodo_actual.data.num_sala == '#USACIPC2_202212333_' + str(index):
                    titulo_existe = True
                    break
                nodo_actual = nodo_actual.next

        titulo = '#USACIPC2_202212333_' + str(index)

        elemento_titulo = ET.SubElement(nuevo_sala, 'numero')
        elemento_titulo.text = titulo

        asientos = ET.SubElement(nuevo_sala, 'asientos')
        asientos.text = str(Asientos)

        objeto = Salas('Cine ABC', titulo, asientos.text)
        self.add(objeto)

        cine = root.find('cine')
        salas = cine.find('salas')
        salas.append(nuevo_sala)

        tree.write('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')

        self.CargarXML_LED(1)

    def editarXML_LED(self, numero_sala, nuevos_asientos):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')
        root = tree.getroot()

        for cine in root.findall('cine'):
            salas_cine = cine.find('salas')

            for sala in salas_cine.findall('sala'):
                numero_sala_element = sala.find('numero')
                asientos_sala_element = sala.find('asientos')

                if numero_sala_element is not None and numero_sala_element.text == numero_sala:
                    if asientos_sala_element is not None:
                        asientos_sala_element.text = str(nuevos_asientos)
                    break

        tree.write('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')

        self.CargarXML_LED(2)

    def eliminar_LED(self, titulo):
        tree = ET.parse('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')
        root = tree.getroot()

        for cine in root.findall('cine'):
            for sala in cine.findall('salas/sala'):
                if sala.find('numero').text == titulo:
                    cine.find('salas').remove(sala)
                    self.delete(Salas(cine.find('nombre').text, titulo, sala.find('asientos').text))
                    break

        tree.write('C:/Users/User/Documents/USAC/Vaqueras V Semestre/Lab/IPC2_V1S12023_ProyectoF1_202109750/Test/salas.xml')

        self.CargarXML_LED(3)