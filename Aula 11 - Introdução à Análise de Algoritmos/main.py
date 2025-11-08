from math import sqrt
import random, timeit
from math import sqrt


def raiz(a, b, c):
    x1 = (-b-sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b+sqrt(b*b-4*a*c))/(2*a)
    return x1, x2


def max_seq(a, N):
    m = a[0]
    for i in range(1, N):
        if m < a[i]:
            m = a[i]
    return m


def nulos(a, N):
    c = 0
    for i in range(N):
        if a[i] == 0:
            c += 1
    return c


def vec_eq(a, b, N):
    for i in range(N):
        if a[i] != b[i]:
            return False
    return True


def imp_mat(a, N, M):
    for i in range(N):
        for j in range(M):
            print(a[i][j], end=" ")
        print("")


def mat_mult(a, b, N, M, P):
    c = [[0 for _ in range(P)] for _ in range(N)]
    for i in range(N):
        for j in range(P):
            c[i][j] = 0
            for k in range(M):
                c[i][j] += a[i][k] * b[k][j]
    return c


def vec_dot(a, b, N):
    c = 0
    for i in range(N):
        c += a[i]*b[i]
    return c


def bench_sizes(name, sizes, maker, func, repeats=1):
    rows = []
    for sz in sizes:
        args = maker(sz)
        t = timeit.timeit(lambda: func(*args), number=repeats)
        rows.append({"Algoritmo": name, "Tamanho": sz, "Chamadas": repeats, "Tempo_s": t})
    return rows

rows = []
rows += bench_sizes("raiz", [1,2,3], lambda _: (2, -5, 3), raiz, repeats=10000)
rows += bench_sizes("max_seq", [10_000, 20_000, 40_000],
                    lambda N: ([random.random() for _ in range(N)], N), max_seq, repeats=3)
rows += bench_sizes("nulos", [10_000, 20_000, 40_000],
                    lambda N: ([0 if random.random()<0.3 else 1 for _ in range(N)], N), nulos, repeats=3)
rows += bench_sizes("vec_eq (pior)", [10_000, 20_000, 40_000],
                    lambda N: (list(range(N)), list(range(N)), N), vec_eq, repeats=3)
rows += bench_sizes("vec_eq (melhor)", [10_000, 20_000, 40_000],
                    lambda N: ([-1]+list(range(1,N)), list(range(N)), N), vec_eq, repeats=100)
rows += bench_sizes("imp_mat", [(10,10), (20,10), (40,10)],
                    lambda sz: ([[1]*sz[1] for _ in range(sz[0])], sz[0], sz[1]), imp_mat, repeats=1)
rows += bench_sizes("mat_mult", [30, 45, 60],
                    lambda N: ([[random.random() for _ in range(N)] for _ in range(N)],
                               [[random.random() for _ in range(N)] for _ in range(N)], N, N, N),
                    mat_mult, repeats=1)
rows += bench_sizes("vec_dot", [10_000, 20_000, 40_000],
                    lambda N: ([random.random() for _ in range(N)], [random.random() for _ in range(N)], N),
                    vec_dot, repeats=3)

from pprint import pprint
pprint(rows)
