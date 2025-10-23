class ABB:
    
    def __init__ (self, raiz):
        # cria uma nova ABB com o info raiz e sem filhos
        self._info = raiz
        self._eprox = None
        self._dprox = None
    

# Procura elemento com info igual a v na ABB h
# Versão recursiva
def busca(h, v):
    if h is None:
        return 0
    if v == h._info:
        return h
    elif v < h._info:
        return busca(h._eprox, v)  # desce a esquerda
    else:
        return busca(h._dprox, v)  # desce a direita


# conta elementos com info igual a v na ABB h
def conta(h, v):
    if h is None: return 0
    # verifica se conta este nó
    if v == h._info: a = 1
    else: a = 0
    # conta esta nó mais as ABBs e direita
    return a + conta(h._dprox, v)

# altura de uma ABB - raíz é altura 0
def altura(h):
    if h is None:
        return -1
    if (h._eprox is None) and (h._dprox is None):  # folha
        return 0
    else:  # tem filhos
        return 1 + max(altura(h._eprox), altura(h._dprox))

def ImprimeABBinOrder(h):
    if h is None:
        return
    ImprimeABBinOrder(h._eprox)
    print(h._info, end=" ")
    ImprimeABBinOrder(h._dprox)

def ImprimeABBpreOrder(h):
    if h is None:
        return
    print(h._info, end=" ")
    ImprimeABBpreOrder(h._eprox)
    ImprimeABBpreOrder(h._dprox)

def ImprimeABBpostOrder(h):
    if h is None:
        return
    ImprimeABBpostOrder(h._eprox)
    ImprimeABBpostOrder(h._dprox)
    print(h._info, end=" ")

def ImprimeABBinLevel(h):
    pass

def insereElementoABB(h, elemento):
    if h is None:
        return ABB(elemento)

    if elemento < h._info:
        h._eprox = insereElementoABB(h._eprox, elemento)
    elif elemento > h._info:
        h._dprox = insereElementoABB(h._dprox, elemento)

    return h

def insereElementoABBIterativo(h, x):
    # verifica se será o primeiro
    if h is None:
        h = ABB(x)
        return h
    # procura o lugar para inserir x
    # percorre a ABB até achar um nó com o filho None
    p, q = h, h
    while q is not None:
        v = q._info
        p = q
        # à esquerda ou à direita
        if x == v: return h
        elif x < v: q = q._eprox  # esquerda
        else: q = q._dprox      # direita
    # Neste ponto, p é o pai do nó a ser inserido
    # Verificar novamente se é a esquerda ou direita
    q = ABB(x)
    if x < p._info: p._eprox = q
    else: p._dprox = q
    return h


# Monta uma ABB a partir de uma lista 
# Elementos repetidos devem ficar a direita
def montaABB(a, a_len):
    abb = None
    for k in range(a_len):
        abb = insereElementoABB(abb, a[k])
    return abb


def montaABBIterativo(a, a_len):
    abb = None
    for k in range(a_len):
        abb = insereElementoABBIterativo(abb, a[k])
    return abb


def printABB_bonito(h, prefix="", is_left=True):
    if h is not None:
        printABB_bonito(h._dprox, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(h._info))
        printABB_bonito(h._eprox, prefix + ("    " if is_left else "│   "), True)


# Testes
"""
lista = [0, 1, 2, 3, 4, 5, 6]
outralista = [10, 4, 2, 30, 7, 15, 40, 27, 60, 6]
mabb = montaABB(lista, len(lista))
moabb = montaABB(outralista, len(outralista))

print("recursivo")
printABB_bonito(mabb)
printABB_bonito(moabb)

_mabb = montaABBIterativo(lista, len(lista))
_moabb = montaABBIterativo(outralista, len(outralista))

print("iterativo")
printABB_bonito(_mabb)
printABB_bonito(_moabb)
print()

print("alturas")
print(altura(mabb))
print(altura(moabb))
print()

ImprimeABBinOrder(mabb)
print()
ImprimeABBinOrder(moabb)
print()

ImprimeABBpreOrder(mabb)
print()
ImprimeABBpreOrder(moabb)
print()

ImprimeABBpostOrder(mabb)
print()
ImprimeABBpostOrder(moabb)
print()

ImprimeABBinLevel(mabb)
print()
ImprimeABBinLevel(moabb)
print()
"""