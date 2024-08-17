datos = {}

def registro(datos):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    datos[usuario] = contraseña

    return datos

def login(datos):
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in datos and datos[usuario] == contraseña:
        print(f"Bienvenido {usuario}!")
    else:
        print("El usuario y la contraseña no coinciden, intentelo nuevamente.")
        return login(datos)
    
registro(datos)
login(datos)
