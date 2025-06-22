combustible = 0
total = 3 #vamos a tener esta variable como la totalidad tanque 

while combustible < total:
    cantidad = int(input("¿Cuántos litros desea cargar? "))
    combustible += cantidad 
    if combustible > total:
        print("¡Cuidado! Te pasaste, el tanque se desbordó.")
        break
    print("Combustible actual: ", combustible, "L")

print("Carga de combustible completa.")
