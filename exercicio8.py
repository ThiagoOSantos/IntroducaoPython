def media(nota1,nota2,nota3):
    nota1= float(input("Digite a nota 1"))
    nota2= float(input("Digite a nota 2"))
    nota3= float(input("Digite a nota 3"))
    media= nota1+nota2+nota3
    if media >=7:
        print("Aluno APROVADO, NOICE")
    elif media >5 and media <= 6.9:
        print("Aluno em recuperação, nt(?)")
    else:
        print("Aluno REPROVADO, iiiiih, sifudeu k k k")

media()
    