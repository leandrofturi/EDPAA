import sys

from ABB import (
    busca, conta, insereElementoABB, altura, printABB_bonito,
    ImprimeABBinLevel, ImprimeABBinOrder, ImprimeABBpreOrder, ImprimeABBpostOrder, 
    ImprimeABBinLevelTAD, ImprimeABBinOrderTAD, ImprimeABBpreOrderTAD, ImprimeABBpostOrderTAD, 
)

from random import randint

n_args = len(sys.argv)

def main():
    # print("Total arguments passed:", n_args)
    # for i in range(n_args):
    #     # verificação de cada argumento de sys.argv
    #    print(sys.argv[i])

    abb = None
    for i in range(int(sys.argv[n_args-1])):
        # geração de n valores aleatórios no intervalo [0-999]
        abb = insereElementoABB(abb, randint(0,1000))
        # árvore deve ser gerada/populada
    
    print("\n")
    if int(sys.argv[n_args-1]) < 10:
        printABB_bonito(abb)
    print("\n")
    print("altura: ", altura(abb))
    print()

    print("inOrder: ")
    ImprimeABBinOrder(abb); print()
    ImprimeABBinOrderTAD(abb)
    print("\n")
    
    print("preOrder: ")
    ImprimeABBpreOrder(abb); print()
    ImprimeABBpreOrderTAD(abb)
    print("\n")

    print("postOrder: ")
    ImprimeABBpostOrder(abb); print()
    ImprimeABBpostOrderTAD(abb)
    print("\n")

    print("inLevel: ")
    ImprimeABBinLevel(abb); print()
    ImprimeABBinLevelTAD(abb)
    print("\n")


    abb = None
    for i in ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']:
        # geração de n valores aleatórios no intervalo [0-999]
        abb = insereElementoABB(abb, i)
        # árvore deve ser gerada/populada
    
    print("\n")
    if int(sys.argv[n_args-1]) < 10:
        printABB_bonito(abb)
    print("\n")
    print("altura: ", altura(abb))
    print()

    print("inOrder: ")
    ImprimeABBinOrder(abb); print()
    ImprimeABBinOrderTAD(abb)
    print("\n")
    
    print("preOrder: ")
    ImprimeABBpreOrder(abb); print()
    ImprimeABBpreOrderTAD(abb)
    print("\n")

    print("postOrder: ")
    ImprimeABBpostOrder(abb); print()
    ImprimeABBpostOrderTAD(abb)
    print("\n")

    print("inLevel: ")
    ImprimeABBinLevel(abb); print()
    ImprimeABBinLevelTAD(abb)
    print("\n")

main()