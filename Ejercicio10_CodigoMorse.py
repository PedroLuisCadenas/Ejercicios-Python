#Programa que recibe una cadena de texto y la pasa a Código Morse y viceversa

def PasarMorseYNatural (cadena):
    cadena_array = cadena.upper() #La función .upper() sirve para que todos los caracteres se pongan en mayúscula
    cadena_final = [] 
    diccionario = {"A" : ". -", "B" : "- . . .", "C" : "- . - ."
    ,"D" : "- . .", "E" : "." ,"F" : ". . - ." ,"G" : "- - ." 
    ,"H" : ". . . ." ,"I" : ". ." ,"J" : ". - - -" ,"K" : "- . -"
    ,"L" : ". - . ." ,"M" : "- -" ,"N" : "- .","O" : "- - -","P" : ". - - ."
    ,"Q" : "- - . -","R" : ". - ." ,"S" : ". . ." ,"T" : "-"
    ,"U" : ". . -" ,"V" : ". . . -","W" : ". - -","X" : "- . . -","Y" : "- . - -" 
    , "Z" : "- - . ."}  #Esto es un diccionario, donde podemos acceder al valor a través de la clave
    
    diccionario_morse = {v : k for k, v in diccionario.items()} #Sintaxis para invertir las claves y los valores de un diccionario
    
    for i in cadena_array:
        if i != "." or i != "-":
            if i in cadena_array:
                cadena_final.append(diccionario[i]) #La función .append() lo que hace es añadir el valor dentro de la lista
        #else:
         #   if i in cadena_array:
          #      cadena_final.append(diccionario_morse[i])
    return cadena_final


#Falta implementar la parte en la que la función lo hace a la inversa(de morse a natural)

#Prueba
texto = ". -"
morse = PasarMorseYNatural(texto)

print(str(morse))