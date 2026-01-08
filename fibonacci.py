def fibo(n):
    
    a, b = 0, 1
    
    list = [a,b]
    
    for i in range(2,n):
        c = a + b
        list.append(c)
        a, b = b, c
    return list

print(fibo(10))