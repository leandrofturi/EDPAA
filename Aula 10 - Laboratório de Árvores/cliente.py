import sys

from ABB import busca, conta, insereElementoABB 
from ABB import ImprimeABBinLevel, ImprimeABBinOrder, ImprimeABBpreOrder, ImprimeABBpostOrder, altura, printABB_bonito
from filaListaEncadeada import FilaListaEncadeada
from pilhaListaEncadeada import PilhaListaEncadeada
from random import randint

n_args = len(sys.argv)

def main():
    print("Total arguments passed:", n_args)
    for i in range(n_args):
        # verificação de cada argumento de sys.argv
        print(sys.argv[i])

    abb = None
    for i in range(int(sys.argv[n_args-1])):
        # geração de n valores aleatórios no intervalo [0-999]
        abb = insereElementoABB(abb, randint(0,1000))
        # árvore deve ser gerada/populada
    
    print()
    if int(sys.argv[n_args-1]) < 10:
        printABB_bonito(abb)
    print("altura: ", altura(abb))

    print("inOrder: ", end=" ")
    ImprimeABBinOrder(abb)
    print()
    
    print("preOrder: ", end=" ")
    ImprimeABBpreOrder(abb)
    print()

    print("postOrder: ", end=" ")
    ImprimeABBpostOrder(abb)
    print()

    print("inLevel: ", end=" ")
    ImprimeABBinLevel(abb)
    print()

main()