class Empty(Exception):
    pass

class FilaListaEncadeada:
    
    # implementa uma fila usando uma LE simples

    # classe _Node - interna
    class _Node:

        __slots__ = '_info', '_prox'
        
        def __init__ (self, info, prox):
            # inicia os campos
            self._info = info
            self._prox = prox

    # métodos de fila
    def __init__ (self):
        # cria uma fila vazia
        self._inicio = None # vazia
        self._final = None  # vazia
        self._tamanho = 0   # tamanho da pilha
        
    def __len__(self):
        # retorna o tamanho da fila
        pass

    def is_empty(self):
        # retorna True se fila vazia
        pass
    

    def first(self):
        # retorna sem remover o inicio da fila.
        # sinaliza exceção se fila vazia
        pass

    def enqueue(self, e):
        # adiciona elemento ao final da fila
        pass   
                    
    def dequeue(self):
        # remove e retorna o elmento do inicio da fila
        # sinaliza exceção se fila vazia
        pass

    def ImprimeFila(self):
        pass

''' 
Testes

# Cria uma fila em lista encadeada
F = FilaListaEncadeada()
# adiciona 10 elementos
for k in range(10): F.enqueue(k)
F.ImprimeLE()
# remove 6 elementos
for k in range(6): F.dequeue()
F.ImprimeFila()
# algumas informações da fila
print("\nprimeiro elemento da fila = ", F.first())
print("tamanho da fila = ", len(F))
# remove 6 elementos - vai dar exceção
for k in range(6): F.dequeue()
'''