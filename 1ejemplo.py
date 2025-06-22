cantidad = int(input("¿Cuántos estudiantes tiene el lado izquierdo?"))
estudiantes = []

for i in range(cantidad):
    nombre = input("Ingresa el nombre del estudiante # " + str(i + 1) + ": ")
    estudiantes.append(nombre)
    #apprend es para el uso de listas, por esa razón estudiantes está con []
    edad = input("Ingrese la edad del estudiante: ")

print("\nLista de estudiantes:")
for nombre in estudiantes:
    print("-", nombre, "tiene", edad, "años")
