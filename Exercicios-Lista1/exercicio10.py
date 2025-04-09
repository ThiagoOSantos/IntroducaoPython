def imc(peso,altura):
    peso = float(input("Digite seu peso para o calculo do IMC"))
    altura = float(input("Digite sua altura para o calculdo do IMC"))
    imc= peso/altura
    if imc < 18.5:
        print("Você está abaixo do peso")
    elif imc >18.5 and imc < 24.9:
        print("Você está com peso normal")
    elif imc >24.9 and imc < 29.9:
        print("Você está com sobrepeso")
    else:
        print("Você está com obesidade")
imc()