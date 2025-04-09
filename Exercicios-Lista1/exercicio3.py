def nota():
    num = float(input("Digite o valor da nota do aluno"))
    if num >=7:
        print("Aluno aprovado")
    elif num >= 5 and num <= 6.9:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
nota()