numero = int (input())
esPrimo = False
Nmultiplo = 0


for i in range (1, 100):
    if(numero%i == 0):
        Nmultiplo += 1  #Contamos el numero de multiplos que tiene el numero

    if(Nmultiplo > 2):
        esPrimo = False #Si tiene más de 2 multiplos no es primo

    if(Nmultiplo == 2):
        esPrimo = True  #Si tiene solo 2 multiplos es primo

#Si al finalizar el bucle la variable esPrimo queda igual a True, el numero es primo
if(esPrimo == True):
    print("El número " + str(numero) + " es primo")
else:
    print("El número " + str(numero) + " no es primo")    


for inicio in range(1, 101):
    if inicio <= 1: #Si el número es menor o igual a 1 skipeamos
        continue

    for i in range (2, inicio):
        if(inicio%i == 0):  #Si encuentra un número que sea su divisor, entonces "inicio" no es primo
            break
    
    else:
        print (str(inicio))
          


