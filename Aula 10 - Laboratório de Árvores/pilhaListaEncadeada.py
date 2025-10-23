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
        pass

    def is_empty(self):
        # retorna True se pilha vazia
        pass

    def push(self, e):
        # adiciona elemento ao topo da pilha
        pass

    def top(self):
        # retorna sem remover o topo da pilha
        # sinaliza exceção se pilha vazia
        pass
                    
    def pop(self):
        # remove e retorna o topo da pilha
        # sinaliza exceção se pilha vazia
        pass
        
    def ImprimePilha(self):
        pass


'''
Testes

# Cria uma pilha
P = PilhaListaEncadeada()
# adiciona 10 elementos
for k in range(10): P.push(k)
P.ImprimeLE()
# remove 5 elementos
for k in range(5): P.pop()
P.ImprimePilha()
# algumas informações da pilha
print("\ntopo da pilha = ", P.top())
print("tamanho da pilha = ", len(P))
# remove 6 elementos - vai dar excessão
for k in range(6): P.pop()
'''