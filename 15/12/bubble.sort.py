def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # troca os elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

lista = [5,2,10,20,1,4]

print(bubble_sort(lista))
print(len(lista))
print(lista[0])