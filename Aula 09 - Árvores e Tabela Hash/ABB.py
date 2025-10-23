class ABB:
  
    def __init__ (self, raiz):
        # cria uma nova ABB com o info raiz e sem filhos
        self._info = raiz
        self._eprox = None
        self._dprox = None
    
# Insere elemento com info x na ABB h
# Elementos iguais sempre a direita
def insere(h, x):
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
        if x < v: q = q._eprox  # esquerda
        else: q = q._dprox      # direita
    # Neste ponto, p é o pai do nó a ser inserido
    # Verificar novamente se é a esquerda ou direita
    q = ABB(x)
    if x < p._info: p._eprox = q
    else: p._dprox = q
    return h

def printABB(h):
    if h is None:
        return
    printABB(h._eprox)
    print(h._info)
    printABB(h._dprox)


def insere_rec(h, x):
    if h is None:
        return ABB(x)

    if x < h._info:
        h._eprox = insere_rec(h._eprox, x)  # desce a esquerda
    else:
        h._dprox = insere_rec(h._dprox, x)  # desce a direita

    return h


def buscaNR(h, v):
    p = h
    while p is not None:
        t = p._info
        if v == t: return p # encontrou
        if v < t: p = p._eprox  # à esquerda
        else: p = p._dprox      # à direita
    # se chegou aqui é porque não encontrou
    return None


# conta elementos com info igual a v na ABB h
def conta(h, v):
    if h is None: return 0
    # verifica se conta este nó
    if v == h._info: a = 1
    else: a = 0
    # conta esta nó mais as ABBs esquerda e direita
    return a + conta(h._eprox, v) + conta(h._dprox, v)


# Faça a contagem de elementos na ABB supondo que elementos iguais estarão sempre à direita.
def conta_dir(h, v):
    if h is None: return 0
    # verifica se conta este nó
    if v == h._info: a = 1
    else: a = 0
    # conta esta nó mais as ABBs e direita
    return a + conta(h._dprox, v)


def conta_iter(h, x):
    if h is None:
        return 0

    count = 0
    p, q = h, h
    while q is not None:
        v = q._info
        p = q
        if x == v: count += 1
        if x < v: q = q._eprox  # esquerda
        else: q = q._dprox      # direita

    return count


# Implemente conta1(h) que conta o número de folhas de uma ABB
def conta1(h):
    if h is None: return 0
    if (h._eprox is None) and (h._dprox is None): a = 1
    else: a = 0
    # conta esta nó mais as ABBs esquerda e direita
    return a + conta1(h._eprox) + conta1(h._dprox)

# Implemente conta2(h) que conta o número de nós que tenham pelo menos um filho de uma ABB
def conta2(h):
    if h is None: return 0
    if (h._eprox is not None) or (h._dprox is not None): a = 1
    else: a = 0
    # conta esta nó mais as ABBs esquerda e direita
    return a + conta2(h._eprox) + conta2(h._dprox)

# Implemente conta3(h, x) que conta número de elementos com info >= x de uma ABB h
def conta3(h, v):
    if h is None:
        return 0
    if h._info >= v:
        return 1 + conta3(h._eprox, v) + conta3(h._dprox, v)
    else:
        # se for menor, só precisa olhar à direita
        return conta3(h._dprox, v)


# Implemente o percurso pré-ordem em ABB (imprime raiz, visita nó esquerdo e visita nó direito)
def pre_ordem(h):
    if h is None:
        return
    print(h._info)
    pre_ordem(h._eprox)
    pre_ordem(h._dprox)

# Implemente o percurso pós-ordem em ABB (visita nó esquerdo, visita nó direito e finalmente visita a raiz)
def pos_ordem(h):
    if h is None:
        return
    pos_ordem(h._eprox)
    pos_ordem(h._dprox)
    print(h._info)


def printABB_bonito(h, prefix="", is_left=True):
    if h is not None:
        printABB_bonito(h._dprox, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(h._info))
        printABB_bonito(h._eprox, prefix + ("    " if is_left else "│   "), True)


abb = None
for k in [4, 7, 85, 98, 4, 5, 6]:
    abb = insere(abb, k)
printABB(abb)

print("")
_abb = None
for k in [4, 7, 85, 98, 4, 5, 6]:
    _abb = insere_rec(_abb, k)
printABB(_abb)


print("")
print(buscaNR(abb, 4)._info)
print(buscaNR(abb, 8))

print("")
print("4: ", conta(abb, 4), ", 5: ", conta(abb, 5))
print("4: ", conta_dir(abb, 4), ", 5: ", conta_dir(abb, 5))
print("4: ", conta_iter(abb, 4), ", 5: ", conta_iter(abb, 5))

print("")
print("folhas: ", conta1(abb))
print("filhos: ", conta2(abb))
print(">=5: ", conta3(abb, 5))

print("")
print("")
printABB_bonito(_abb)
print("pre_ordem")
pre_ordem(_abb)
print("pos_ordem")
pos_ordem(_abb)
