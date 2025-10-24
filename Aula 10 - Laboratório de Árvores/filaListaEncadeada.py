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
        return self._tamanho

    def is_empty(self):
        # retorna True se fila vazia
        return self.__len__() == 0
    

    def first(self):
        # retorna sem remover o inicio da fila.
        # sinaliza exceção se fila vazia
        if self.is_empty():
            raise Empty("Lista encadeada Vazia")
        return self._inicio._info

    def enqueue(self, e):
        # adiciona elemento ao final da fila
        novo = self._Node(e, None)
        if self.is_empty():
            self._inicio = self._final = novo
        else:
            self._final._prox = novo
            self._final = novo
        self._tamanho += 1

    def dequeue(self):
        # remove e retorna o elmento do inicio da fila
        # sinaliza exceção se fila vazia
        if self.is_empty():
            raise Empty("Lista encadeada Vazia")
        e = self._inicio
        self._inicio = e._prox
        self._tamanho -= 1
        if self.is_empty():
            self._inicio = self._final = None
        return e._info

    def ImprimeFila(self):
        p = self._inicio
        while p is not None:
            print(p._info, end=" ")
            p = p._prox
        print()

''' 
Testes

# Cria uma fila em lista encadeada
F = FilaListaEncadeada()
# adiciona 10 elementos
for k in range(10): F.enqueue(k)
F.ImprimeFila()
# remove 6 elementos
for k in range(6): F.dequeue()
F.ImprimeFila()
# algumas informações da fila
print("\nprimeiro elemento da fila = ", F.first())
print("tamanho da fila = ", len(F))
# remove 6 elementos - vai dar exceção
for k in range(6): F.dequeue()
'''