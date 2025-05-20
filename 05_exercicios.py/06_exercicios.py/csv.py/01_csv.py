import csv

# Lista de dicionários com os dados das pessoas
pessoas = [
    {"Nome": "Ana Silva", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Carlos Souza", "Idade": 35, "Cidade": "Rio de Janeiro"},
    {"Nome": "Mariana Lima", "Idade": 22, "Cidade": "Belo Horizonte"},
    {"Nome": "João Mendes", "Idade": 40, "Cidade": "Curitiba"}
]

# Nome do arquivo CSV a ser criado
nome_arquivo = "pessoas.csv"

# Abrimos o arquivo no modo escrita ('w') com codificação UTF-8
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Definimos os nomes das colunas (cabeçalho)
    campos = ["Nome", "Idade", "Cidade"]

    # Criamos o escritor CSV que usa dicionários
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    # Escrevemos o cabeçalho no arquivo
    escritor.writeheader()

    # Escrevemos cada linha de dados
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")