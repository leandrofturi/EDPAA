# RELATÓRIO
Trabalho Prático T2 (Árvore B) \
EDPAA 2025/2 \
Leandro Furlam Turi \
Repositório: https://github.com/leandrofturi/EDPAA.git

## 1. Introdução

Este relatório descreve a implementação da Árvore B solicitada no Trabalho Prático T2. O objetivo é indexar registros com foco em armazenamento secundário, simulado por um arquivo binário. A solução implementa busca, inserção e remoção, imprime a árvore em largura ao final e segue a execução exigida pelo enunciado.

Além da correção das operações, este trabalho implementa modularização com TADs e a representação fixa em bytes dos nós para acesso por índice no arquivo, também conforme a especificação.

## 2. Estruturas Desenvolvidas

### 2.1. TAD BTree

Arquivo: **BTree.py**

Responsável pelas operações de busca, inserção e remoção. Principais decisões:
* `d` define a ordem da árvore, com `max_keys = d - 1`.
* `min_keys` é tratado com caso especial para `d = 2` (evitar árvore vazia) e a transformação de valor `d` ímpar em par, para evitar overflow em merges e manter n_keys <= max_keys.
* Inserção bottom-up: insere na folha, depois divide nós cheios.
* Chaves repetidas atualizam o valor existente.
* Antes de descer para um filho na remoção, garante que o filho não fique com menos chaves do que o mínimo permitido.
* Impressão em largura.

### 2.2. TAD BTreeNode

Arquivo: **BTreeNode.py**

Define a estrutura do nó da árvore:
* `n_keys`, `is_leaf`, arrays de `keys`, `values` e `children`.
* `children` é preenchido com `-1` na inicialização ou quando não existir.

### 2.3. TAD DiskManager

Arquivo: **diskManager.py**

Simula o armazenamento secundário com um arquivo binário, conforme especificação do trabalho:
* Layout fixo usando `struct` com formato `"ii" + "i"*max_keys + "i"*max_keys + "i"*d`.
* Cada nó ocupa `node_size` bytes e é acessado por índice: `offset = idx * node_size`.
* Operações `read_node` e `write_node` fazem leitura/escrita direta do nó.
* Um arquivo binário é criado no início e removido ao final.

## 3. Leitura, Execução e Saída

### 3.1. Entrada

Arquivo texto com:
1. Ordem `d`
2. Número de operações `n`
3. `n` linhas de operações `I`, `R` ou `B`

### 3.2. Execução

Padrão exigido pelo enunciado:
```
python trab2.py <arquivo_entrada> <arquivo_saida>
```

Se `<arquivo_saida> = "-"`, imprime no terminal.

### 3.3. Saída

Arquivo texto com:
* Uma linha por busca: `O REGISTRO ESTA NA ARVORE!` ou `O REGISTRO NAO ESTA NA ARVORE!`
* Impressão final da árvore em largura, nível a nível, com o prefixo `-- ARVORE B`.


### 3.4. Testes

Com a ajuda do ChatGPT, criamos alguns testes para validação.

#### 3.4.1. Teste 1

```
4
6
I 10, 10
I 20, 20
I 30, 30
I 40, 40
I 50, 50
I 60, 60
```

Passo a passo:
1. Insere 10: raiz folha fica `[10]`
2. Insere 20: `[10, 20]`
3. Insere 30: `[10, 20, 30]`
4. Insere 40: overflow, faz split e promove 30  
5. Insere 50: desce para a direita
6. Insere 60: continua na direita

Estado final:
```
-- ARVORE B
[key: 30, ]
[key: 10, key: 20, ][key: 40, key: 50, key: 60, ]
```

#### 3.4.2. Teste 2

```
4
8
I 10, 10
I 20, 20
I 30, 30
I 40, 40
B 10
R 10
R 20
R 30
```

Passo a passo:
1. Insere 10: raiz folha fica `[10]`
2. Insere 20: `[10, 20]`
3. Insere 30: `[10, 20, 30]`
4. Insere 40: overflow, faz split e promove 30  
5. Busca 10: encontra e imprime mensagem positiva
6. Remove 10: folha esquerda vira `[20]`
7. Remove 20: filho esquerdo estava no mínimo, faz fusão com o irmão direito e remove 20 do nó fundido
8. Remove 30: remove da raiz folha resultante

Saída:
```
O REGISTRO ESTA NA ARVORE!
-- ARVORE B
[key: 40, ]
```

## 4. Decisões que podem gerar árvores diferentes

Mesmo com o mesmo conjunto de operações, algumas escolhas de implementação levam a árvores distintas. Esta entendimento foi importante pois após a primeira implementação conforme referências diversas, observamos resultados distintos (mas conceituamente corretos) para o exemplo fornecido na implementação.

```
-- ARVORE B
[key: 40, key: 55, key: 75, ]
[key: 20, ][key: 45, key: 51, ][key: 60, key: 62, ][key: 77, ]
```

A saida deveria ser
```
-- ARVORE B
[key: 51, key: 75, ]
[key: 20, key: 40, key: 45, ][key: 55, key: 60, key: 62, ][key: 77, ]
```

Este caso apareceu quando a inserção é top‑down (split antes de descer), em vez de bottom‑up (split só depois de inserir na folha, que é o caso deste trabalho).

Com a ajuda do ChatGPT, entendemos o que muda:

1. Top‑down (primeiro resultado)
Dividimos nós cheios antes de inserir a chave nova: quando foi inserir `78`, a raiz tinha `[20, 75, 77]` e foi dividida antes de receber o `78`, então a chave promovida foi `75` (não `77`). Isso empurra a árvore para uma raiz `[40, 55, 75]` e mantém `77` no filho da direita, ficando `[77, 78]`.
2. Bottom‑up (saída correta, atual no trabalho)
Inserimos na folha e só depois ocorre a divisão. Então o split considera a chave nova e a mediana promovida muda (`77` e depois `51`), gerando a raiz `[51, 75]`.


### 4.1. Mediana no split

Quando ocorrer overflow (`len(keys) == d`) o código usa `mid = len(keys)//2`, ou seja, mediana superior quando `d` é par, mudando a distribuição entre filhos (método `_split_overflow`).
1. `left_keys = keys[:mid]` recebe as menores
2. `promo_k = keys[mid]` sobe
3. `right_keys = keys[mid+1:]` recebe as maiores

### 4.2. Split bottom-up
O split mencionado anteriormente só ocorre após inserir na folha e propagar para cima. Ou seja: o nó só é dividido depois de ficar cheio.
1. a operação de inserção desce recursivamente até a folha
2. insere a chave na folha
3. se passou do limite, chama o split (seção 4.1.)
4. o split retorna uma chave promovida para o pai
5. o pai recebe a chave promovida, se o pai estourar, ele também é dividido... e assim por diante até a raiz


### 4.3. Remoção em nó interno
Antes de descer para um filho na remoção, precisa-se garantir que o filho não fique com menos chaves do que o mínimo permitido, escolhendo uma dessas ações (método `_fix_child_underflow`):
1. se o filho esquerdo tem mais que o mínimo de chaves, dá para puxar a maior chave da subárvore esquerda (predecessor) e substituir a chave removida por ela. Depois, remove essa chave lá no filho esquerdo
2. se o filho direito também tem mais que o mínimo, ele usa a menor chave da subárvore direita (sucessor) para substituir a chave removida. Depois remove essa chave no filho direito
3. se nenhum dos filhos pode doar, ambos estão no mínimo de chaves, então não dá para puxar sem quebrar a regra. Nesse caso o algoritmo faz fusão: junta filho esquerdo + a chave do meio + filho direito em um único nó, e continua a remoção nesse nó fundido


### 4.4. Escolha do irmão para fusão
No item 4.3.3., quando nenhum irmão pode emprestar, prioriza fundir com o irmão direito, e só usa o esquerdo quando o direito não existe.


### 4.5. Rebalanceio adicional
Após a remoção, o método chama `_rebalance_level`. Esse passo percorre os filhos do nível da raiz e, se o irmão direito tiver chaves sobrando e o esquerdo estiver com espaço, ele faz um empréstimo da direita para a esquerda. É um ajuste extra para deixar o nível mais equilibrado.
* **Caso `d = 2`:** há um tratamento especial que evita remover a única chave da raiz folha, para não deixar a árvore vazia.

## 5. Análise da Implementação

### 5.1. Correção

A árvore mantém as propriedades de balanceamento:
* todas as folhas no mesmo nível,
* número de chaves limitado por `min_keys` e `max_keys`,
* splits e merges garantem que a árvore permaneça válida após inserções e remoções.

### 5.2. Complexidade

Considerando altura `h = O(log_d n)`:
* **Busca:** `O(d * h)` para varrer as chaves de cada nó e descer.
* **Inserção:** `O(d * h)` com possíveis splits em cada nível.
* **Remoção:** `O(d * h)` com empréstimos ou fusões ao longo do caminho.

Em armazenamento secundário, cada passo implica leitura/escrita do nó, então o número de I/Os é proporcional à altura da árvore.

### 5.3. Consumo de Memória

Cada nó ocupa tamanho fixo em bytes (`node_size`), com vetores de tamanho `d` ou `d-1`. O arquivo cresce linearmente com o número de nós: `O(n)`.

## 6. Conclusão

A solução implementa a Árvore B com armazenamento secundário simulado, respeita o padrão de entrada/saída e utiliza TADs opacos para modularização. O relatório destaca as principais decisões de implementação que influenciam a forma final da árvore, facilitando a justificativa de diferenças entre soluções corretas.
