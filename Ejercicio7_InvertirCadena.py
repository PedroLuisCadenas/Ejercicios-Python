#Programa que invierte la cadena de texto recibida
def InvertirCadena(cadena):
    cadena_final = [0] * len(cadena)

    for i in range(0, len(cadena)):
        cadena_final[i] = cadena[-i - 1] #Ponemos ese -1 para que no empiece con el valor 0

    return cadena_final


#Prueba
cadena = [1, 2, 3]
print(InvertirCadena(cadena))