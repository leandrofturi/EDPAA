import random
from item import less, exch
from pilhaListaEncadeada import PilhaListaEncadeada


def insertion_sort(a, lo, hi):
    for i in range(lo+1, hi+1):
        for k in range(i, lo, -1):
            if less(a[k-1], a[k]):
                break
            a[k], a[k-1] = exch(a[k], a[k-1])
    return a


def shuffle(a, lo, hi):
    for i in range(hi, lo - 1, -1):
        j = random.randint(lo, i)
        a[i], a[j] = exch(a[j], a[i])


def partition(a, lo, hi):
    i, j = lo+1, hi
    v = a[lo]
    while(1):
        while(less(a[i], v)): # Find on left to swap
            if(i == hi): break
            i+=1
        while(less(v, a[j])): # Find on right to swap
            if(j == lo): break
            j-=1
        if (i >= j): break # Check if pointers cross
        a[i], a[j] = exch(a[i], a[j])
    a[lo], a[j] = exch(a[lo], a[j])
    return j


def median_of_3(a, lo, hi):
    # Ordena a[lo], a[mid], a[hi] para que:
    # a[lo] <= a[mid] <= a[hi]
    mid = (lo + hi) // 2
    if less(a[mid], a[lo]):
        a[lo], a[mid] = exch(a[lo], a[mid])
    if less(a[hi], a[lo]):
        a[lo], a[hi] = exch(a[lo], a[hi])
    if less(a[hi], a[mid]):
        a[mid], a[hi] = exch(a[mid], a[hi])
    return mid


# Versao 1: quick sort classico top-down recursivo sem nenhuma otimizacao
def quick_sortV1(a, lo, hi):
    if(hi <= lo): return
    j = partition(a, lo, hi)
    quick_sortV1(a, lo, j-1)
    quick_sortV1(a, j+1, hi)


def sortV1(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV1(a, lo, hi)
    return a


# Versao 2: quick sort top-down recursivo com cut-off para insertion sort
def quick_sortV2(a, lo, hi, CUTOFF):
    if(hi <= lo + CUTOFF - 1):
        insertion_sort(a, lo, hi)
        return
    j = partition(a, lo, hi)
    quick_sortV2(a, lo, j-1, CUTOFF)
    quick_sortV2(a, j+1, hi, CUTOFF)


def sortV2(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV2(a, lo, hi, CUTOFF)
    return a


# Versao 3: quick sort top-down recursivo com mediana de 3.
def quick_sortV3(a, lo, hi):
    if hi <= lo: return
    if hi - lo >= 2:
        median = median_of_3(a, lo, hi)
        a[lo], a[median] = exch(a[lo], a[median])
    j = partition(a, lo, hi)
    quick_sortV3(a, lo, j-1)
    quick_sortV3(a, j+1, hi)


def sortV3(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV3(a, lo, hi)
    return a


# Versao 4: fusao das Versoes 2 e 3, isto e, usar as duas otimizacoes
def quick_sortV4(a, lo, hi, CUTOFF):
    if(hi <= lo + CUTOFF - 1):
        insertion_sort(a, lo, hi)
        return
    if hi - lo >= 2:
        median = median_of_3(a, lo, hi)
        a[lo], a[median] = exch(a[lo], a[median])
    j = partition(a, lo, hi)
    quick_sortV4(a, lo, j-1, CUTOFF)
    quick_sortV4(a, j+1, hi, CUTOFF)


def sortV4(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV4(a, lo, hi, CUTOFF)
    return a


# Versao 5: quick sort bottom-up sem nenhuma otimizacao
def quick_sortV5(a, lo, hi):
    P = PilhaListaEncadeada()
    P.push(hi)
    P.push(lo)
    while not P.is_empty():
        lo = P.pop()
        hi = P.pop()
        if (hi <= lo): continue  # Could add cutoff here
        i = partition(a, lo, hi)
        if (i-lo > hi-i):  # Test the size of sub-arrays
            P.push(i-1)
            P.push(lo)  # Push the larger one
            P.push(hi)
            P.push(i+1)  # Sort the smaller one first
        else:
            P.push(hi)
            P.push(i+1)
            P.push(i-1)
            P.push(lo)


def sortV5(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV5(a, lo, hi)
    return a


# Versao 6: altere a Versao 5 para incluir cut-off e mediana de 3
def quick_sortV6(a, lo, hi, CUTOFF):
    P = PilhaListaEncadeada()
    P.push(hi)
    P.push(lo)
    while not P.is_empty():
        lo = P.pop()
        hi = P.pop()
        if (hi <= lo):
            continue
        if (hi <= lo + CUTOFF - 1):
            insertion_sort(a, lo, hi)
            continue
        if hi - lo >= 2:
            median = median_of_3(a, lo, hi)
            a[lo], a[median] = exch(a[lo], a[median])

        i = partition(a, lo, hi)
        if (i-lo > hi-i):  # Test the size of sub-arrays
            P.push(i-1)
            P.push(lo)  # Push the larger one
            P.push(hi)
            P.push(i+1)  # Sort the smaller one first
        else:
            P.push(hi)
            P.push(i+1)
            P.push(i-1)
            P.push(lo)


def sortV6(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV6(a, lo, hi, CUTOFF)
    return a


# Versao 7: altere a melhor versao que voce obteve ate aqui para incluir o embaralhamento (shuffle) da entrada.

# Versao 8: implemente o quick sort top-down com o particionamento 3-way de Dijkstra
def quick_sortV8(a, lo, hi):
    if(hi <= lo ): return
    v = a[lo]
    lt, gt, i = lo, hi, lo
    while(i <= gt):
        if(a[i] < v):
            a[lt], a[i] = exch(a[lt], a[i])
            lt+=1
            i+=1
        elif(a[i] > v):
            a[i], a[gt] = exch(a[i], a[gt])
            gt-=1
        else:
            i+=1
    quick_sortV8(a, lo, lt-1)
    quick_sortV8(a, gt+1, hi)


def sortV8(a, lo, hi, CUTOFF, _shuffle=False):
    if _shuffle:
        shuffle(a, lo, hi)
    quick_sortV8(a, lo, hi)
    return a
