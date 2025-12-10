import math
import sys

def dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx*dx + dy*dy)


def closest_pair_rec(px, py):
    n = len(px)
    if n <= 3:
        min_d = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                min_d = min(min_d, dist(px[i], px[j]))
        return min_d

    mid = n // 2
    Qx = px[:mid]
    Rx = px[mid:]

    midx = px[mid][0]
    # Divide o conjunto em duas metades
    Qy = []
    Ry = []
    for p in py:
        if p[0] <= midx:
            Qy.append(p)
        else:
            Ry.append(p)

    # Resolve recursivamente
    d_esq = closest_pair_rec(Qx, Qy)
    d_dir = closest_pair_rec(Rx, Ry)
    d = min(d_esq, d_dir)
    
    # Combina os resultados considerando apenas pontos próximos da linha divisória
    faixa = [p for p in py if abs(p[0] - midx) < d]

    # verifica apenas os próximos
    tam_faixa = len(faixa)
    for i in range(tam_faixa):
        for j in range(i+1, min(i+7, tam_faixa)):
            d = min(d, dist(faixa[i], faixa[j]))
    return d

def closest_pair(points):
    lo = 0
    hi = len(points)-1
    px = sort(points, lo, hi, less0)
    py = sort(points, lo, hi, less1)
    return closest_pair_rec(px, py)


def less0(a, b):
    return a[0] < b[0]

def less1(a, b):
    return a[1] < b[1]

def merge(a, aux, lo, mid, hi, less_func):
    for k in range(lo, hi+1):
        aux[k] = a[k]
    i,j = lo, mid+1
    for k in range(lo, hi+1):
        if(i > mid):
            a[k] = aux[j]
            j+=1
        elif(j > hi):
            a[k] = aux[i]
            i+=1
        elif(less_func(aux[j], aux[i])):
            a[k] = aux[j]
            j+=1
        else:
            a[k] = aux[i]
            i+=1

def merge_sort(a, aux, lo, hi, less_func):
    if(hi <= lo):
        return
    mid = lo + (hi-lo) // 2
    merge_sort(a, aux, lo, mid, less_func)
    merge_sort(a, aux, mid+1, hi, less_func)
    merge(a, aux, lo, mid, hi, less_func)

def sort(a, lo, hi, less_func):
    aux = [None] * len(a)
    merge_sort(a, aux, lo, hi, less_func)
    return a


'''
--------------------------
    LEITURA DA ENTRADA
--------------------------
'''
def main():
    for linha in sys.stdin:
        N = int(linha.strip())
        if N == 0:
            break

        pontos = []
        for _ in range(N):
            x, y = map(int, sys.stdin.readline().split())
            pontos.append((x, y))

        resposta = closest_pair(pontos)

        if resposta >= 10000:
            print("INFINITY")
        else:
            print(f"{resposta:.4f}")


if __name__ == "__main__":
    main()


'''
Análise do comportamento pela relação de recorrência:
'''