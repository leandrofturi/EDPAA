def less(A, B):
    return A < B

def exch(A, B):
    C = A
    A = B
    B = C
    return (A, B)

def compexch(A, B):
    if less(A, B):
        A, B = exch(A, B)
    return A, B
