print("---Cursos---")
print("Matematicas - Biologia - Lenguaje - Ciencias")

curso = input("Ingrese el curso deseado: ")

print(curso)

if curso in ("Matematicas , Biologia , Lenguaje , Ciencias"):
    print("Curso {0} seleccionado.".format(curso))
else:
    print("No existe ese curso...")
