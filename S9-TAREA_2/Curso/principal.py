import os

from main import Menu
"""from Curso import Modulo, Paquete1, POO, Break_Continue_Pass, Cadenas, Concatenacion, \
    Conversiones, Diccionarios, Excepciones,Factorial, For, Funciones, Generadores, Generadores2, \
    HolaMundo, If_Else, If_In, IngresoDatos, Listas, Numeros_Operaciones, OperadoresLogicos, OperadorTernario, \
    PruebaPaquete, Raise, Range, Tuplas, variables, While"""
main = Menu()

lista = ["1) Python", "2) Modulo","3) Paquete" ,"4) POO", "5) Salir"]
opcion = ""

while opcion != "5":
    os.system("cls")
    opcion = main.menu(lista, "Menu")
    os.system("cls")
    if opcion == '1':
        opc1=""
        while opc1 != "7":
            os.system("cls")
            print("PYTHON")
            opc1 = main.menu(["1) Ejercicio 1","2) Ejercicio 2","3) Ejercicio 3", "4) Ejercicio 4", "5) Ejercicio 5", "6) Ejercicio 6", "7) Ejercicio 7","8) Ejercicio 8" ,"9) Ejercicio 9" ,"10) Ejercicio 10"                                                                                                                                                           "1) Ejercicio 1",
                              "11) Ejercicio 11","12) Ejercicio 12", "13) Ejercicio 13", "14) Ejercicio 14", "15) Ejercicio 15", "16) Ejercicio 16","17) Ejercicio 17", "18) Ejercicio 18", "19) Ejercicio 19", "20) Ejercicio 20",
                              "21) Ejercicio 21","22) Ejercicio 22", "23) Ejercicio 23", "24) Ejercicio 24", "25) Salir"],
                              "Sub-menú Python")
            os.system("cls")
            if opc1 == "1":
                os.system("cls")
                from Curso import HolaMundo
                ejr1 = HolaMundo
                print(ejr1)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "2":
                os.system("cls")
                from Curso import variables
                ejr2 = variables
                print(ejr2)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "3":
                os.system("cls")
                from Curso import Conversiones
                ejr3 = Conversiones
                print(ejr3)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "4":
                os.system("cls")
                from Curso import Numeros_Operaciones
                ejr4 = Numeros_Operaciones
                print(ejr4)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "5":
                os.system("cls")
                from Curso import Concatenacion
                ejr5 = Concatenacion
                print(ejr5)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "6":
                os.system("cls")
                from Curso import Cadenas
                ejr6 = Cadenas
                print(ejr6)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "7":
                os.system("cls")
                from Curso import Tuplas
                ejr7 = Tuplas
                print(ejr7)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "8":
                os.system("cls")
                from Curso import Listas
                ejr8 = Listas
                print(ejr8)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "9":
                os.system("cls")
                from Curso import Diccionarios
                ejr9 = Diccionarios
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "10":
                os.system("cls")
                from Curso import IngresoDatos
                ejr10 = IngresoDatos
                print(ejr10)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "11":
                os.system("cls")
                from Curso import If_Else
                ejr11 = If_Else
                print(ejr11)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "12":
                os.system("cls")
                from Curso import Funciones
                ejr12 = Funciones
                print(ejr12)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "13":
                os.system("cls")
                from Curso import OperadoresLogicos
                ejr13 = OperadoresLogicos
                print(ejr13)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "14":
                os.system("cls")
                from Curso import OperadorTernario
                ejr14 = OperadorTernario
                print(ejr14)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "15":
                os.system("cls")
                from Curso import Range
                ejr15 = Range
                print(ejr15)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "16":
                os.system("cls")
                from Curso import For
                ejr16 = For
                print(ejr16)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "17":
                os.system("cls")
                from Curso import If_In
                ejr17 = If_In
                print(ejr17)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "18":
                os.system("cls")
                from Curso import Factorial
                ejr18 = Factorial
                print(ejr18)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "19":
                os.system("cls")
                from Curso import While
                ejr19 = While
                print(ejr19)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "20":
                os.system("cls")
                from Curso import Break_Continue_Pass
                ejr20 = Break_Continue_Pass
                print(ejr20)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "21":
                os.system("cls")
                from Curso import Generadores
                ejr21 = Generadores
                print(ejr21)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "22":
                os.system("cls")
                from Curso import Generadores2
                ejr22 = Generadores2
                print(ejr22)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "23":
                os.system("cls")
                from Curso import Excepciones
                ejr23 = Excepciones
                print(ejr23)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "24":
                os.system("cls")
                from Curso import Raise
                ejr24 = Raise
                print(ejr24)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "25":
                input("Saliendo..."
                      "\n" "Presione una tecla para continuar...")
                break
    if opcion == '2':
        opc1=""
        while opc1 != "7":
            os.system("cls")
            print("MODULO")
            opc1 = main.menu(["1) Ejercicio 1", "2) Salir"],"Sub-menú Modulo")
            os.system("cls")
            if opc1 == "1":
                os.system("cls")
                from Curso.Modulo import modulos
                ejr1 = modulos
                print(ejr1)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "2":
                input("Saliendo..."
                      "\n" "Presione una tecla para continuar...")
                break
    if opcion == '3':
        opc1=""
        while opc1 != "7":
            os.system("cls")
            print("PAQUETE")
            opc1 = main.menu(["1) Ejercicio ", "2) Salir"],"Sub-menú Paquete")
            os.system("cls")
            if opc1 == "1":
                os.system("cls")
                from Curso import PruebaPaquete
                ejr1 = PruebaPaquete
                print(ejr1)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "2":
                input("Saliendo..."
                      "\n" "Presione una tecla para continuar...")
                break
    if opcion == '4':
        opc1=""
        while opc1 != "7":
            os.system("cls")
            print("POO")
            opc1 = main.menu(["1) Ejercicio 1", "2) Ejercicio 2","3) Ejercicio 3 ","4) Ejercicio 4 ","5) Ejercicio 5 ","6) Ejercicio 6","7) Ejercicio 7 ","8) Salir"],"Sub-menú Poo")
            os.system("cls")
            if opc1 == "1":
                os.system("cls")
                from Curso.POO import Persona
                ejr1 = Persona
                print(ejr1)
                input("\n"
                      "Presiona una tecla para continuar:)")
            if opc1 == "2":
                os.system("cls")
                from Curso.POO import Curso
                ejr2 = Curso
                print(ejr2)
                input("\n"
                      "Presiona una tecla para continuar:)")
            if opc1 == "3":
                os.system("cls")
                from Curso.POO import Cuenta
                ejr3 = Cuenta
                print(ejr3)
                input("\n"
                      "Presiona una tecla para continuar:)")
            if opc1 == "4":
                os.system("cls")
                from Curso.POO import Herencia
                ejr4 = Herencia
                print(ejr4)
                input("\n"
                      "Presiona una tecla para continuar:)")
            if opc1 == "5":
                os.system("cls")
                from Curso.POO import HerenciaMultiple
                ejr5 = HerenciaMultiple
                print(ejr5)
                input("\n"
                      "Presiona una tecla para continuar:)")
            if opc1 == "6":
                os.system("cls")
                from Curso.POO import Polimorfismo
                ejr6 = Polimorfismo
                print(ejr6)
                input("\n"
                      "Presiona una tecla para continuar:)")
            if opc1 == "7":
                os.system("cls")
                from Curso.POO import RelacionesClases
                ejr7 = RelacionesClases
                print(ejr7)
                input("\n"
                      "Presiona una tecla para continuar:)")
            elif opc1 == "8":
                input("Saliendo..."
                      "\n" "Presione una tecla para continuar...")
                break