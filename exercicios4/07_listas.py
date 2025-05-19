lista_compras = []

for i in range(10):
    try:
        item = input(f"Digite o nome do produto #{i + 1} (ou 'fim' para encerrar): ").strip()

        if item.lower() == "fim":
            break
        if item == "":
            print("Item vazio ignorado.")
            continue

        lista_compras.append(item)
    except Exception as e:
        print("Erro ao inserir o item. Tente novamente.")
        continue

print("\nLista de Compras:")
for i, produto in enumerate(lista_compras, start=1):
    print(f"{i}. {produto}")