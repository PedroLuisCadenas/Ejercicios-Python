#Programa que recibe un número decimal y lo devuelva en binario
from Ejercicio7_InvertirCadena import InvertirCadena

def PasarBinario (numero):
    cadena_binaria = [0] * 15
    i = 0
    while numero > 0:
        if numero%2 == 0:
            cadena_binaria[i] = "0"
        elif numero%2 == 1:
            cadena_binaria[i] = "1"
        numero /= 2
        numero = int(numero)
        i += 1

    return InvertirCadena(cadena_binaria)

#Prueba:
numero = 23519
binario = PasarBinario(numero)

print(binario)
