# sequencialidade - acordar
print("acordei")
print("ir ao banheiro")
print("tomar cafe")
print("escovar os dentes")

# definiçao clara
print("vamos somar 2 numeros, me iga qual e digite")
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
soma = numero1 + numero2
print("a soma é: ", soma)

# finitude
'''for i in range(5):
    print("contar", 1)
while True:
        print("nao tem fim")'''

 # determinismo
def soma(a, b):
            return a + b
print(soma(4, 5))
