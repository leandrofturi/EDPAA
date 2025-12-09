def max_divisao_e_conquista(A, p, r):
    if p == r:
        return A[p]
    else:
        meio = (p + r) // 2
        resp = max_divisao_e_conquista(A, p, meio)
        resp2 = max_divisao_e_conquista(A, meio + 1, r)
        if resp < resp2:
            return resp2
        else:
            return resp


# EXEMPLO DE USO
A = [7, 3, 12, 1, 9, 15, 4]

resultado = max_divisao_e_conquista(A, 0, len(A) - 1)

print("Vetor:", A)
print("Máximo encontrado por divisão e conquista:", resultado)


def max_trivial(A):
    s = A[0]
    for a in A:
        if s < a:
            s = a
    return s


print("Máximo encontrado por trivial:", max_trivial(A))
