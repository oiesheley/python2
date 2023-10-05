def subtracao(a, b):
    return a - b

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

vetor = []
while True:
    print("Digite 1 para soma.")
    print("Digite 2 para subtração.")
    print("Digite 3 para multiplicação.")
    print("Digite 4 para divisão.")
    print("Digite 5 para sair da calculadora.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5 or len(vetor) == 10:
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = soma(num1, num2)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = divisao(num1, num2)

    vetor.append(resultado)

print("Resultados:")
print(vetor)
