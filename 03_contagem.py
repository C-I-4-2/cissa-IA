# Solicita ao usuário um número inteiro para iniciar a contagem regressiva
numero = int(input("Digite um número para iniciar a contagem regressiva: "))

# Inicia a contagem regressiva até 0
for i in range(numero, -1, -1):  # Começa no número, vai até 0 (inclusive), decrementando de 1 em 1
    print(i)  # Exibe o número atual da contagem

# Mensagem final
print("FIM!")