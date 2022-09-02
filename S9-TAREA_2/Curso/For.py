# Bucle: Son estructuras de control de flujo que repite una o varias lineas de codigo.

for num in range(0,10):
    print("Valor actual: {0}".format(num))

for num in range(0,20,2):
    print("Valor actual: {0}".format(num))

for i in range(1,13):
    print("{0} x {1} es: {2}".format(i, i, (i * i)))

for nom in ["Karen", "Oscar", "Hector", "Leonardo"]:
    print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
