# Dicionário com alguns países e suas capitais
paises_capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington, D.C.",
    "França": "Paris",
    "Japão": "Tóquio",
    "Alemanha": "Berlim",
    "Canadá": "Ottawa",
    "Argentina": "Buenos Aires"
}

# Solicita ao usuário que digite o nome de um país
pais = input("Digite o nome de um país: ")

# Verifica se o país está no dicionário (sem diferenciar maiúsculas e minúsculas)
capital = paises_capitais.get(pais.strip().title())

# Exibe a capital correspondente ou uma mensagem de erro
if capital:
    print(f"A capital de {pais.strip().title()} é {capital}.")
else:
    print("País não encontrado no dicionário.")