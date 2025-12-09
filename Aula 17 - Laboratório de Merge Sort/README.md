# Resumo dos Resultados
## Versão 1 -- Clássica (top-down sem otimizações)
* Apresentou o pior desempenho geral
* Tempos entre 3-4 s para entradas de 1M em dados aleatórios

## Versão 2 -- Cut-off para Insertion Sort (top-down)
* Desempenho melhor que V1
* Melhora: ~15-25% em relação ao Merge Sort puro
* cutoff ~ 35 apresentou os melhores tempos

## Versão 3 -- Merge Skip (top-down)
* Melhora em entradas parcialmente ou totalmente ordenadas

## Versão 4 -- Cut-off + Merge Skip (top-down)
* Melhor desempenho entre todas as versões top-down
* O cut-off ideal ficou entre 25 e 35
* Variante mais eficiente

## Versões 5-7 -- Bottom-up
* Versão 5 (pura) ficou estável, porém mais lenta que V4
* Versão 6 (cut-off) teve tempos semelhantes ou piores
* Versão 7 (cut-off + merge skip) não superou a abordagem top-down


# Conclusão

* Merge skip oferece grande melhoria por si só
* Cut-off melhora a performance para valores entre 20 e 35
* A combinação das otimizações (V4) produz um ganho de até 10× em relação ao merge sort clássico e cerca de 4× sobre outras variantes otimizadas
