# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita as três notas do aluno e converte para float (números com casas decimais)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média com duas casas decimais
print(f"Média de {nome}: {media:.2f}")

# Verifica a situação do aluno com base na média
if media >= 7:
    print("Situação: Aprovado ✅")
elif media >= 5:
    print("Situação: Recuperação ⚠️")
else:
    print("Situação: Reprovado ❌")