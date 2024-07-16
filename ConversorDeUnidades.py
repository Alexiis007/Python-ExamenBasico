"""
    Examen parte 2
    Uso de temas como:
    *Funciones con parametros
    *Match Case
    *While True
    *Breack
    *Casteo de datos
"""


def metros_kilometros(p_metros):
    print(f"Los {p_metros} metros a kilometros es: {p_metros/1000}")


def kilometros_metros(p_kilometros):
    print(f"Los {p_kilometros} kilometros a metros es: {p_kilometros*1000}")


def metros_centimetro(p_metros):
    print(f"Los {p_metros} metros a centimetros es: {p_metros*100}")


while True:
    print("-"*45)
    print("Converion de unidades")
    print("1- Metros a Kilometros")
    print("2- Kilometros a Metros")
    print("3- Centimetros a Metros")
    print("4- Salir")
    print("-" * 45)
    respuesta = int(input("Cual es tu respuesta: "))
    match respuesta:
        case 1:
            print("-"*10, "Metros a kilometros", "-"*10)
            metros = float(input("Ingresa los metros: "))
            metros_kilometros(metros)
        case 2:
            print("-"*10, "Kilometros a metros", "-"*10)
            kilometros = float(input("Ingresa los kilometros: "))
            kilometros_metros(kilometros)
        case 3:
            print("-"*10, "Metros a centimetros", "-"*10)
            metros = float(input("Ingresa los metros: "))
            metros_centimetro(metros)
        case 4:
            print("-"*10, "Adios!!", "-"*10)
            break
        case _:
            print("Esa no fue una opcion")

