# Cuando indicamos un * adelante del parámetro de una función, estamos indicando que se va a recibir un número indeterminado
# de parámetros. Además, esos parámetros se recibirán en forma de tupla.

"""def devuelveLenguaje(*lenguajes):
    for leng in lenguajes:
        yield leng"""

"""def devuelveLenguaje(*lenguajes):
    for leng in lenguajes:
        for letra in leng:
            yield letra"""

def devuelveLenguaje(*lenguajes):
    for leng in lenguajes:
        yield from leng

lenguajesObtenidos = devuelveLenguaje("Python", "Java", "PHP", "Ruby", "JavaScript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))