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
except ZeroDivisionError as e:
    # Tratamento da exceção
    print(f"Erro: {e}")
else:
    # Código que é executado se não ocorrer exceções
    print("Tudo certo!")
finally:
    # Código que é sempre executado
    print("Fim do bloco")