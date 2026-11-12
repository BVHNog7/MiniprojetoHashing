# Relatório do mini-projeto

O experimento usa 2.400 linhas geradas pelo programa. As duas estratégias recebem as mesmas consultas, na mesma ordem. Os tempos foram medidos com `perf_counter()` no Python 3.12.14 em Linux. A preparação do texto e a impressão dos resultados ficaram fora da medição.

## Experimento 1 — 1.000 buscas

| Medição | Tempo (ms) |
| --- | ---: |
| Construção do índice | 10,222 |
| Busca por varredura | 6.720,792 |
| Busca com o índice pronto | 9,516 |

## Experimento 2 — Incluindo a construção

Para cada quantidade de consultas, foram feitas três rodadas. A tabela mostra o tempo do meio depois de ordenar as três medições, ou seja, a mediana.

| Consultas | Varredura (ms) | Construção + buscas com índice (ms) |
| ---: | ---: | ---: |
| 1 | 6,019 | 8,050 |
| 2 | 11,976 | 7,156 |
| 10 | 61,743 | 7,595 |
| 100 | 606,353 | 8,510 |
| 1.000 | 6.153,565 | 16,523 |

## Análise

1. Com o índice pronto, as 1.000 buscas levaram cerca de 10 ms. A varredura levou cerca de 6,7 segundos porque percorreu o texto a cada consulta. Para uma consulta só, foi mais rápido fazer a varredura do que montar o índice e depois usá-lo.
2. Nesse teste, o índice compensou a partir de duas consultas. A varredura levou 11,976 ms. Montar o índice e fazer as duas buscas levou 7,156 ms.
3. O conjunto guarda o número da linha uma vez. Se uma palavra aparece três vezes na linha 4, o índice guarda o 4 uma vez. Também dá para unir os conjuntos na busca OU e pegar o que eles têm em comum na busca E.
4. A consulta de uma chave em um dicionário custa `O(1)` em média. Se a busca encontra `r` linhas, ordenar a resposta pode custar até `O(r log r)`.
5. Construir o índice custa `O(C)` em média, com `C` sendo o número de caracteres do texto. Se dois conjuntos têm tamanhos `a` e `b`, a união custa `O(a + b)` em média. A interseção custa `O(min(a, b))` em média, pois a operação percorre o menor conjunto e verifica se cada item também está no maior.
6. O índice ocupa mais memória porque guarda as palavras e os números das linhas onde cada uma aparece.
