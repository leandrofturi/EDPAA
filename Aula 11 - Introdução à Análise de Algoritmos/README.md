1) Raízes da equação do 2º grau
    - Melhor:  O(1) (número constante de operações)
    - Médio: O(1)
    - Pior: O(1)

2) Máximo de uma sequência (N elementos)
    - Melhor: O(N) (precisa olhar todos)
    - Médio: O(N)
    - Pior: O(N)

3) Contagem de nulos em vetor (N elementos)
    - Melhor: O(N) (tem que varrer tudo para contar)
    - Médio: O(N)
    - Pior: O(N)

4) Igualdade entre dois vetores (tamanho N)
    - Melhor: O(1) se o primeiro elemento já difere
    - Médio: O(N) (em média, diferença por volta do meio)
    - Pior: O(N) se são idênticos (ou diferem só no último)

5) Impressão de matriz N×M
    - Melhor: O(NxM) (tem que imprimir todos os elementos)
    - Médio: O(NxM)
    - Pior: O(NxM)

6) Multiplicação de matrizes (A: N×M, B: M×P)
    - Melhor: O(NxMxP) (três laços aninhados; não há atalhos)
    - Médio: O(NxMxP)
    - Pior: O(NxMxP)

7) Produto escalar (N elementos)
    - Melhor: O(N) (é necessário considerar todos os pares)
    - Médio: O(N)
    - Pior: O(N)
