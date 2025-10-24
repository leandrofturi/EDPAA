class Empty(Exception):
    pass

class PilhaListaEncadeada:
    
    # implementa uma pilha usando uma LE simples

    # classe _Node - interna
    class _Node:

        __slots__ = '_info', '_prox'
        
        def __init__ (self, info, prox):
            # inicia os campos
            self._info = info
            self._prox = prox
    
    # métodos de pilha
    def __init__ (self):
        # cria uma pilha vazia
        self._topo = None # vazia
        self._tamanho = 0 # tamanho da pilha
        
    def __len__(self):
        # retorna o tamanho da pilha
        return self._tamanho

    def is_empty(self):
        # retorna True se pilha vazia
        return self.__len__() == 0

    def push(self, e):
        # adiciona elemento ao topo da pilha
        novo = self._Node(e, self._topo)
        self._topo = novo
        self._tamanho += 1

    def top(self):
        # retorna sem remover o topo da pilha
        # sinaliza exceção se pilha vazia
        if self.is_empty():
            raise Empty("Lista encadeada Vazia")
        return self._topo._info
                    
    def pop(self):
        # remove e retorna o topo da pilha
        # sinaliza exceção se pilha vazia
        if self.is_empty():
            raise Empty("Lista encadeada Vazia")
        e = self._topo
        self._topo = e._prox
        self._tamanho -= 1
        return e._info
        
    def ImprimePilha(self):
        p = self._topo
        while p is not None:
            print(p._info, end=" ")
            p = p._prox
        print()

'''
Testes

# Cria uma pilha
P = PilhaListaEncadeada()
# adiciona 10 elementos
for k in range(10): P.push(k)
P.ImprimePilha()
# remove 5 elementos
for k in range(5): P.pop()
P.ImprimePilha()
# algumas informações da pilha
print("\ntopo da pilha = ", P.top())
print("tamanho da pilha = ", len(P))
# remove 6 elementos - vai dar excessão
for k in range(6): P.pop()
'''