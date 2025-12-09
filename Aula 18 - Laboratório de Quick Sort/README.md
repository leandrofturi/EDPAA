# Quick Sort - Versões
## V1, V2, V5 e V8
* Muitos timeouts para 100K+ e 1M
* Sensíveis a entradas ordenadas/reversas ou com muitas chaves iguais

## V3 - mediana de 3 (sem cut-off)
* Estável em todos os tipos de entrada
* Sempre mais lenta que as versões com cut-off

## V4 - mediana de 3 + cut-off (top-down)
* Melhor desempenho geral
* Cut-off ideal entre 30 e 35
* Pouco impacto da ordem inicial (sorted, reverse, nearly_sorted, rand)

## V6 - bottom-up + cut-off
* Tempos próximos da V4, porém em geral um pouco piores

## V8 - 3-way (Dijkstra)
* Não compensa em dados aleatórios normais
* Espera-se vantagem clara em entradas com poucas chaves distintas (few_uniq), mas houve timeout em 10M

## Quick Sort (V4) vs Merge Sort
* Para até 1M elementos:
    - Quick V4 e Merge sort otimizado têm tempos bem próximos
    - Quick usa menos memória e aproveita melhor cache
    - Merge tem comportamento mais previsível (sempre O(n log n))

* Para 10M (onde houve timeout):
    - Pelo padrão observado em 1M, espera-se tempos similares entre Quick V4 e Merge sort em sorted, reverse_sorted, nearly_sorted, unif_rand
    - Quick V4 levemente mais rápido em geral
    - Merge sort mantendo a vantagem em estabilidade e previsibilidade de tempo

# Conclusão
* A melhor variante de quick sort do laboratório é a V4 (mediana de 3 + cut-off ~30-35, sem shuffle).
* Entre Quick V4 e Merge sort, não há vencedor absoluto:
    - se o critério é memória e desempenho prático, Quick V4 é preferível
    - se o critério é previsibilidade e estabilidade, Merge sort é mais seguro
