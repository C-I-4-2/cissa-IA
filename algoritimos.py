# algoritimo de busca
''''def busca(lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i] == nome_procurado:
            return i # retorna para a posiçao
        return -1 # nao encontrou
    nomes = [" Maria", "Ana", "Joao", "Pedro"]
    posiçao = busca( nomes, "Ana")
    nome_procurado = input(" Qual nome voce quer procurar")
    print("Ana esta na posiçao:", posiçao)'''

    # algoritimo de busca binaria
def binaria (lista, valor_procurado):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim)// 2
        if lista[meio] == valor_procurado:
            return meio
        elif lista [meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return - 1
numeros =[1,3, 5, 7, 9, 11, 13, 15]
posiçao = binaria(numeros, 15)
print("numero encontrado na posiçao:", posiçao)