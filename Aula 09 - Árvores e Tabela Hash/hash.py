# basal ########################################################################
def hash(x):
    return x % 10

def insere(a, x):
    a[hash(x)] = x

def busca_hash(a, x):
    k = hash(x)
    if a[k] == x: return k
    return –1;


# extendida ####################################################################
def hash(x, M):
    return x % M

def insere_hash(a, x):
    M = len(a)
    cont = 0
    i = hash(x, M)
    # procura a próxima posição livre
    while a[i] != None:
        if a[i] == x: return -1 # valor já existente na tabela
        cont += 1               # conta os elementos da tabela
        if cont == M: return -2 # tabela cheia
        i = (i + 1) % M         # tabela circular
    # achamos uma posição livre - coloque x nesta posição
    a[i] = x
    return i

def busca_hash(a, x):
    M = len(a)
    cont = 0
    i = hash(x, M)
    # procura x a partir da posição i
    while a[i] != x:
        if a[i] == None: return -1  # não achou x, pois há uma vazia
        cont += 1                   # conta os elementos da tabela
        if cont == M: return -2;    # a tabela está cheia
        i = (i + 1) % M             # tabela circular


