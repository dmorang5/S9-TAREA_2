import os
os.system("cls")

class Menu:
    def __int__(self):
        x=10
        pass
    def menu(self, opciones, titulo):
        print(titulo)
        for opcion in opciones:
            print(opcion)
        literal = input("Elija la sección deseada [1....{}]: ".format(len(opciones)))
        return literal