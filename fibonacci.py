def fibo(n):
    
    a = 0
    b = 1 
    
    listafibo = [a, b]  
 
    for i in range(2, n):
        c = a + b
        listafibo.append(c)
        a = b
        b = c
    return listafibo

num = int(input("Ingrese un numero: "))
print(fibo(num))

    
