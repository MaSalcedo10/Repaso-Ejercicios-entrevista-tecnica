def fiboahorro(n):
    
    a = int(input("Ingrese el ahorro del primer mes: "))
    b = a*2
    
    ahorro = {}
    
    ahorro["Mes 1"] = a
    ahorro["Mes 2"] = b
    
        
    for i in range(2, n):
        
        c = a + b
        ahorro[f"Mes {i+1}"] = c
        a = b
        b = c
    print("El detalle de su ahorro mensual es el siguiente: ")
    for mes, cantidad in ahorro.items():
        print(f"{mes}: {f"${cantidad:,.2f}"}")
        
    print(f"Total ahorrado es: {f'${sum(ahorro.values()):,.2f}'}")
    

print("Bienvenido al desafío de ahorro Fibonacci")

num = int(input("Ingrese la cantidad de meses que desea ahorrar: "))

fiboahorro(num)








