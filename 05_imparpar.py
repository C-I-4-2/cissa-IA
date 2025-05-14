# Loop que percorre os números de 1 a 10
for i in range(1, 11):
    # Verifica se o número é par
    if i % 2 == 0:
        continue  # Se for par, pula para a próxima repetição do loop

    # Se o número não for par (ou seja, for ímpar), imprime
    print(i)