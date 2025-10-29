# Detectar palíndromos: crea una función que reciba una cadena y devuelva True si es un palíndromo, ignorando espacios y mayúsculas.

def palindromo():
    cadena = input("Ingrese una cadena: ")
    
    cadena_limpia = ''.join(cadena.split()).lower()
    
    return cadena_limpia == cadena_limpia[::-1]

resultado = palindromo()

print(f"Es un palíndromo." if resultado else "No es un palíndromo")
