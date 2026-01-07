def tablamultiplicar(n):
    
    for i in range(1,11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}") 

tablamultiplicar(int(input("Ingrese un número para ver su tabla de multiplicar: ")))
