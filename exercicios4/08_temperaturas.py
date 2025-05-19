temperaturas = []

for i in range(7):
    entrada = input(f"Digite a temperatura #{i + 1} (ou 'fim' para encerrar): ").strip()

    if entrada.lower() == 'fim':
        break

    try:
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        print("Entrada inválida! Digite um número válido ou 'fim'.")
        continue

# Verifica se houve temperaturas registradas
if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"\nTemperaturas registradas: {temperaturas}")
    print(f"Média das temperaturas: {media:.2f}°C")
else:
    print("\nNenhuma temperatura válida foi registrada.")