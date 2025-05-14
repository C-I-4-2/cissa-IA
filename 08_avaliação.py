# Solicita a nota de avaliação ao usuário
nota = int(input("Avalie o restaurante de 0 a 5 estrelas: "))

# Verifica se a nota está dentro do intervalo válido
if nota < 0 or nota > 5:
    print("Nota inválida! Por favor, digite um número de 0 a 5.")
elif nota == 0:
    print("☆☆☆☆☆ - Péssimo! Que experiência ruim.")
elif nota == 1:
    print("★☆☆☆☆ - Muito ruim. Precisa melhorar muito.")
elif nota == 2:
    print("★★☆☆☆ - Ruim. Tem potencial, mas falta qualidade.")
elif nota == 3:
    print("★★★☆☆ - Razoável. Dá para melhorar.")
elif nota == 4:
    print("★★★★☆ - Muito bom! Poucos detalhes a melhorar.")
else:  # nota == 5
    print("★★★★★ - Excelente! Recomendado com certeza!")