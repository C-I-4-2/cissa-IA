# Define a senha correta
senha_correta = "1234"

# Loop infinito até que a senha correta seja digitada
while True:
    # Solicita a senha ao usuário
    senha = input("Digite a senha: ")

    # Verifica se a senha está correta
    if senha == senha_correta:
        print("Acesso concedido. Bem-vindo!")
        break  # Encerra o loop
    else:
        print("Senha incorreta. Tente novamente.")