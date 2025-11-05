#	Detectar palíndromos: crea una función que reciba una cadena y devuelva True si es un palíndromo, ignorando espacios y mayúsculas.

def palindromo():
    cadena = input("Ingresa una cadena: ")
    cadena_limpia = "".join(c.lower() for c in cadena if c.isalnum())
    return cadena_limpia == cadena_limpia[::-1]

print("Es palíndromo" if palindromo() else "No es palíndromo")


