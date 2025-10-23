def esprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True   

def cantidad():
    
    cantidad = int(input("Ingrese la cantidad: "))
    
    lista = []

    for i in range(1,cantidad):
        if esprimo(i) == True:
            lista.append(i)
        else:
           continue
       
    print(lista)
    
cantidad()
