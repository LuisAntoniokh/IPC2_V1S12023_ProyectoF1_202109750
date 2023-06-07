from colorama import Fore

def Iniciar_sesion():
    print(Fore.YELLOW + "\n======= Inicio de sesión ========")
    Correo = input(Fore.YELLOW + "Ingrese su correo: ")
    Contra = input(Fore.YELLOW + "Ingrese su contraseña: ")
    print(Fore.YELLOW + "================================= \n")

def Registrar_usuario():
    print(Fore.BLUE + "\n===== Registro de usuario =====")
    Nombre = input(Fore.BLUE + "Ingrese su nombre: ")
    Apellido = input(Fore.BLUE + "Ingrese su apellido: ")
    Telefono = input(Fore.BLUE + "Ingrese su teléfono: ")
    Email = input(Fore.BLUE + "Ingrese su correo: ")
    Password = input(Fore.BLUE + "Ingrese su contraseña: ")
    #Rol = Cliente
    print(Fore.BLUE + "================================= \n")

def Ver_listado():
    print(Fore.RED + "\nAquí va el listado")

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

Pantalla_Inicial()
