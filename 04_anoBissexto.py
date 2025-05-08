# Solicita ao usuário que insira um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto:
# 1. Deve ser divisível por 4
# 2. Mas se for divisível por 100, também deve ser divisível por 400
if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")