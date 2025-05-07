# Solicita ao usuário que digite um número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo
if numero > 0:
    print("O número é positivo.")

# Verifica se o número é negativo
elif numero < 0:
    print("O número é negativo.")

# Se não for maior nem menor que zero, então é igual a zero
else:
    print("O número é igual a zero.")