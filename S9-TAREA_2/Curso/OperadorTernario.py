"""
string sexo;
sexo = (10 > 2) ? "Masculino" : "Femenino" """

sexos = ("Hombre", "Mujer")

posicion = True
sexo = sexos[posicion] #Mujer
print(sexo)
sexo = sexos[not posicion] #Hombre
print(sexo)