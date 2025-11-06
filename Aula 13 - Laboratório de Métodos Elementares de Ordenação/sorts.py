from item import less, exch, compexch


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
