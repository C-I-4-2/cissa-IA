# Listas para armazenar os números positivos e negativos
positivos = []
negativos = []

while True:
    entrada = input("Digite um número inteiro (ou 0 para encerrar): ")

    try:
        numero = int(entrada)  # Tenta converter a entrada para inteiro

        if numero == 0:
            break  # Encerra o loop se o número for 0

        if numero > 0:
            positivos.append(numero)  # Armazena positivos
        else:
            negativos.append(numero)  # Armazena negativos

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue  # Ignora entrada inválida e continua o loop

# Exibe os resultados
print(f"\nQuantidade de números positivos: {len(positivos)}")
print(f"Quantidade de números negativos: {len(negativos)}")
