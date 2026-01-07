def esprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# resultado = esprimo(11)
# print(resultado)

numero = int(input("Ingrese un numero: "))

if esprimo(numero) == True:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")
    