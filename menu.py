def menu():
    try:
        while True:
            print("1. opción 1")
            print("2. opción 2")
            print("3. opción 3")
            print("4. Salir")
            
            opcion = input("Ingrese una opción: ")
            
            if opcion in ("1", "2", "3"):
                print(f"Elegiste la opción {opcion}")
            elif opcion == "4":
                print("Saliendo del menú...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
            
    except Exception as e:
        print("Ocurrió un error:", e)

menu()