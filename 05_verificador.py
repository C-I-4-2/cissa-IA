# Solicita ao usuário que digite um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é maior que 1, pois 0 e 1 não são primos
if numero <= 1:
    print("Números menores ou iguais a 1 não são primos.")
else:
    # Assume que o número é primo
    primo = True

    # Verifica se existe algum divisor além de 1 e ele mesmo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            # Se houver divisor, não é primo
            primo = False
            break  # Não precisa continuar verificando

    # Exibe o resultado
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")