while True:
    print("\n¡Bienvenido a HeyClic, escoge tu video!")
    print("Opciones disponibles:")
    print("1. Instalación Java")
    print("2. Instalación Windows Server")
    print("3. Instalación Cisco PacketTracer")
    print("4. Salir")

    opcion = input("\nElige una opción: ")

    match opcion:
        case "1":
            print("Has seleccionado Java. A desarrollar.")
        case "2":
            print("Has seleccionado Windows Server. Simulación VM.")
        case "3":
            print("Has seleccionado Cisco PacketTracer. ¡Que lo disfrutes!")
        case "4":
            print("Saliendo... ¡Hasta pronto!")
            break
        case _:
            print("\nOpción no válida. Por favor digite de nuevo")
