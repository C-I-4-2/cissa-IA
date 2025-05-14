# Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada de 1 a 10
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")