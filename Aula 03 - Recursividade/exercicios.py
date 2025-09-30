# Função Max_Lista(L) que devolve o máximo dos elementos de uma lista L.
def Max_Lista(L):
    if len(L) == 1: return L[0]
    return max(L[0], Max_Lista(L[1:]))

print(Max_Lista([3, 5, 1, 7, 4]))


# Idem Min_Lista(L) para o mínimo.
def Min_Lista(L):
    if len(L) == 1: return L[0]
    return min(L[0], Min_Lista(L[1:]))

print(Min_Lista([3, 5, 1, 7, 4]))


# Função Inverte_Lista(L) que devolve a lista L invertida
def Inverte_Lista(L):
    if len(L) == 0: return L
    return L[-1:] + Inverte_Lista(L[:-1])

print(Inverte_Lista([5, 4, 3, 2, 1]))


# Função Potencia(x, n) que recebe x ≠ 0 float e n > 0 inteiro e devolve x^n
def Potencia(x, n):
    if n == 0: return 1
    return x * Potencia(x, n-1)

print(Potencia(2, 3))


# Função Soma_Seq(x, n) que recebe x float e n ≥ 0 inteiro e devolve o valor da soma: x + x^2/2 + x^3/3 + .... x^n/n
def Soma_Seq(x, n):
    if n == 0: return 0
    return (Potencia(x, n) / n) + Soma_Seq(x, n-1)

print(Soma_Seq(2, 3)) # 2 + 2^2/2 + 2^3/3 = 6.666


# Função Soma_Seq(x, eps) que recebe x float e eps float (eps - valor pequeno – ex: 10-5  x é um valor entre 0 e 1) e devolve o valor da soma acima até encontrar um termo que seja menor que eps.
def soma_seq2(x, n, eps):
    print(n)
    s = (Potencia(x, n) / n)
    if s < eps: return 0
    return s + soma_seq2(x, n+1, eps)

def Soma_Seq2(x, eps):
    return soma_seq2(x, 1, eps)

print(Soma_Seq2(0.5, 10e-5))


# Função Busca(L, x) que recebe uma lista L e um valor x e procura x em L. Devolve o primeiro k tal que L[k] = x ou -1 se não encontrar. Está resolvido à frente, mas tente resolvê-lo sem ver a solução.
def busca(L, x, k):
    if k >= len(L): return -1
    if L[k] == x: return k
    return busca(L, x, k+1)

def Busca(L, x):
    return busca(L, x, 0)

print(Busca([5, 4, 3, 2, 1], 3))


# Função Binomial(n, k) que devolve o número binomial de n e k. A definição recursiva do número binomial de n e k é: 0 se se n = 0 e k > 0; 1 se se n ≥ 0 e k = 0; Binomial(n-1, k) + Binomial(n-1, k-1) se n e k > 0
def Binomial(n, k):
    if n == 0 and k > 0: return 0
    elif n >= 0 and k == 0: return 1
    return Binomial(n-1, k) + Binomial(n-1, k-1)

Binomial(3, 2)  # 3


# Seja f(x, n)  =  x^n  (n  ≥  0 inteiro). Observe que f(x, n) = 1 se n = 0 e x * f(x,  n - 1) se n  >  0
# Exercício 11: Escreva a função acima nas versões iterativa e recursiva.
def Potencia_Iterativa(x, n):
    p = 1
    for _ in range(n): p *= x
    return p

print(Potencia_Iterativa(2, 3))  # 8


def Potencia_Recursiva(x, n):
    print("chamada!")
    if n == 0: return 1
    return x * Potencia_Recursiva(x, n-1)

print(Potencia_Recursiva(2, 10))  # 1024


# Faça uma função pot(x, n) recursiva usando a definição acima. Verifique na sua solução quantas chamadas à função pot são feitas. O objetivo é que a função faça o mínimo de chamadas possível.
def pot(x, n):
    print("chamada!")
    if n == 0: return 1
    h = n // 2
    p = pot(x, h)
    if n % 2 == 0: print("par!"); return p*p
    print("impar")
    return p*p*x

print(pot(2, 10))  # 1024


# Quantas multiplicações são feitas para se calcular x^n no algoritmo acima ?
# n/2 + 1 se n par, n/2 + 2 se n impar

# Refaça os 2 exercícios anteriores expandindo a definição para n negativo, lembrando que:
# x^n  = 1 / x^-n  se n  <  0. Se n < 0 e x = 0 a função não está definida.
def Potencia_Negativa_Recursiva(x, n):
    if x == 0 and n < 0: raise ValueError("Zero não!")
    if n == 0: return 1
    if n < 0: return 1 / Potencia_Negativa_Recursiva(x, -n)
    return x * Potencia_Negativa_Recursiva(x, n - 1)

print(Potencia_Negativa_Recursiva(2, -3))  # 0.125
print(Potencia_Negativa_Recursiva(2, 3))  # 8


def pot_negativa(x, n):
    if x == 0 and n < 0: raise ValueError("Zero não!")
    if n == 0: return 1
    if n < 0: return 1 / pot_negativa(x, -n)
    h = n // 2
    p = pot_negativa(x, h)
    if n % 2 == 0: return p*p
    return p*p*x

print(pot_negativa(2, 10))  # 1024
print(pot_negativa(2, -10))  # 0.0009765625


# Dado n e uma sequência com n números, imprimir a sequência na ordem inversa a que foi lida. Fazer isso sem usar listas.  Sugestão: faça uma função recursiva imprime, que lê um número, chama a si própria se não chegou ao fim da sequência e imprime o número lido.
def Imprime_Inverso(n, seq):
    if n == 0: print("\n"); return
    print(seq[n-1], end=" ")
    return Imprime_Inverso(n-1, seq)

Imprime_Inverso(5, [5, 4, 3, 2, 1])
