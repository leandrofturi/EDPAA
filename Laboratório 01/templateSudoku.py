''' 
    Função que busca um espaço vazio no Grid do Sudoku (posição == 0) e returna a posição livre
    Caso não encontre uma posição livre no Grid, retorna False

    @input grid: Grid do sudoku
    @input r: número de linhas do Grid do sudoku
    @input c: número de colunas do Grid do sudoku
    @return row,col: posição válida ainda não preenchida do Grid
'''
def encontraPosicaoValida(grid, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                return i, j
    return False

'''
    Função que verifica se um número candidato pode ser utilizado na posição do Grid do Sudoku.
    Deve-se verificar a existência do candidato passado na linha, coluna e região (n x n) do Grid.

    @param grid: Grid do sudoku
    @param num: número candidato a ser colocado na posição do Grid
    @param row: linha em que o número será preenchido no Grid
    @param col: coluna em que o número será preenchido no Grid
    @param dim: dimensão do Grid do Sudoku

    @return: True se o candidato pode ser utilizado na posição ou False caso contrário
'''
def verificaCandidatoPosicaoValida(grid, num, row, col, dim):
    # Verificar se a linha inclui o número candidato
    # Verificar se a coluna inclui o número cadidato
    block_size = int(dim**(0.5))
    for k in range(dim):
        if grid[row][k] == num:
            return False
        if grid[k][col] == num:
            return False

    # Verificar se o número já está incluído no bloco individual do Grid
    block_row = (row // block_size)*block_size
    block_col = (col // block_size)*block_size
    for i in range(block_size):
        for j in range(block_size):
            if grid[block_row + i][block_col + j] == num:
                return False
    
    return True

'''
    Função de solução do Sudoku. Deve buscar uma nova posição válida, e caso esta não exista, retornar True
    pois todas as células já foram preenchidas no Grid.
    Caso contrário, deve resolver o problema verificando possíveis candidatos para a posição não visitada 
    encontrada (posição válida).

    Para cada possível candidato (permutação de 1, ..., n) deve-se verificar a validade deste para a posição válida.
    Se o número candidato for válido para a posição, deve-se atualizar o conteúdo do Grid com este número e prosseguir
    com a resolução do problema para a próxima posição válida a ser preenchida (de forma recursiva), retornando
    True sempre que um novo candidato pode ser colocado no Grid para esta possível solução (princípio do backtracking).

    Caso contrário (algum possível candidato da solução candidata não atende aos requisitos de preenchimento do Grid)
    a função de solução do Sudoku deve retornar False após reestabelecer o valor 0 para a posição válida do Grid.

    @param grid: Grid do sudoku
    @param dimSudoku: dimensão total do tabuleiro (linhas x colunas) do Sudoku

    @return: True se houver solução e False caso contrário
'''
def resolveSudoku(grid, dimSudoku):
    pos = encontraPosicaoValida(grid, dimSudoku, dimSudoku)
    if pos == False:
        return True
    
    row = pos[0]
    col = pos[1]
    for num in range(1, dimSudoku+1):
        if verificaCandidatoPosicaoValida(grid, num, row, col, dimSudoku):
            grid[row][col] = num
            if resolveSudoku(grid, dimSudoku):
                return True
            grid[row][col] = 0
    
    return False

def main():
    dimSudoku = 9

    # Exemplo de entrada do Grid do Sudoku - entrada 3x3 -> 9x9
    # 0 -> posições não preenchidas

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    '''
    Output
    [3, 1, 6, 5, 0, 8, 4, 0, 0]
    [5, 2, 9, 0, 0, 0, 0, 0, 0]
    [4, 8, 7, 0, 0, 0, 0, 3, 1]
    [0, 0, 3, 0, 1, 0, 0, 8, 0]
    [9, 0, 0, 8, 6, 3, 0, 0, 5]
    [0, 5, 0, 0, 9, 0, 6, 0, 0]
    [1, 3, 0, 0, 0, 0, 2, 5, 0]
    [0, 0, 0, 0, 0, 0, 0, 7, 4]
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
    '''
    
    # Chamada de solução do Sudoku - deve alterar o Grid com a solução
    if (resolveSudoku(grid, dimSudoku)):
        for i in grid:
            print(i)
    else:
        print("Não existe solução!")


    dimSudoku = 4

    grid = [[1, 0, 0, 0],
            [0, 0, 3, 4],
            [0, 0, 0, 0],
            [0, 3, 0, 1]]

    '''
    Exemplo 2:
    [1, 0, 0, 0]
    [0, 0, 3, 4]
    [0, 0, 0, 0]
    [0, 3, 0, 1]
     -> Não existe solução!.
    '''
    
    # Chamada de solução do Sudoku - deve alterar o Grid com a solução
    if (resolveSudoku(grid, dimSudoku)):
        for i in grid:
            print(i)
    else:
        print("Não existe solução!")
    
main()