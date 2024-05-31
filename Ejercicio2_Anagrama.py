def esAnagrama(palabra, palabra_2):
    arraypalabra = list(palabra)
    arraypalabra2 = list(palabra_2)
    return sorted(arraypalabra) == sorted(arraypalabra2)



palabra1 = str(input())
palabra2 = str(input())
noIguales = False

while noIguales is False:
    if palabra1 == palabra2:
        print("Palabras iguales no, introduce de nuevo: ")
        palabra1 = str(input())
        palabra2 = str(input())
    else:
        break

print("¿Las palabras son anagrama? " + str(esAnagrama(palabra1, palabra2)))


