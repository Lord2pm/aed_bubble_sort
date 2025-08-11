from pprint import pprint


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


if __name__ == "__main__":
    lista = [
        (1, "Ajax", "ajax.png", 36, 200.0),
        (2, "AS Roma", "as_roma.png", 3, 150.0),
        (3, "Atlético de Madrid", "atletico_madrid.png", 11, 350.0),
        (4, "Barcelona", "barcelona.png", 97, 750.0),
        (5, "Bayern de Munique", "bayern_de_munique.png", 80, 700.0),
        (6, "Borussia Dortmund", "borrussia_dortmund.png", 19, 300.0),
        (7, "Chelsea", "chelsea.png", 34, 600.0),
        (8, "Inter de Milão", "inter_milan.png", 31, 400.0),
        (9, "Juventus", "juventus.png", 69, 450.0),
        (10, "Leipzig", "leipzig.png", 3, 180.0),
        (11, "Liverpool", "liverpool.png", 67, 550.0),
        (12, "Manchester City", "manchester_city.png", 28, 620.0),
        (13, "Manchester United", "manchester_united.png", 68, 650.0),
        (14, "Paris Saint-Germain", "psg.png", 50, 500.0),
        (15, "Real Madrid", "real_madrid.png", 99, 800.0),
    ]
    lista_ordenada = bubble_sort(lista, 3)
    pprint(lista_ordenada)
