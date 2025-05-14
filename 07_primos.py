# Lista de números inteiros
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]

# Percorre cada número da lista
for num in numeros:
    # Números menores que 2 não são primos
    if num < 2:
        continue

    # Verifica se o número é primo
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    # Se não for primo, pula para o próximo
    if not primo:
        continue

    # Se for primo, imprime
    print(num)