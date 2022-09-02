#Diccionarios: Son estructuras de datos que permiten almacenar distintos
#valores.
#Los datos se almacena asociado a una clave unica, tenemos una relacion clave:valor
#Los elementos almacenados estan en desorden, el orden es indiferente a la forma de
#almacenamiento

miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlin"}
print(miDiccionario["Perú"])
print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)

miDiccionario["España"] = "Barcelona"
print(miDiccionario)

del miDiccionario["España"]   #borrar un elemento
print(miDiccionario)

dic2 = {"Garcia": "Oscar", 25: True, "Sueldo":150.80}
print(dic2[25])

llaves = ("España", "Francia", "Inglaterra")
dicPaises={llaves[0]:"Madrid", llaves[1]:"Paris", llaves[2]:"Londres"}
print(dicPaises)

datosPersonales={"Apellido": "Garcia", "Anios":{1:2010, 2:2011, 3:2012, 4:2013, 5:2014}}
print(datosPersonales)
print(datosPersonales["Anios"])

print(datosPersonales.get('Apellido',"Oscar"))

print(datosPersonales.values())
print(datosPersonales.keys())
valores = list(datosPersonales.values())
print(valores)
valores = tuple(datosPersonales.values())
print(valores)
