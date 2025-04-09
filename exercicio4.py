def horastrabalhadas(hora, valorhora):
    horas = float(input("Digite a quantidade de horas trabalhadas"))
    if horas > 8:
        print("Hora extra registrada")
    valorhoras = float(input("Digite o valor da hora trabalhada"))
    print(f"Esse é o total de {horas} trabalhadas: {valorhoras}")
    
    horastrabalhadas()