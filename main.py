from colorama import Fore
from Lists.simpleList import ListaEnlazada
from Lists.dobleCircle import listaDobleCircular
import xml.etree.ElementTree as ET

from Objects.user import Usuario

lenSimple = ListaEnlazada()
lenCircular = listaDobleCircular()

def canBol():
    pass
def AgCat():
    pass
def modCat():
    pass
def delCat():
    pass

def gesBoletos():
    print(Fore.WHITE + "\n1. Cancelar boletos")
    print(Fore.WHITE + "2. Regresar al menú\n")

    sextoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if sextoPaso == "1":
        canBol()
    elif sextoPaso == "2":
        MenAdmin()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesBoletos()

def gesCat():
    print(Fore.WHITE + "\n1. Cargar categorías y películas")
    print(Fore.WHITE + "2. Ver categorías y películas")
    print(Fore.WHITE + "3. Agregar categorías y películas")
    print(Fore.WHITE + "4. Modificar categorías y películas")
    print(Fore.WHITE + "5. Eliminar categorías y películas")
    print(Fore.WHITE + "6. Regresar a gestiones\n")

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
    elif quintoPaso == "5":
        delCat()
    elif quintoPaso == "6":
        MenAdmin()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesCat()

def gesSal():
    print(Fore.WHITE + "\n1. Ver salas")
    print(Fore.WHITE + "2. Agregar salas")
    print(Fore.WHITE + "3. Modificar salas")
    print(Fore.WHITE + "4. Eliminar salas")
    print(Fore.WHITE + "5. Regresar a gestiones\n")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        pass
    elif quintoPaso == "2":
        AgCat()
    elif quintoPaso == "3":
        modCat()
    elif quintoPaso == "4":
        delCat()
    elif quintoPaso == "5":
        MenAdmin()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesSal()

def modUser():
    print(Fore.BLUE + "\n===== Modificación de usuario =====")
    Email = input(Fore.BLUE + "Ingrese su correo: ")
    Role = input(Fore.BLUE + "Ingrese su nuevo rol: ")
    Nombre = input(Fore.BLUE + "Ingrese su nuevo nombre: ")
    Apellido = input(Fore.BLUE + "Ingrese su nuevo apellido: ")
    Telefono = input(Fore.BLUE + "Ingrese su nuevo teléfono: ")
    Password = input(Fore.BLUE + "Ingrese su nueva contraseña: ")

    lenSimple.editarXML(Role, Nombre, Apellido, Telefono, Email, Password)

    print(Fore.BLUE + "\nEl Usuario ha sido modificado correctamente\n")

def delUser():
    print(Fore.BLUE + "\n===== Modificación de usuario =====")
    Email = input(Fore.BLUE + "Ingrese su correo: ")
    lenSimple.eliminarXML(Email)
    lenSimple.delete(Email)
    print(Fore.BLUE + "\nEl Usuario ha sido eliminado correctamente\n")

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
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesUser()

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

def LisPel():
    pass
def comBol():
    pass
def hisBol():
    pass
def favPel():
    pass

def MenCliente():
    print(Fore.LIGHTMAGENTA_EX + "\n======== Opciones =========")
    print(Fore.LIGHTMAGENTA_EX + "1. Listado películas ")
    print(Fore.LIGHTMAGENTA_EX + "2. Comprar boletos ")
    print(Fore.LIGHTMAGENTA_EX + "3. Historial boletos ")
    print(Fore.LIGHTMAGENTA_EX + "4. Películas favoritas ")
    print(Fore.LIGHTMAGENTA_EX + "5. Regresar al menú ")
    print(Fore.LIGHTMAGENTA_EX + "============================\n")

    cuartoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if cuartoPaso == "1":
        LisPel()
    elif cuartoPaso == "2":
        comBol()
    elif cuartoPaso == "3":
        hisBol()
    elif cuartoPaso == "4":
        favPel()
    elif cuartoPaso == "5":
        Pantalla_Inicial()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        MenCliente()

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
                    MenCliente()
                elif actual.data.rol == "Administrador" or actual.data.rol == "administrador":
                    MenAdmin()
                else:
                    print(Fore.RED+"Usuario no encontrado")
                return
            else:
                print(Fore.RED+"Contraseña incorrecta")
                return
        actual = actual.next
    print(Fore.RED+"Correo electrónico no encontrado")

def Registrar_usuario():
    print(Fore.BLUE + "\n===== Registro de usuario =====")
    Nombre = input(Fore.BLUE + "Ingrese su nombre: ")
    Apellido = input(Fore.BLUE + "Ingrese su apellido: ")
    Telefono = input(Fore.BLUE + "Ingrese su teléfono: ")
    correo = input(Fore.BLUE + "Ingrese su correo: ")
    Password = input(Fore.BLUE + "Ingrese su contraseña: ")

    def regresarMenuP():
        print(Fore.BLUE + "1. Registrar un nuevo usuario")
        print(Fore.BLUE + "2. Regresar al menú principal")
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
        print(Fore.BLUE + "\nSe ha registrado un nuevo usuario")
        print(Fore.BLUE + "================================= \n")
        regresarMenuP()

    regresarMenuP()

def genList():
    pass

def catList():
    pass

def Ver_listado():
    print(Fore.RED + "\n==== Listado de películas ====")
    print(Fore.RED + "1. Listado general")
    print(Fore.RED + "2. Listado por categoría")
    print(Fore.RED + "3. Regresar al menú")
    print(Fore.RED + "============================\n")

    segundoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if segundoPaso == "1":
        genList()
    elif segundoPaso == "2":
        catList()
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
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        Pantalla_Inicial()

UserPrincipal = Usuario("administrador", "Luis", "Castro", "202109750", "a", "a")
lenSimple.add(UserPrincipal)

Pantalla_Inicial()