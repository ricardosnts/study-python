def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor_indice = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j

        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    return lista

lista = [5,2,10,20,1,4]

print(selection_sort(lista))
print(len(lista))
print(lista[0])