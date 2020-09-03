
"""
	A função abaixo irá realizar a troca dos elementos de acordo
	com o particionamento feito das duas sublistas
"""


def troca(entrada, i, j):

	if i < j:

		aux = entrada[i]				
	
		entrada[i] = entrada[j]
		
		entrada[j] = aux

"""
	A função abaixo irá realizar as chamada recursivas para
	cada metade da lista a ser ordenada
"""

def quickSort(entrada, p, r):

	if p < r:

		q = particao(entrada, p, r)
		quickSort(entrada, p, q - 1)
		quickSort(entrada, q + 1, r)

"""
	A função abaixo irá dividir a entrada principal em
	duas sublistas, para que o pivô seja usado como referencial
	para a ordenação delas
"""

def particao(entrada, p, r):

	pivo = entrada[r]

	j = p

	i = p - 1

	for j in range(j, r):

		if entrada[j] <= pivo:

			i = i + 1

			troca(entrada, i, j)

	troca(entrada, i + 1, r)

	return i + 1

"""
	Logo abaixo uma lista representando uma entrada arbitrária
"""

entrada = [9, 10, -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0]


"""
	Logo abaixo a chamada da função quickSort para realizar todos os
	passos descritos
"""

quickSort(entrada, 0, 14)

"""
	Logo abaixo a exibição da entrada ordenada na tela
"""

print(entrada)