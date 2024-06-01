#Un programa que cuenta cuántas veces se repite una palabra en una cadena de texto
import re

def ContarPalabra (cadena, palabra):
    n_palabra = 0
    cadena = re.split(r', ', cadena) #Funcion que separa la cadena por palabras delimitandolo por espacios y comas
    for i in range(0, len(cadena)):
        if cadena[i] == palabra:
            n_palabra += 1
        else:
            continue
    return n_palabra


print("Introduzca la cadena de texto: ")
cadena = input()
print("Introduzca la palabra a contar: ")
palabra = input()

n_palabra = ContarPalabra(cadena, palabra)
print(str(n_palabra))
