def bubble_sort(lista_equipas: list[tuple], index: int):
    for i in range(len(lista_equipas) - 1):
        for j in range(len(lista_equipas) - 1):
            if lista_equipas[j + 1][index] < lista_equipas[i][index]:
                lista_equipas[i + 1], lista_equipas[i] = (
                    lista_equipas[i],
                    lista_equipas[i + 1],
                )
    return lista_equipas
