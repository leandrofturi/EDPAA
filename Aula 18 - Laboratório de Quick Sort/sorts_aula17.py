from item import less, exch


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        for k in range(i, 0, -1):
            if less(a[k-1], a[k]):
                break
            a[k], a[k-1] = exch(a[k], a[k-1])
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if less(a[j], a[k]):
                k = j
        a[i], a[k] = exch(a[i], a[k])
    return a


def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if less(a[j+1], a[j]):
                a[j+1], a[j] = exch(a[j+1], a[j])
    return a


def shaker_sort(a):
    n = len(a)
    for i in range(n // 2):
        for j in range(i, n-i-1):
            if less(a[j+1], a[j]):
                a[j+1], a[j] = exch(a[j+1], a[j])
        for j in range(n-i-2, i, -1):
            if less(a[j], a[j-1]):
                a[j], a[j-1] = exch(a[j], a[j-1])
        
    return a


def insertion_sort_lo_hi(a, lo, hi):
    for i in range(lo+1, hi+1):
        for k in range(i, lo, -1):
            if less(a[k-1], a[k]):
                break
            a[k], a[k-1] = exch(a[k], a[k-1])
    return a


# Versao 1: merge sort classico top-down recursivo sem nenhuma otimizacao
def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k]
    i,j = lo, mid+1
    for k in range(lo, hi+1): # Merge
        if(i > mid):
            a[k] = aux[j]
            j+=1
        elif(j > hi):
            a[k] = aux[i]
            i+=1
        elif(less(aux[j], aux[i])):
            a[k] = aux[j]
            j+=1
        else:
            a[k] = aux[i]
            i+=1

def merge_sortV1(a, aux, lo, hi, CUTOFF):
    if(hi <= lo):
        return
    mid = lo + (hi-lo) // 2 # Avoid overflow
    merge_sortV1(a, aux, lo, mid, CUTOFF)
    merge_sortV1(a, aux, mid+1, hi, CUTOFF)
    merge(a, aux, lo, mid, hi)

def sortV1(a, lo, hi, CUTOFF, shuffle):
    aux = [None] * len(a) # Same size and Item type as a
    merge_sortV1(a, aux, lo, hi, CUTOFF)
    return a


# Versao 2: merge sort top-down recursivo com cut-off para insertion sort. Varie o valor de cut-off a partir de 1 e determine o valor ideal para a sua implementacao.
def merge_sortV2(a, aux, lo, hi, CUTOFF):
    if(hi <= lo + CUTOFF - 1):
        insertion_sort_lo_hi(a, lo, hi)
        return
    mid = lo + (hi-lo) // 2 # Avoid overflow
    merge_sortV2(a, aux, lo, mid, CUTOFF)
    merge_sortV2(a, aux, mid+1, hi, CUTOFF)
    merge(a, aux, lo, mid, hi)

def sortV2(a, lo, hi, CUTOFF, shuffle):
    aux = [None] * len(a) # Same size and Item type as a
    merge_sortV2(a, aux, lo, hi, CUTOFF)
    return a


# Versao 3: merge sort top-down recursivo com merge skip. Implemente essa versao a partir da Versao 1, isto e, nao use cut-off.
def merge_sortV3(a, aux, lo, hi, CUTOFF):
    if(hi <= lo):
        return
    mid = lo + (hi-lo) // 2 # Avoid overflow
    merge_sortV3(a, aux, lo, mid, CUTOFF)
    merge_sortV3(a, aux, mid+1, hi, CUTOFF)
    if (~less(a[mid+1], a[mid])):
        return
    merge(a, aux, lo, mid, hi)

def sortV3(a, lo, hi, CUTOFF, shuffle):
    aux = [None] * len(a) # Same size and Item type as a
    merge_sortV3(a, aux, lo, hi, CUTOFF)
    return a


# Versao 4: fusao das Versoes 2 e 3, isto e, usar as duas otimizacoes: cut-off e merge skip.
def merge_sortV4(a, aux, lo, hi, CUTOFF):
    if(hi <= lo + CUTOFF - 1):
        insertion_sort_lo_hi(a, lo, hi)
        return
    mid = lo + (hi-lo) // 2 # Avoid overflow
    merge_sortV4(a, aux, lo, mid, CUTOFF)
    merge_sortV4(a, aux, mid+1, hi, CUTOFF)
    if (~less(a[mid+1], a[mid])):
        return
    merge(a, aux, lo, mid, hi)

def sortV4(a, lo, hi, CUTOFF, shuffle):
    aux = [None] * len(a) # Same size and Item type as a
    merge_sortV4(a, aux, lo, hi, CUTOFF)
    return a


# Versao 5: merge sort bottom-up sem nenhuma otimizacao. (Veja o slide 19 da Aula 15.)
def sortV5(a, lo, hi, CUTOFF, shuffle):
    n = len(a)
    y = n -1
    aux = [None] * n # Same size and Item type as a
    sz = 1
    while sz < n:
        for aux_lo in range(0, n-sz, 2*sz):
            x = lo + 2*sz - 1
            merge(a, aux, aux_lo, aux_lo+sz-1, min(x,y))
        sz = 2*sz
    return a


# Versao 6: altere a Versao 5 para implementar o que seria o cut-off na versao bottom-up.
def sortV6(a, lo, hi, CUTOFF, shuffle):
    n = len(a)
    y = n -1
    aux = [None] * n # Same size and Item type as a
    sz = 1
    while sz < n:
        for aux_lo in range(0, n-sz, 2*sz):
            aux_hi = aux_lo+sz-1
            if(aux_hi <= aux_lo + CUTOFF - 1):
                insertion_sort_lo_hi(a, aux_lo, aux_hi)
            else:
                x = lo + 2*sz - 1
                merge(a, aux, aux_lo, aux_lo+sz-1, min(x,y))
        sz = 2*sz
    return a


# Versao 7: altere a Versao 6 para implementar o merge skip na versao bottom-up.
def sortV7(a, lo, hi, CUTOFF, shuffle):
    n = len(a)
    y = n -1
    aux = [None] * n # Same size and Item type as a
    sz = 1
    while sz < n:
        for aux_lo in range(0, n-sz, 2*sz):
            mid = aux_lo+sz-1
            if (~less(a[mid+1], a[mid])):
                continue
            x = lo + 2*sz - 1
            merge(a, aux, aux_lo, aux_lo+sz-1, min(x,y))
        sz = 2*sz
    return a
