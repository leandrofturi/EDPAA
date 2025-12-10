def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k]
    i, j = lo, mid+1
    inversoes = 0
    for k in range(lo, hi+1):  # Merge
        if (i > mid):
            a[k] = aux[j]
            j += 1
        elif (j > hi):
            a[k] = aux[i]
            i += 1
        elif (aux[j] < aux[i]):
            # aux[j] é menor que aux[i..mid] -> gera (mid - i + 1) inversões
            a[k] = aux[j]
            j += 1
            inversoes += (mid - i + 1)
        else:
            a[k] = aux[i]
            i += 1
    return inversoes


def mergesort_conta_inv(a, aux, lo, hi):
    if lo >= hi:
        return 0

    mid = (lo + hi) // 2

    inv_esq = mergesort_conta_inv(a, aux, lo, mid)
    inv_dir = mergesort_conta_inv(a, aux, mid + 1, hi)
    inv_merge = merge(a, aux, lo, mid, hi)

    return inv_esq + inv_dir + inv_merge


def kendall_tau(A, B):
    pos = [-1] * len(B)
    for idx, x in enumerate(B):
        pos[x] = idx

    C = [-1] * len(A)
    aux = [-1] * len(A)
    for idx, x in enumerate(A):
        C[idx] = pos[A[idx]]
        aux[idx] = pos[A[idx]]

    return mergesort_conta_inv(C, aux, 0, len(C) - 1)


# EXEMPLO DE USO
A = [2, 0, 1, 3]
B = [0, 1, 2, 3]
print("Kendall τ:", kendall_tau(A, B))


# Source - https://stackoverflow.com/a
# Posted by mikebob
# Retrieved 2025-12-09, License - CC BY-SA 4.0

from scipy.stats import kendalltau

def kendall_distance_count(a, b):
    tau, p_value = kendalltau(a, b)
    n = len(a)
    N = n * (n - 1) / 2
    D = (1 - tau) * N / 2
    return round(D)

print("Kendall τ:", kendall_distance_count(A, B))