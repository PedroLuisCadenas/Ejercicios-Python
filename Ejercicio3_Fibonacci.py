numero = 0
numero2 = 1

for i in range (0, 50): 
    numero_siguiente = numero + numero2
    numero = numero2
    numero2 = numero_siguiente
    i += 1
    print(numero_siguiente)
