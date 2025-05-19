# Lista para armazenar palavras com mais de 5 letras
palavras_longas = []

while True:
    try:
        entrada = input("Digite uma palavra (ou 'parar' para encerrar): ").strip()

        if entrada.lower() == "parar":
            break  # Encerra o programa

        if entrada.isnumeric():
            continue  # Ignora palavras numéricas

        if len(entrada) > 5:
            palavras_longas.append(entrada)  # Armazena palavras com mais de 5 letras

    except Exception as e:
        print("Erro ao processar a palavra. Tente novamente.")
        continue

# Exibe o resultado
print("\nPalavras com mais de 5 letras inseridas:")
print(palavras_longas)