import random
import string

# Caracteres especiais que serão usados na senha
caracteres_especiais = "!@#$%&*()-_=+[]{};:,.<>?/|\\"

# Combina letras, números e caracteres especiais
todos_caracteres = string.ascii_letters + string.digits + caracteres_especiais

try:
    # Solicita ao usuário o tamanho da senha
    tamanho = int(input("Informe a quantidade de caracteres da senha: "))

    if tamanho <= 0:
        print("O tamanho da senha deve ser maior que zero.")
    else:
        # Gera senha aleatória
        senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
        print("Senha gerada:", senha)

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")