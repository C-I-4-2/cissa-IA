idades = []

for _ in range(1000):  # limite alto para permitir muitas entradas
    entrada = input("Digite uma idade (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        idade = int(entrada)
        if 0 <= idade <= 120:
            idades.append(idade)
        else:
            print("Idade inválida! Deve estar entre 0 e 120.")
            continue
    except ValueError:
        print("Entrada inválida! Digite um número inteiro ou 'fim'.")
        continue

print("\nLista de idades válidas:")