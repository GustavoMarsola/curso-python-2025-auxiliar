# Palavra chave para definir uma função é def
# Uma função pode ter parâmetros ou não
# Uma função pode retornar um valor ou não
# É possível definir os tipos de dados dos parâmetros e do retorno da função
# Bem como o tipo de dados que a função retorna
# Também é uma boa prática fornecer uma descrição da função
# Quando você não deixa explícito o retorno da função, ela retorna None (nulo)


def somar_valores(valor1: int|float, valor2: int|float) -> int|float:
    """
    Retorna a soma de dois valores
    
    valor1: int|float - Primeiro valor a ser somado
    valor2: int|float - Segundo valor a ser somado
    
    return int|float - Retorna a soma dos valores
    """
    soma = valor1 + valor2
    return soma


# Uma função também pode ter parâmetros estritamente posicionais
# Neste caso, é possível passar n valores
# O *args é uma sequência de valores
# Neste caso, a ordem dos valores importa !


def multiplicar_valores(*args) -> int|float:
    """
    Retorna a multiplicação de n valores
    """
    multiplicacao = 1
    for valor in args:
        multiplicacao *= valor
    return multiplicacao

# Uma função também pode ter parâmetros estritamente nomeados

def dividir_valores(**kwargs) -> int|float:
    """
    Retorna a divisão de dois valores
    
    dividendo: int|float - Valor a ser dividido
    divisor:   int|float - Por quanto o valor será dividido
    
    return int|float - Retorna a divisão dos valores
    """
    dividendo = kwargs.get("dividendo")
    divisor   = kwargs.get("divisor")
    divisao   = dividendo / divisor
    return divisao

