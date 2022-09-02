# Break: Permite salir de un bucle cuando se cumple una condicion

"""for numero in range(1,6):
    if numero == 3:
        break # Descanso o interrupción en este punto
    print("El numero es: {0}".format(numero))

print("Bucle terminado")"""

#Continue: Omite una parte del bucle cuando se cumple una condicion y contunúa con el resto
"""for numero in range(1,6):
    if numero == 3:
        continue #Continua con el resto del bucle
    print("El numero es: {0}".format(numero))

print("Bucle terminado")"""

#Pass: Permite continuar con una sentencia o función que ya no tiene o aún no tiene un bloque de código útil.
for numero in range(1,6):
    if numero <= 3:
        pass #Aquí no pasa nada y el bulce sigue trabajando
    else:
        print("El siguiente valor es mayor a 3")
    print("El numero es: {0}".format(numero))

print("Bucle terminado")

def funcionSinImplementar():
    pass
