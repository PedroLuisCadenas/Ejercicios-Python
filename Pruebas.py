def piramide_asteriscos(numero):
    
    for i in range(1, numero+1):
        if i % 2 == 1:
            if i == 1 :
                print(" "*(int(numero/2)) + "*"*i + " "*(int(numero/2)))
            elif i > 1 and i < numero-1:
                print(" "*(int((numero-i)/2)) + "*"*i + " "*(int((numero-i)/2)))
        
            else:
                print("*"*(i))
        else:   
            continue


#Prueba
num = 15
piramide_asteriscos(num)