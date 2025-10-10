class Empty(Exception):
    pass

class Full(Exception):
    pass

class PilhaLista:
    # Pilha como uma lista
    # Construtor da classe PilhaLista
    def __init__(self, MaxTamPilha):
        self._pilha = [None] * MaxTamPilha # lista que conterá a pilha
        self.MaxTamPilha = MaxTamPilha
        self.TamPilha = 0

    # retorna o tamanho da pilha
    def __len__ (self):
        return self.TamPilha

    # retorna True se pilha vazia
    def is_empty(self):
        return self.TamPilha == 0

    # empilha novo elemento e
    def push(self, e):
        if self.TamPilha < self.MaxTamPilha:
            self._pilha[self.TamPilha] = e
            self.TamPilha += 1
        else:
            raise Full("Pilha cheia")

    # retorna o elemento do topo da pilha sem retirá-lo
    # exceção se pilha vazia
    def top(self):
        if self.is_empty():
            raise Empty("Pilha vazia")
        return self._pilha[self.TamPilha - 1]

    # desempilha elemento
    # excessão se pilha vazia
    def pop(self):
        if self.is_empty():
            raise Empty("Pilha vazia")
        e = self._pilha[self.TamPilha - 1]
        self.TamPilha -= 1
        return e

    def __str__(self):
        s = ""
        for i in reversed(range(self.TamPilha)):
             s += f"{i}- {self._pilha[i]}\n"
        return s


def prioridade(x):
    if x == '+': return 1
    elif x == '-': return 1
    elif x == '*': return 2
    elif x == '/': return 2
    elif x == '^': return 3
    elif x == '(': return 4 # caso particular
    elif x == ')': return 5 # caso particular
    elif x == '[': return 6 # caso particular
    elif x == ']': return 7 # caso particular
    elif x == '{': return 8 # caso particular
    elif x == '}': return 9 # caso particular
    
    else: return 0          # não é operador

abres = {'(': ')', '[': ']', '{': '}'}
fechas = {')': '(', ']': '[', '}': '{'}

def notacaoPolonesa(expressao: str):
    n = len(expressao)
    operadores = PilhaLista(n)
    posfixa = ""
    for p in expressao:
        prior = prioridade(p)
        if prior == 0:
            posfixa += p
        elif p in abres.keys():
            operadores.push(p)
        elif p in fechas.keys():
            while (not operadores.is_empty()) and operadores.top() != fechas[p]:
                posfixa += operadores.pop()
            operadores.pop()
        else:
            while (not operadores.is_empty() and
                   operadores.top() not in abres.keys() and
                   prior <= prioridade(operadores.top())):
                posfixa += operadores.pop()
            operadores.push(p)
    while not operadores.is_empty():
        posfixa += operadores.pop()
    return posfixa
