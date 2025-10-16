from pilha import PilhaLista, Empty, UnknownOperator

def prioridade(x):
    if x == '+': return 1
    elif x == '-': return 1
    elif x == '*': return 2
    elif x == '/': return 2
    elif x == '^': return 3
    elif x == '(': return 4 # caso particular
    elif x == ')': return 5 # caso particular
    else: return 0          # não é operador


# Transformação de in-fixa para pós-fixa

'''
Função que recebe uma expressão em notação in-fixa e retorna sua correspondente em notação 
pós-fixa. As expressões de entrada e saída são descritas como uma lista de strings.

@param inFixa: Lista de strings com a entrada -- expressão na notação in-fixa
@return posFixa: Lista de strings com a saída em notação pós-fixa
'''
def fromInToPos(inFixa):
    operadores = PilhaLista()
    posFixa = ""

    for p in inFixa.split(" "):
        if p == " ":
            continue
        priority = prioridade(p)

        if priority == 0:
            posFixa += " " + p
        elif p == "(":
            operadores.push(p)
        elif p == ")":
            while (not operadores.is_empty()) and operadores.top() != "(":
                posFixa += " " + operadores.pop()
            operadores.pop()  # (
        else:
            while (not operadores.is_empty() and
                   operadores.top() != "(" and
                   priority <= prioridade(operadores.top())):
                posFixa += " " + operadores.pop()
            operadores.push(p)

    while not operadores.is_empty():
        posFixa += " " + operadores.pop()
    
    return posFixa.strip()

'''
Função que recebe uma expressão em notação pós-fixa e retorna a sua resolução matemática.

@param posFixa: Lista de strings com a entrada -- expressão na notação pós-fixa
@return resultado: valor final da expressão, após sua resolução.
'''
def solvePosFixa(posFixa):
    operandos = PilhaLista()

    for p in posFixa.split(" "):
        priority = prioridade(p)

        if priority == 0:
            operandos.push(p)
        
        #elif priority == 1:
        #    e1 = float(operandos.pop())
        #    if p == "+": r = +e1
        #    elif p == "-": r = -e1
        #    operandos.push(str(r))

        else:
            e1 = float(operandos.pop())
            e2 = float(operandos.pop())
            if p == '+': r = e2 + e1
            elif p == '-': r = e2 - e1
            elif p == '*': r = e2 * e1
            elif p == '/': r = e2 / e1
            elif p == '^': r = e2 ^ e1

            operandos.push(str(r))

    return operandos.pop()
        
     
def main():
    # exemplos de entrada
    inFixa = "12 + ( 13 - 4 * 2 ) * 15" # resultado = 87
    inFixa = "12 + 13 - 4 * 2 * 15" # resultado = -95
    # inFixa = "a * (b + c * (d + e))"


    # transforma a string de entrada em lista de strings

    # chamada da transformação de notações (in-fixa -> pós-fixa)
    posFixa = fromInToPos(inFixa)

    # impressão das notações em formato de string
    print("Notação in-fixa: ", "".join(inFixa))
    print("Notação pós-fixa: ", "".join(posFixa))

    # resolução da equação em notação pós-fixa
    print(solvePosFixa(posFixa))

main()