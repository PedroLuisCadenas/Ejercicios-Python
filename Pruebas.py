def piramide_asteriscos(numero):
    for i in range(0, numero):
        if (i == 0):
            caracter = "*" * (i+1)
            print(caracter)
        else:
            caracter = "*" * (i-1) 
            print(caracter)    



#Prueba
num = 5
piramide_asteriscos(num)