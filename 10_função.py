# Define a função que recebe um número e retorna seu quadrado
def quadrado(numero):
    return numero ** 2  # ou: numero * numero

# Solicita ao usuário que digite um número
entrada = float(input("Digite um número: "))

# Chama a função passando o número digitado e armazena o resultado
resultado = quadrado(entrada)

# Exibe o resultado
print("O quadrado de", entrada, "é", resultado)