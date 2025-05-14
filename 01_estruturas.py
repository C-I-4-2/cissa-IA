# Solicita a nota do usuário
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Verifica a situação do aluno com base na nota
if nota < 0 or nota > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
elif nota < 5:
    print("Aluno REPROVADO.")
elif nota < 7:
    print("Aluno em RECUPERAÇÃO.")
else:
    print("Aluno APROVADO.")