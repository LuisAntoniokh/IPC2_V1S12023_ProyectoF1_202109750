from colorama import Fore
from Lists.simpleList import ListaEnlazada
from Lists.dobleCircle import listaDobleCircular
from Lists.dobleLinked import ListaDobleEnlazada
import xml.etree.ElementTree as ET
from Objects.pelis import Pelicula

from Objects.user import Usuario

lenSimple = ListaEnlazada()
lenCircular = listaDobleCircular()
lenDoble = ListaDobleEnlazada()

def AgCat():
    print(Fore.LIGHTMAGENTA_EX + "\n===== Registro de categoría y película =====")
    Categoria = input(Fore.LIGHTMAGENTA_EX + "Ingrese la categoría: ")
    Titulo = input(Fore.LIGHTMAGENTA_EX + "Ingrese el título: ")
    Director = input(Fore.LIGHTMAGENTA_EX + "Ingrese el director: ")
    Anio = input(Fore.LIGHTMAGENTA_EX + "Ingrese el anio: ")
    Fecha = input(Fore.LIGHTMAGENTA_EX + "Ingrese la fecha: ")
    Hora = input(Fore.LIGHTMAGENTA_EX + "Ingrese la horas: ")

    def regresarMenuP():
        print(Fore.LIGHTMAGENTA_EX + "1. Registrar una nueva película")
        print(Fore.LIGHTMAGENTA_EX + "2. Regresar al menú de películas \n")
        tercerPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

        if tercerPaso == "1":
            AgCat()
        elif tercerPaso == "2":
            gesCat()
        else:
            print(Fore.RED+"Por favor, seleccione una opción válida")
            regresarMenuP()

    lenCircular.agregarXML_LDC(Categoria, Titulo, Director, Anio, Fecha, Hora)
    print(Fore.LIGHTMAGENTA_EX + "Se ha registrado una nueva función")
    print(Fore.LIGHTMAGENTA_EX + "================================= \n")
    regresarMenuP()
    
def modCat():
    print(Fore.BLUE + "\n===== Modificación de película =====")
    Titulo = input(Fore.BLUE + "Ingrese el título de la película a modificar: ")
    Director = input(Fore.BLUE + "Ingrese el nuevo director: ")
    Anio = input(Fore.BLUE + "Ingrese el nuevo año: ")
    Fecha = input(Fore.BLUE + "Ingrese la nueva fecha: ")
    Hora = input(Fore.BLUE + "Ingrese la nueva hora: ")

    lenCircular.editarXML_LDC(Titulo, Director, Anio, Fecha, Hora)

    print(Fore.BLUE + "\nLa película ha sido modificada correctamente\n")

def delCat():
    print(Fore.RED + "\n===== Eliminación de película =====")
    titulo = input(Fore.RED + "Ingrese el título: ")
    lenCircular.eliminar_DLC(titulo)
    lenCircular.delete(titulo)
    print(Fore.LIGHTGREEN_EX + "El Usuario ha sido eliminado correctamente")
    print(Fore.RED + "================================= \n")

def gesCat():
    print(Fore.YELLOW + "\n1. Cargar categorías y películas")
    print(Fore.YELLOW + "2. Ver categorías y películas")
    print(Fore.YELLOW + "3. Agregar categorías y películas")
    print(Fore.YELLOW + "4. Modificar categorías y películas")
    print(Fore.YELLOW + "5. Eliminar categorías y películas")
    print(Fore.YELLOW + "6. Regresar a gestiones\n")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        lenCircular.CargarXML_LDC(1)
        print(Fore.GREEN + "Datos cargados al sistema")
        gesCat()
    elif quintoPaso == "2":
        lenCircular.Imprimir_LDC()
        gesCat()
    elif quintoPaso == "3":
        AgCat()
    elif quintoPaso == "4":
        modCat()
        gesCat()
    elif quintoPaso == "5":
        delCat()
        gesCat()
    elif quintoPaso == "6":
        MenAdmin()
    else:
        print(Fore.RED+"Por favor, seleccione una opción válida")
        gesCat()

def AgSal():
    print(Fore.YELLOW + "\n===== Registro de sala =====")
    Asientos = input(Fore.BLUE + "Ingrese la cantidad de asientos: ")

    def regresarMenuP():
        print(Fore.YELLOW + "1. Registrar una nueva sala")
        print(Fore.YELLOW + "2. Regresar al menú de salas \n")
        tercerPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

        if tercerPaso == "1":
            AgSal()
        elif tercerPaso == "2":
            gesSal()
        else:
            print(Fore.RED+"Por favor, seleccione una opción válida")
            regresarMenuP()

    lenDoble.agregarXML_LED(Asientos)
    print(Fore.YELLOW + "\nSe ha registrado una nueva sala")
    print(Fore.YELLOW + "================================= \n")
    regresarMenuP()

def modSal():
    print(Fore.CYAN + "\n===== Modificación de salas =====")
    Sale = input(Fore.CYAN + "Ingrese la sala a modificar: ")
    chairs = input(Fore.CYAN + "Ingrese el nuevo numero de asientos: ")

    lenDoble.editarXML_LED(Sale, chairs)

    print(Fore.LIGHTGREEN_EX + "La película ha sido modificada correctamente") 
    print(Fore.CYAN + "=========================================\n")

def delSal():
    print(Fore.RED + "\n===== Eliminación de sala =====")
    sala = input(Fore.RED + "Ingrese el título: ")
    lenDoble.eliminar_LED(sala)
    lenDoble.delete(sala)
    print(Fore.LIGHTGREEN_EX + "El Usuario ha sido eliminado correctamente") 
    print(Fore.RED + "=========================================\n")

def gesSal():
    print(Fore.BLUE + "\n1. Cargar salas")
    print(Fore.BLUE + "2. Ver salas")
    print(Fore.BLUE + "3. Agregar salas")
    print(Fore.BLUE + "4. Modificar salas")
    print(Fore.BLUE + "5. Eliminar salas")
    print(Fore.BLUE + "6. Regresar a gestiones\n")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        lenDoble.CargarXML_LED(1)
        print(Fore.GREEN + "Datos cargados al sistema")
        gesSal()
    elif quintoPaso == "2":
        lenDoble.mostrar()
        gesSal()
    elif quintoPaso == "3":
        AgSal()
    elif quintoPaso == "4":
        modSal()
        gesSal()
    elif quintoPaso == "5":
        delSal()
        gesSal()
    elif quintoPaso == "6":
        MenAdmin()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesSal()

def modUser():
    print(Fore.CYAN + "\n===== Modificación de usuario =====")
    Email = input(Fore.CYAN + "Ingrese su correo: ")
    Role = input(Fore.CYAN + "Ingrese su nuevo rol: ")
    Nombre = input(Fore.CYAN + "Ingrese su nuevo nombre: ")
    Apellido = input(Fore.CYAN + "Ingrese su nuevo apellido: ")
    Telefono = input(Fore.CYAN + "Ingrese su nuevo teléfono: ")
    Password = input(Fore.CYAN + "Ingrese su nueva contraseña: ")

    lenSimple.editarXML(Role, Nombre, Apellido, Telefono, Email, Password)

    print(Fore.LIGHTGREEN_EX + "El Usuario ha sido modificado correctamente")
    print(Fore.CYAN + "=========================================\n")

def delUser():
    print(Fore.RED + "\n===== Modificación de usuario =====")
    Email = input(Fore.RED + "Ingrese su correo: ")
    lenSimple.eliminarXML(Email)
    lenSimple.delete(Email)
    print(Fore.LIGHTGREEN_EX + "El Usuario ha sido eliminado correctamente")
    print(Fore.RED + "=========================================\n")

def gesUser():
    print(Fore.WHITE + "\n1. Cargar datos")
    print(Fore.WHITE + "2. Ver usuarios")
    print(Fore.WHITE + "3. Modificar usuarios")
    print(Fore.WHITE + "4. Eliminar usuarios")
    print(Fore.WHITE + "5. Regresar a gestiones\n")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        lenSimple.CargarXML(1)
        print(Fore.GREEN + "Datos cargados al sistema")
        gesUser()
    elif quintoPaso == "2":
        lenSimple.Imprimir()
        gesUser()
    elif quintoPaso == "3":
        modUser()
        gesUser()        
    elif quintoPaso == "4":
        delUser()
        gesUser()
    elif quintoPaso == "5":
        MenAdmin()
    else:
        print(Fore.RED+"Por favor, seleccione una opción válida")
        gesUser()

def gesBoletos():
    print(Fore.BLACK + "\n1. Cancelar boletos")
    print(Fore.BLACK + "2. Regresar al menú\n")

    sextoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if sextoPaso == "1":
        pass
    elif sextoPaso == "2":
        MenAdmin()
    else:
        print(Fore.RED+"Por favor, seleccione una opción válida")
        gesBoletos()

def MenAdmin():
    print(Fore.LIGHTMAGENTA_EX + "\n========== Opciones =============")
    print(Fore.LIGHTMAGENTA_EX + "1. Gestionar boletos ")
    print(Fore.LIGHTMAGENTA_EX + "2. Gestionar categorías y películas ")
    print(Fore.LIGHTMAGENTA_EX + "3. Gestionar salas ")
    print(Fore.LIGHTMAGENTA_EX + "4. Gestionar usuarios ")
    print(Fore.LIGHTMAGENTA_EX + "5. Regresar al menú ")
    print(Fore.LIGHTMAGENTA_EX + "============================\n")

    cuartoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if cuartoPaso == "1":
        gesBoletos()
    elif cuartoPaso == "2":
        gesCat()
    elif cuartoPaso == "3":
        gesSal()
    elif cuartoPaso == "4":
        gesUser()
    elif cuartoPaso == "5":
        Pantalla_Inicial()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        MenAdmin()


lista_historial = []

def comBol(username):
    global lista_historial
    print(Fore.YELLOW+"=== Películas Disponibles ===")
    lenCircular.Imprimir_LDC()
    titulo = input(Fore.CYAN+"Ingrese el título de la película que quiere ver: ")
    pelicula_seleccionada = lenCircular.obtener_pelicula_por_titulo(titulo)
    if pelicula_seleccionada is not None:
        print("--- Detalles de la Película ---")
        print("Título:", pelicula_seleccionada.Titulo)
        print("Fecha:", pelicula_seleccionada.Fecha)
        print("Hora:", pelicula_seleccionada.Hora)
    else:
        print("No se encontró la película con ese título.")
        comBol(username)

    n_boletos = input(Fore.YELLOW+"Ingrese el numero de boletos: ")

    lenDoble.mostrar()

    num_sala = input(Fore.CYAN+"Ingrese el número de sala: ")
    sala_seleccionada = lenDoble.verificar_informacion(num_sala)
    if sala_seleccionada is not None:
        print("--- Detalles de la Sala ---")
        print("Número de sala: ", sala_seleccionada.num_sala)
        print("Cantidad de asientos: ", sala_seleccionada.asiento)
    else:
        print("El número de sala no coincide.")
        comBol(username)

    n_asiento = input("Ingrese el numero de asiento: ")
    monto_total = int(n_boletos) * 42

    datos_facturacion = input("Desea ingreasar datos de facturacion s/n")

    nit = ""
    direccion = ""

    if datos_facturacion.lower() == 's' :
        nit = input(Fore.MAGENTA+"Ingrese el NIT ")
        direccion = input(Fore.MAGENTA+"Ingrese la direccion ")

    else:
        nit="CF"
        direccion ="CF"

    obj_his = (pelicula_seleccionada.Titulo, pelicula_seleccionada.Fecha, pelicula_seleccionada.Hora, n_boletos, sala_seleccionada.num_sala, n_asiento, monto_total, nit, username, direccion)
    lista_historial.append(obj_his)

    for historial in lista_historial:
        print(Fore.LIGHTBLUE_EX+f"{historial[0]} {historial[1]} {historial[2]} {historial[3]} {historial[4]} {historial[5]} {historial[6]} {historial[7]} {historial[8]} {historial[9]}")

    def regresarMenuP():
        print(Fore.BLUE + "1. Registrar un nuevo boleto")
        print(Fore.BLUE + "2. Regresar al menú de cliente\n")
        kick_back = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

        if kick_back == "1":
            comBol(username)
        elif kick_back == "2":
            MenCliente(username)
        else:
            print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
            regresarMenuP()

    regresarMenuP()

def hisBol(username):
    global lista_historial
    for historial in lista_historial:
        print(Fore.LIGHTBLUE_EX+f"{historial[0]} {historial[1]} {historial[2]} {historial[3]} {historial[4]} {historial[5]} {historial[6]} {historial[7]} {historial[8]} {historial[9]}")
    MenCliente(username)


lista_favs = []

def favPel(username):
    global lista_favs
    print(Fore.YELLOW+"\n========= Películas Disponibles ========= \n")
    lenCircular.Imprimir_LDC()
    print()
    titulo = input(Fore.CYAN+"Ingrese el título de la película que guardar como favorita: ")
    print()
    pelicula_seleccionada = lenCircular.obtener_pelicula_por_titulo(titulo)
    if pelicula_seleccionada is not None:
        pass
    else:
        print("No se encontró la película con ese título.\n")
        favPel(username)

    obj_fav = (pelicula_seleccionada.Titulo, username)
    lista_favs.append(obj_fav)

    for historial in lista_favs:
        print(Fore.WHITE +f"Usuario: {historial[1]}, Película favorita: {historial[0]}")

    def regresarMenuP():
        print(Fore.BLUE + "\n1. Registrar una nueva película favorita")
        print(Fore.BLUE + "2. Regresar al menú de cliente\n")
        kick_back = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

        if kick_back == "1":
            favPel(username)
        elif kick_back == "2":
            MenCliente(username)
        else:
            print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida\n")
            regresarMenuP()

    regresarMenuP()


def MenCliente(username):
    print(Fore.LIGHTMAGENTA_EX + "\n======== Opciones =========")
    print(Fore.LIGHTMAGENTA_EX + "1. Listado películas ")
    print(Fore.LIGHTMAGENTA_EX + "2. Comprar boletos ")
    print(Fore.LIGHTMAGENTA_EX + "3. Historial boletos ")
    print(Fore.LIGHTMAGENTA_EX + "4. Películas favoritas ")
    print(Fore.LIGHTMAGENTA_EX + "5. Regresar al menú ")
    print(Fore.LIGHTMAGENTA_EX + "============================\n")

    cuartoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if cuartoPaso == "1":
        lenCircular.Imprimir_LDC()
        MenCliente(username)
    elif cuartoPaso == "2":
        comBol(username)
    elif cuartoPaso == "3":
        hisBol(username)
    elif cuartoPaso == "4":
        favPel(username)
    elif cuartoPaso == "5":
        Pantalla_Inicial()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        MenCliente(username)

def Iniciar_sesion():
    print(Fore.YELLOW + "\n======= Inicio de sesión ========")
    Email = input(Fore.YELLOW + "Ingrese su correo: ")
    Password = input(Fore.YELLOW + "Ingrese su contraseña: ")
    print(Fore.YELLOW + "================================= \n")

    actual = lenSimple.cabeza
    while actual is not None:
        if actual.data.correo == Email:
            if actual.data.contraseña == Password:
                print(Fore.GREEN+"Inicio de sesión exitoso")
                if actual.data.rol == "Cliente" or actual.data.rol == "cliente":
                    MenCliente(actual.data.nombre)
                elif actual.data.rol == "Administrador" or actual.data.rol == "administrador":
                    MenAdmin()
                else:
                    print(Fore.RED+"Usuario no encontrado")
                return
            else:
                print(Fore.RED+"Contraseña incorrecta")
                Iniciar_sesion()
        actual = actual.next
    print(Fore.RED+"Correo electrónico no encontrado")
    Pantalla_Inicial()

def Registrar_usuario():
    print(Fore.BLUE + "\n===== Registro de usuario =====")
    Nombre = input(Fore.BLUE + "Ingrese su nombre: ")
    Apellido = input(Fore.BLUE + "Ingrese su apellido: ")
    Telefono = input(Fore.BLUE + "Ingrese su teléfono: ")
    correo = input(Fore.BLUE + "Ingrese su correo: ")
    Password = input(Fore.BLUE + "Ingrese su contraseña: ")

    def regresarMenuP():
        print(Fore.BLUE + "1. Registrar un nuevo usuario")
        print(Fore.BLUE + "2. Regresar al menú principal\n")
        tercerPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

        if tercerPaso == "1":
            Registrar_usuario()
        elif tercerPaso == "2":
            Pantalla_Inicial()
        else:
            print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
            regresarMenuP()

    if lenSimple.existe_usuario_correo(correo):
        print(Fore.RED + "El correo ingresado ya está registrado.")
        regresarMenuP()
    else:
        lenSimple.agregarXML(Nombre, Apellido, Telefono, correo, Password)
        print(Fore.LIGHTGREEN_EX + "Se ha registrado un nuevo usuario")
        print(Fore.BLUE + "================================= \n")
        regresarMenuP()

    regresarMenuP()

def Ver_listado():
    print(Fore.RED + "\n==== Listado de películas ====")
    print(Fore.RED + "1. Listado general")
    print(Fore.RED + "2. Listado por categoría")
    print(Fore.RED + "3. Regresar al menú")
    print(Fore.RED + "============================\n")

    segundoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if segundoPaso == "1":
        lenCircular.Imprimir_LDC()
        Ver_listado()
    elif segundoPaso == "2":
        categoria = input(Fore.BLUE + "Ingrese la categoria para descubrir las peliculas: ")
        lenCircular.mostrar_peliculas_categoria(categoria)
        Ver_listado()
    elif segundoPaso == "3": 
        Pantalla_Inicial()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        Ver_listado()

def Pantalla_Inicial():
    print(Fore.CYAN + "\n======== Menú principal =========")
    print(Fore.CYAN + "| 1. Iniciar sesión             |")
    print(Fore.CYAN + "| 2. Registar usuario           |")
    print(Fore.CYAN + "| 3. Ver listado de películas   |")
    print(Fore.CYAN + "| 4. Cerrar programa            |")
    print(Fore.CYAN + "================================= \n")

    primerPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if primerPaso == "1":
        Iniciar_sesion()
    elif primerPaso == "2":
        Registrar_usuario()
    elif primerPaso == "3": 
        Ver_listado()
    elif primerPaso == "4": 
        exit()
    else:
        print(Fore.RED+"Por favor, seleccione una opción válida")
        Pantalla_Inicial()

UserPrincipal = Usuario("administrador", "Luis", "Castro", "202109750", "a", "a")
lenSimple.add(UserPrincipal)

Pantalla_Inicial()