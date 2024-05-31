print("¿De qué figura quiere saber el área?: ")
figura = str(input())
print("Introduzca su base y su altura: ")
base = float(input())
altura = float(input())

if figura == "triangulo" :
    print("El área es: " + str((base * altura) / 2) )
elif figura == "cuadrado" or figura == "rectangulo" :
    print("El área es: " + str(altura * base)) 
 
          