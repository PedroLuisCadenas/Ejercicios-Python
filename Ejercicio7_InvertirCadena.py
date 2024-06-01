#Programa que invierte la cadena de texto recibida

cadena = list(input())
cadena_final = [0] * len(cadena)

for i in range(0, len(cadena)):
    cadena_final[i] = cadena[-i - 1] #Ponemos ese -1 para que no empiece con el valor 0

print(cadena_final)