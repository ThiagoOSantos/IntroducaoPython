#exercicio 6
def verificar_senha():
    senha = input("Digite a senha: \n")
    if senha == "senac123":
        print("Acesso liberado.")
    else:
        print("Senha incorreta!")

# verificar_senha()
#exercicio 7
def converter_para_dolar():
    reais = float(input("Digite o valor em reais (R$): \n"))
    dolar = reais / 5.20
    print("O valor em dolares é: ", dolar)

#converter_para_dolar()
#exercicio 9
def caixa_eletronico():
    valor = int(input("Digite o valor que será sacado (multiplos de 10): \n"))
    if valor % 10 == 0:
        ced100 = valor // 100
        valor %= 100
        ced50 = valor // 50
        valor %= 50
        ced20 = valor // 20
        valor %=20
        ced10 = valor //10
        valor %=10

        print("Notas entregues: \n")
        if ced100>0:
            print(f"{ced100} nota(s) de RS100.\n")
        if ced50>0:
            print(f"{ced100} nota(s) de RS50.\n")
        if ced20>0:
            print(f"{ced20} nota(s) de RS20.\n")
        if ced10>0:
            print(f"{ced10} nota(s) de RS10.\n")
            
    else:
        print("Valor inválido. Tente outro valor múltiplo de 10")

#exercicio 10
def calcular_imc():
    peso = float(input("Digite seu peso em kg: \n"))
    altura = float(input("Digite sua altura em metros:\n"))
    imc = peso / (altura**2)
    if imc <=18.5:
        print("Você está abaixo do peso!")
    elif imc <= 24.9:
        print("Peso normal.")
    elif imc <= 29.9:
        print("Sobrepeso, cuidado!")
    else:
        print("Obesidade.")