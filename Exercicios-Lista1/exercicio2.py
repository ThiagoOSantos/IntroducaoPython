def desconto():
    valor = float(input("Digite o valor do item para desconto"))
    if valor>100:
        valor = valor - valor/10
        print(f"o valor do item com o desconto é de {valor}")
    else:
        print("Não é possível aplicar o desconto da promoção")

desconto()