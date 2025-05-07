'''2 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar'''

# Programa para verificar se um número é par ou ímpar

# Solicita um número ao usuário e converte para inteiro
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2
if numero % 2 == 0:
    # Se o resto da divisão for 0, o número é par
    print("O número é par.")
else:
    # Caso contrário, o número é ímpar
    print("O número é ímpar.")
