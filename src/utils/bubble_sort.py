def bubble_sort(lista):
	qtd_elementos = len(lista)
	
	for i in range(qtd_elementos - 1):
		for i in range(qtd_elementos - 1):
			if type(lista[i]) == int:
				if lista[i+1] > lista[i]:
					lista[i+1], lista[i] = lista[i], lista[i+1]
			else:
				if lista[i+1] < lista[i]:
					lista[i+1], lista[i] = lista[i], lista[i+1]
	
	return lista