# Função que recebe um número e retorna o dobro
def dobrar(numero):
    return numero * 2

# Solicita um número ao usuário e converte para float (para aceitar decimais também)
entrada = float(input("Digite um número: "))

# Chama a função 'dobrar' com o número fornecido pelo usuário
resultado = dobrar(entrada)

# Exibe o resultado
print("O dobro do número é:", resultado)