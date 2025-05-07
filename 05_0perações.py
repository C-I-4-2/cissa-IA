# Solicita ao usuário que digite o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que digite o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que escolha uma operação matemática
operacao = input("Escolha a operação (+, -, * ou /): ")

# Verifica qual operação foi escolhida e executa o cálculo correspondente
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == "/":
    # Verifica se o segundo número é zero para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    # Caso o usuário digite uma operação inválida
    print("Operação inválida. Use apenas +, -, * ou /.")