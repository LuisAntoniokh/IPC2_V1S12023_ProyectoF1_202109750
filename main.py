from colorama import Fore
from Lists.simpleList import ListaEnlazada

pclave = ['administrador', 'Luis', 'Castro', '202109750', 'a', 'a'] 

def canBol():
    pass
def verCat():
    pass
def AgCat():
    pass
def modCat():
    pass
def delCat():
    pass

def gesBoletos():
    print(Fore.WHITE + "1. Cancelar boletos")
    print(Fore.WHITE + "2. Regresar al menú")

    sextoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if sextoPaso == "1":
        canBol()
    elif sextoPaso == "2":
        MenAdmin()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesBoletos()

def gesCat():
    print(Fore.WHITE + "1. Ver categorías")
    print(Fore.WHITE + "2. Agregar categorías")
    print(Fore.WHITE + "3. Modificar categorías")
    print(Fore.WHITE + "4. Eliminar categorías")
    print(Fore.WHITE + "5. Regresar a gestiones")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        verCat()
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
        gesCat()

def gesSal():
    print(Fore.WHITE + "1. Ver salas")
    print(Fore.WHITE + "2. Agregar salas")
    print(Fore.WHITE + "3. Modificar salas")
    print(Fore.WHITE + "4. Eliminar salas")
    print(Fore.WHITE + "5. Regresar a gestiones")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        verCat()
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

def gesUser():
    print(Fore.WHITE + "1. Ver usuarios")
    print(Fore.WHITE + "2. Modificar usuarios")
    print(Fore.WHITE + "3. Eliminar usuarios")
    print(Fore.WHITE + "4. Regresar a gestiones")

    quintoPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if quintoPaso == "1":
        verCat()
    elif quintoPaso == "2":
        modCat()
    elif quintoPaso == "3":
        delCat()
    elif quintoPaso == "4":
        MenAdmin()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        gesUser()

def MenAdmin():
    print(Fore.LIGHTMAGENTA_EX + "\n==== Opciones ====")
    print(Fore.LIGHTMAGENTA_EX + "1. Gestionar boletos")
    print(Fore.LIGHTMAGENTA_EX + "2. Gestionar categorías y películas")
    print(Fore.LIGHTMAGENTA_EX + "3. Gestionar salas")
    print(Fore.LIGHTMAGENTA_EX + "4. Gestionar usuarios")
    print(Fore.LIGHTMAGENTA_EX + "5. Regresar al menú")
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
    print(Fore.LIGHTMAGENTA_EX + "1. Listado películas")
    print(Fore.LIGHTMAGENTA_EX + "2. Comprar boletos")
    print(Fore.LIGHTMAGENTA_EX + "3. Historial boletos")
    print(Fore.LIGHTMAGENTA_EX + "4. Películas favoritas")
    print(Fore.LIGHTMAGENTA_EX + "5. Regresar al menú")
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
    Correo = input(Fore.YELLOW + "Ingrese su correo: ")
    Contra = input(Fore.YELLOW + "Ingrese su contraseña: ")
    print(Fore.YELLOW + "================================= \n")

    """if user = Cliente:
            cliente()
        if user = Admin:
            Admin()
    """

def Registrar_usuario():
    print(Fore.BLUE + "\n===== Registro de usuario =====")
    Nombre = input(Fore.BLUE + "Ingrese su nombre: ")
    Apellido = input(Fore.BLUE + "Ingrese su apellido: ")
    Telefono = input(Fore.BLUE + "Ingrese su teléfono: ")
    Email = input(Fore.BLUE + "Ingrese su correo: ")
    Password = input(Fore.BLUE + "Ingrese su contraseña: ")
    print(Fore.BLUE + "\nSe ha registrado un nuevo usuario")
    print(Fore.BLUE + "================================= \n")

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
    print(Fore.CYAN + "================================= \n")

    primerPaso = input(Fore.GREEN + "¿Qué acción quiere realizar? ")

    if primerPaso == "1":
        Iniciar_sesion()
    elif primerPaso == "2":
        Registrar_usuario()
    elif primerPaso == "3": 
        Ver_listado()
    else:
        print(Fore.LIGHTGREEN_EX+"Por favor, seleccione una opción válida")
        Pantalla_Inicial()

lista = ListaEnlazada()
print("Cargando XML para lista enlazada ...")
lista.CargarXML(1)

lista.Imprimir()

Pantalla_Inicial()