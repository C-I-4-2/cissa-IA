# Função para converter de qualquer unidade para Celsius
def para_celsius(valor, origem):
    if origem == "c":
        return valor
    elif origem == "f":
        return (valor - 32) * 5 / 9
    elif origem == "k":
        return valor - 273.15

# Função para converter de Celsius para a unidade desejada
def de_celsius_para(valor_celsius, destino):
    if destino == "c":
        return valor_celsius
    elif destino == "f":
        return (valor_celsius * 9 / 5) + 32
    elif destino == "k":
        return valor_celsius + 273.15

# Entrada de dados do usuário
valor = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F ou K): ").strip().lower()
destino = input("Informe a unidade de destino (C, F ou K): ").strip().lower()

# Verifica se as unidades são válidas
unidades_validas = ["c", "f", "k"]
if origem in unidades_validas and destino in unidades_validas:
    # Converte para Celsius, depois para a unidade final
    valor_celsius = para_celsius(valor, origem)
    resultado = de_celsius_para(valor_celsius, destino)

    # Exibe o resultado final
    print(f"{valor:.2f}°{origem.upper()} equivale a {resultado:.2f}°{destino.upper()}")
else:
    print("Unidade inválida. Use C, F ou K.")