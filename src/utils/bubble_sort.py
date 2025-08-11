def bubble_sort(lista_equipas: list[tuple], index: int):
    for i in range(len(lista_equipas) - 1):
        for j in range(len(lista_equipas) - 1):
            if lista_equipas[i][index] < lista_equipas[j][index]:
                lista_equipas[i], lista_equipas[j] = (
                    lista_equipas[j],
                    lista_equipas[i],
                )
    if index != 1:
        lista_equipas.reverse()
    return lista_equipas
