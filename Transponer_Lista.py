def transpose(lista):
    print(lista)
    lista_transpuesta = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if i == 0:
                lista_transpuesta.append([])
            lista_transpuesta[j].append(lista[i][j])
    print(lista_transpuesta)


#Prueba
lista = [[1]]
transpose(lista)