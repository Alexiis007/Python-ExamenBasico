# Examen Basico Python
# Calculadora de calificaciones 2024
"""
    Temas vistos:
    *Funciones con parametros
    *Comentarios
    *Uso de diccionarios
    *Uso de ciclo For
    *Uso de range()
    *Uso de operadores aritmeticos
    *Uso de operadores de comparacion y and o or
    *Uso de inputs y prints
    *Concatenacion de datos y casteo de datos
    *Uso de if, elif y else
    *Uso de listas y su metodo append
"""
alumnos = []


def promedios(p_calificaciones):
    promedio = 0
    for e in p_calificaciones:
        promedio += e
    promedio = promedio / 4
    return promedio


print("-------Calificaciones de los alumnos Soinf-------")
num_alumnos = int(input("Cuantos alumnos tiene: "))
for a in range(0, num_alumnos):
    alumno = {
        "nombre": input("Ingrese el nombre del alumno: "),
        "edad": int(input("Edad: ")),
        "calificaciones": [],
        "promedio": 0
    }
    for i in range(0, 4):
        calificiacion = int(input(f"Calificacion materia {i + 1}: "))
        alumno["calificaciones"].append(calificiacion)
    alumno["promedio"] = promedios(alumno["calificaciones"])
    alumnos.append(alumno)
print("-"*10, "Resultados", "-"*10)
for b in alumnos:
    print(f"=> Nombre: {b["nombre"]}")
    if b["promedio"] == 10:
        print(f"=> Aprobado con {b["promedio"]}, punto extra")
    elif 7 < b["promedio"] < 10:
        print(f"=> Aprobado con {b["promedio"]}")
    else:
        print(f"=> Reprobado con {b["promedio"]}")
    print("-"*34)


