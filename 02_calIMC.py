# Solicita ao usuário que informe o peso em quilogramas (kg)
peso = float(input("Digite seu peso (em kg): "))

# Solicita ao usuário que informe a altura em metros (m)
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC usando a fórmula: IMC = peso / (altura * altura)
imc = peso / (altura ** 2)

# Exibe o valor calculado do IMC
print(f"Seu IMC é: {imc:.2f}")  # {:.2f} limita o número a 2 casas decimais

# Classifica o IMC de acordo com a tabela padrão
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibe a classificação final
print("Classificação:", classificacao)