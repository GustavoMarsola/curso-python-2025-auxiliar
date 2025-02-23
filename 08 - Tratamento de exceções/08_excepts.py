# Em python, exceções são erros que ocorrem durante a execução de um programa.
# Podemos tratar exceções com blocos try/except/else/finally.

# try     - Bloco de código que pode gerar exceções
# except  - Bloco de código que trata exceções
# else    - Bloco de código que é executado se não ocorrer exceções
# finally - Bloco de código que é sempre executado

# Exemplo:

try:
    # Código que pode gerar exceções
    numero = 10 / 0.0
    print(numero)
except ZeroDivisionError as ex:
    # Tratamento da exceção
    print(f"Erro: {ex}")
else:
    # Código que é executado se não ocorrer exceções
    print("Tudo certo!")
finally:
    # Código que é sempre executado
    print("Fim do bloco")


# Podemos tratar várias exceções em um mesmo bloco try/except
try:
    # Código que pode gerar exceções
    numero = 10 / 0.0
    print(numero)
except ZeroDivisionError as ex:
    # Tratamento da exceção
    print(f"Erro: {ex}")
except TypeError as ex:
    # Tratamento da exceção
    print(f"Erro: {ex}")
else:
    # Código que é executado se não ocorrer exceções
    print("Tudo certo!")
finally:
    # Código que é sempre executado
    print("Fim do bloco")