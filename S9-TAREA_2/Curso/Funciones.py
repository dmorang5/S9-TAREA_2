# Funcion es un conjunto de instrucciones que realizan un proceso o tarea.
#Su principal ventaha es que ayuda a evitar codigo repetido

def saludar():
    print("Garcia")
    print("Oscar")
    print("UskoKruM2010")
    return "Hola"

print(saludar())

def evalueSueldoMinimo (sueldo):
    if sueldo >= 850:
        print("Cumple con el sueldo")
    else:
        print("Ganas menos que el sueldo minimo")

evalueSueldoMinimo(100)