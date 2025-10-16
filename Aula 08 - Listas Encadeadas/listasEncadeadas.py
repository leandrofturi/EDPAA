class Empty(Exception):
    pass


class ListaEncadeadaSimples:
    
    # Implementa uma LE simples

    # classe _Node - interna
    class _Node:

        __slots__ = '_info', '_prox'
        
        def __init__ (self, info, prox):
            # inicia os campos
            self._info = info
            self._prox = prox

    # métodos de LE

    def __init__ (self):
        # cria uma fila vazia
        self._inicio = None # vazia
        self._tamanho = 0   # tamanho da LE
        
    def __len__(self):
        # retorna o tamanho da LE
        return self._tamanho

    def is_empty(self):
        # retorna True se LE vazia
        return self._tamanho == 0
    
    def first(self):
        # retorna o campo info da LE sem remover
        # sinaliza exceção se LE vazia
        if self.is_empty():
            raise Empty("Lista encadeada Vazia")
        return self._inicio._info # elemento inicial da LE

    def adiciona(self, e):
        # adiciona elemento no inicio da LE
        # novo nó referencia o inicio da LE
        novo = self._Node(e, self._inicio)
        # novo nó será o inicio da LE
        self._inicio = novo
        self._tamanho += 1

    def adiciona_afrente(self, p, e):
        # adiciona elemento a frente de p
        # novo nó referencia o mesmo que p
        novo = self._Node(e, p._prox)
        # p referencia o novo nó
        p._prox = novo
        self._tamanho += 1
        
    def remove_afrente(self, p):
        # remove elemento a frente de p
        # caso particular - p não pode ser o último
        if p._prox is None:
            raise Empty("Nó inexistente") 
        # p referencia o mesmo que o próximo
        p._prox = p._prox._prox
        self._tamanho -= 1

    def busca(self, e):
        # procura elemento com info = e
        # devolve referência para esse elemento ou None
        # p percorre a lista
        p = self._inicio
        while p is not None:
            if p._info == e: return p # achou
            p = p._prox # vai para o próximo
        # se chegou aqui é porque não achou
        return None        

    def Procura(self, e):
        return self.busca(e)

    def busca_ant(self, e):
        # procura elemento com info = e
        # devolve uma dupla de referências (p_ant, p)
        # p percorre a lista e pant referencia o anterior
        pant, p = None, self._inicio
        while p is not None:
            if p._info == e:
                return pant, p
            pant, p = p, p._prox
        return pant, p

    def CriaLE(self, vet):
        # cria uma LE com elementos do vetor vet
        for k in range(len(vet) - 1, -1, -1):
            self.adiciona(vet[k])
  
    def ImprimeLE(self):
        # só para teste
        p = self._inicio
        k = 1
        print("Imprimindo a lista encadeada:")
        while p is not None:
            print(k, " - ", p._info)
            k = k + 1
            p = p._prox

    def busca_maior(self, e):
        pant, p = None, self._inicio
        while p is not None:
            if p._info > e:
                return pant, p
            pant, p = p, p._prox
        return pant, p

    def Adiciona_emOrdem(self, e):
        # Supondo que os nós estão em ordem crescente 
        # pelo campo info, faça uma função 
        # Adiciona_emOrdem(x) que adiciona um novo nó com 
        # info igual a x, mantendo a ordem. 
        # Para isso é necessário procurar o primeiro nó 
        # com info maior que x, mas guardar a referência 
        # ao nó anterior para que possa inserir o novo nó 
        # à frente dele.
        pant, _ = self.busca_maior(e)
        self.adiciona_afrente(pant, e)
        pass
    
    def Conta(self, e):
        # Função Conta(x) que devolve a quantidade de nós 
        # com info = x.
        count = 0
        p = self._inicio
        while p is not None:
            if p._info == e: count += 1
            p = p._prox
        return count

    def ComparaLE(self, LEX):
        # Função ComparaLE(LEX) que compara o conteúdo 
        # (campo info) de uma lista encadeada com a lista 
        # encadeada LEX. Neste caso, para se comparar a 
        # lista encadeada LX com a LEX o comando será 
        # LX.Compara(LEX). Outra forma seria escrever a 
        # função com 2 parâmetros: Compara(LX, LEX). 
        # Faça das duas formas. As funções devem retornar 
        # se as listas são iguais ou diferentes.
        if self.is_empty() and LEX.is_empty():
            return True
        elif not self.is_empty() and LEX.is_empty():
            return False
        elif self.is_empty() and not LEX.is_empty():
            return False
        p = self._inicio
        q = LEX._inicio
        while (p is not None) and (q is not None):
            if p._info != q._info: return False
            p = p._prox
            q = q._prox
        return True

def Compara(LE, LEX):
    # Função ComparaLE(LEX) que compara o conteúdo 
    # (campo info) de uma lista encadeada com a lista 
    # encadeada LEX. Neste caso, para se comparar a 
    # lista encadeada LX com a LEX o comando será 
    # LX.Compara(LEX). Outra forma seria escrever a 
    # função com 2 parâmetros: Compara(LX, LEX). 
    # Faça das duas formas. As funções devem retornar 
    # se as listas são iguais ou diferentes.
    if LE.is_empty() and LEX.is_empty():
        return True
    elif not LE.is_empty() and LEX.is_empty():
        return False
    elif LE.is_empty() and not LEX.is_empty():
        return False
    p = LE._inicio
    q = LEX._inicio
    while (p is not None) and (q is not None):
        if p._info != q._info: return False
        p = p._prox
        q = q._prox
    return True


numeros = [1,1,2,4,5]
LEC = ListaEncadeadaSimples()
LEC.CriaLE(numeros)
LEC.Adiciona_emOrdem(7)
LEC.ImprimeLE()
LEC.Adiciona_emOrdem(3)
LEC.ImprimeLE()
print("Igual a 1: ", LEC.Conta(1))
print("Igual a mesma: ", LEC.ComparaLE(LEC))
print("Igual a vazia: ", LEC.ComparaLE(ListaEncadeadaSimples()))
cores = ["vermelho", "preto", "azul", "amarelo", "verde", "branco"]
LEC_cores = ListaEncadeadaSimples()
LEC_cores.CriaLE(cores)
print("Igual a cores: ", LEC.ComparaLE(LEC_cores))
print("Igual a cores: ", Compara(LEC, LEC_cores))

# Cria lista encadeada
cores = ["vermelho", "preto", "azul", "amarelo", "verde", "branco"]
LEC = ListaEncadeadaSimples()
LEC.CriaLE(cores)
LEC.ImprimeLE()

# Verifica se algumas cores estão na lista
while True:
    cor = input("\nEntre com o nome da cor:")
    if cor == 'fim': break
    if LEC.busca(cor) is None:
        print("A cor", cor, "não está na lista encadeada")
    else:
        print("Encontrada a cor", cor, "na lista encadeada")

print("\nAdicionando laranja e violeta depois e antes da azul")





# Adicionar cor laranja a frente do azul
anterior, atual = LEC.busca_ant("azul")
if atual is None:
    print("Cor azul não está na lista")
else:
    LEC.adiciona_afrente(atual, "laranja")

# Adicionar cor violeta antes da azul
if anterior is None:
    print("Cor azul não tem anterior")
else:
    LEC.adiciona_afrente(anterior, "violeta")

LEC.ImprimeLE()

print("\nRemovendo as cores amarelo e lilás da lista")

# Remove cor amarelo
anterior, atual = LEC.busca_ant("amarelo")
if atual is None or anterior is None:
    print("Cor amarelo não está na lista ou não tem anterior")
else:
    LEC.remove_afrente(anterior)

# Remove cor lilas
anterior, atual = LEC.busca_ant("lilas")
if atual is None or anterior is None:
    print("Cor lilas não está na lista ou não tem anterior")
else:
    LEC.remove_afrente(anterior)
    
LEC.ImprimeLE()

# teste de len e first
print("\nTamanho da LE = ", len(LEC))
print("\nPrimeiro elemento da LE = ", LEC.first())