def fibo(n):
    
    a = 0
    b = 1
    
    lista = [a,b]
    
    for i in range(2, n):
        c = a + b
        lista.append(c)
        a,b = b,c
    return lista

print(fibo(10))
    
    
    
    
