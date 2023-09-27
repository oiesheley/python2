# Solicita o preço original do produto ao usuário
preco_original = float(input("Digite o preço original do produto: R$ "))

# Solicita a porcentagem de desconto ao usuário
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# Calcula o valor do desconto
valor_desconto = (porcentagem_desconto / 100) * preco_original

# Calcula o preço com o desconto aplicado
preco_com_desconto = preco_original - valor_desconto

# Exibe o valor do desconto e o preço com desconto
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço com desconto: R$ {:.2f}".format(preco_com_desconto))


