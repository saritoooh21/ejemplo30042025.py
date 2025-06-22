numero_secreto = 3
intentos = 0

while True: 
    intento = int(input("Adivina el número (entre 1 y 3): "))
    intentos += 1 

    if intento == numero_secreto:
        print("¡Correcto! Lo adivinaste en ", intentos, "intentos")
        break
    elif intento ==0:
        print("Saliste del juego.")
        break
    elif intento < 0:
        print("Número inválido. Se salta esta ronda.")
        continue
    else:
        print("Incorrecto, intenta de nuevo.")
