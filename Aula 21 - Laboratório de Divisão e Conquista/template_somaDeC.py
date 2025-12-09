def soma_divisao_e_conquista(A, inicio, fim):
    # Caso base: intervalo com um único elemento
    if inicio == fim:
        return A[inicio]

    # Divide o vetor em duas metades
    meio = (inicio + fim) // 2

    # Soma recursivamente a metade esquerda e a metade direita
    soma_esq = soma_divisao_e_conquista(A, inicio, meio)
    soma_dir = soma_divisao_e_conquista(A, meio + 1, fim)

    # Conquista: combina as duas somas
    return soma_esq + soma_dir


# Função para chamar a soma
def soma_vetor(A):
    return soma_divisao_e_conquista(A, 0, len(A) - 1)


# EXEMPLO DE USO
A = [5, 2, 8, 3, 7]

resultado = soma_vetor(A)
print("Vetor:", A)
print("Soma calculada por divisão e conquista:", resultado)


def soma_vetor_trivial(A):
    s = 0
    for a in A:
        s += a
    return s


print("Soma calculada por trivial:", soma_vetor(A))
