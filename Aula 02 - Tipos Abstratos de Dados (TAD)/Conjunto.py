def Elimina_Repetidos(lista):
    nova_lista = []
    for k in range(0, len(lista)):
        tem_rep = False
        # procura lista[k] nos elementos à frente
        for j in range(k + 1, len(lista)):
            if lista[k] == lista[j]:
                tem_rep = True
                break
        # se não tem repetidos inclua na nova lista
        if not tem_rep: nova_lista.append(lista[k])
    return nova_lista


def Elimina_Repetidos_set(lista):
    return list(set(lista))


def Elimina_Repetidos_dict(lista):
    return list(dict.fromkeys(lista))


def Elimina_Repetidos_list_set(lista):
    vistos = set()
    # x in vistos retorna True se o elemento x já foi visto
    # vistos.add(x) adiciona x ao conjunto vistos e retorna None
    nova_lista = [x for x in lista if not (x in vistos or vistos.add(x))]
    return nova_lista


class Conjunto:
    # Define a classe Conjunto
    
    # Construtor da classe
    def __init__(self, lista = []):
        # Cria uma instância de Conjunto
        self.lset = Elimina_Repetidos(lista)
        self.lset.sort()
   
    # união (+)
    def __add__(s1, s2):
        # cria Conjunto com a concatenação de duas listas
        return Conjunto(s1.lset + s2.lset)

    # intersecção (*)
    def __mul__(s1, s2):
        # cria Conjunto com a intersecção de duas listas
        inter = [x for x in s1.lset if x in s2.lset]
        return Conjunto(inter)
    
    # diferença (-)
    def __sub__(s1, s2):
        # cria Conjunto com a diferença de duas listas
        diff = [x for x in s1.lset if x not in s2.lset]
        return Conjunto(diff)
    
    # Tamanho do Conjunto
    def __len__(self):
        return len(self.lset)

    # Transforma elemento da classe em str para o print
    # Mostrar um '*' na frente para diferenciar do print(lista)
    def __str__(self):
        return '*' + str(self.lset)
    
    # está contido (<)
    def __lt__(s1, s2):
        return all(x in s2.lset for x in s1.lset)

    # contém (>)
    def __gt__(s1, s2):
        return s2.__lt__(s1)

    # igual (==)
    def __eq__(s1, s2):
        s1_cpy = sorted(s1.lset)
        s2_cpy = sorted(s2.lset)
        return (
            len(s1_cpy) == len(s2_cpy) and
            all([s1_cpy[i] == s2_cpy[i] for i in range(len(s1_cpy))])
        )
    
    # pertinência (in)
    def __contains__(self, x):
        return x in self.lset
    
    # inclusão (+=)
    def __iadd__(self, x):
        if not self.__contains__(x):
            self.lset.append(x)
            self.lset.sort()
        return self

    # exclusão (-=)
    def __isub__(self, x):
        if self.__contains__(x):
            self.lset.remove(x)
        return self
