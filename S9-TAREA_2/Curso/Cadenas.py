texto = "BienveNidos al caNal de UskOKrum2010"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())  #Convierte una cadena a un formato de titulo
print(texto.find("al"))   #Posición donde encuentra la cadena o porción
print(texto.count("e"))   #Cantidad de concurrencia de una letra a porción

textoFinal = texto.replace("e", "3")
print(textoFinal)

valor = texto.isnumeric()   #Arroja true o false, dependiendo si es un número
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)