def exp(a, n):
    if n == 0:
        return 1
    else:
        aux = exp(a, n // 2)
        aux = aux * aux
        if n % 2 == 1:
            aux = aux * a
        return aux