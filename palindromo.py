'''Detectar palíndromos: crea una función que reciba 
   una cadena y devuelva True si es un palíndromo, 
   ignorando espacios y mayúsculas'''

def palindromo():
    cadena = input("Ingresa una cadena de texto: ")
    cadena_nueva = "".join(cadena.split()).lower() 
    return cadena_nueva == cadena_nueva[::-1]
    
    
print("Es palíndromo" if palindromo() else "No es palíndromo")