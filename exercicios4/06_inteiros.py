pares = []
contador = 0

while contador < 10:
    entrada = input(f"Digite o {contador + 1}º número inteiro: ")

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            print("Número ímpar ignorado.")
        contador += 1  # conta mesmo se for ímpar, como pedido
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        continue

print("\nLista de números pares válidos:")
print(pares)