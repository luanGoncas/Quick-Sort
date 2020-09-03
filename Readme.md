# ---------- Projeto e Análise de Algoritmos -------------------- ALGORITMO DE ORDENAÇÃO QUICK SORT -------------------- #

Neste algoritmo de ordenação o vetor é particionado em dois por meio de um procedimento recursivo. Essa divisão ocorre

até que o vetor fique com apenas um elemento, enquanto os demais ficam ordenados à medida que ocorre o particionamento.

Esse algoritmo é baseado na técnica de divisão e conquista, que é feita da seguinte forma:


- DIVIDIR: A lista entrada[p...r] é particionada em duas sublistas não vazias entrada[p...q] e entrada[q + 1...r], tais

que cada elemento de entrada[p...q] é menor ou igual a cada elemento de entrada[q + 1...r]. O índice q é calculado como

parte do processo de particionamento. Para determinar o índice q, escolhe-se o elemento que se encontra no fim da lista

original, chamado de pivô, e rearranjam-se os elementos da lista de forma que os que ficarem à esquerda de q são menores

(ou iguais) ao pivô e os que ficarem à direita de q são maiores ou iguais ao pivô. A escolha do pivô é arbitrária, o que 

permite que ele seja o último elemento, o elemento central, ou qualquer outro.


- CONQUISTAR: As duas sublistas são ordenadas entrada[p...q] e entrada[q + 1...r] por chamadas recursivas ao QUICK SORT.

Durante o processo recursivo, os elementos vão sendo ordenados na própria lista, não exigindo nenhum processamento nesta

etapa.
