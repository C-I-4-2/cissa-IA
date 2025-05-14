import random

# O computador escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

print("Eu escolhi um número entre 1 e 10. Tente adivinhar!")

# Loop para as tentativas do usuário
while True:
    # Solicita ao usuário que tente adivinhar o número
    tentativa = int(input("Qual é o número? "))

    # Verifica se o número está correto
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break  # Encerra o loop quando o usuário acerta
    else:
        print("Errou! Tente novamente.")