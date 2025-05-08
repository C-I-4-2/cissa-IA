# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas (para tornar a verificação mais precisa)
palavra_formatada = palavra.replace(" ", "").lower()

# Inverte a palavra usando slicing [::-1]
palavra_invertida = palavra_formatada[::-1]

# Verifica se a palavra original é igual à invertida
if palavra_formatada == palavra_invertida:
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")