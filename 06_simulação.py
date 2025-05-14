# Define a senha correta
senha_correta = "1234"

# Inicializa o contador de tentativas
tentativas = 0

# Loop infinito para pedir a senha
while True:
    # Solicita a senha ao usuário
    senha = input("Digite a senha: ")

    # Verifica se a senha está correta
    if senha == senha_correta:
        print("Acesso concedido. Bem-vindo!")
        break  # Encerra o loop se a senha estiver correta
    else:
        tentativas += 1  # Incrementa o número de tentativas
        print("Senha incorreta.")

    # Verifica se o número máximo de tentativas foi atingido
    if tentativas >= 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")
        break  # Encerra o loop após 3 tentativas incorretas