def temperatura():
    temp = int(input("Digite a temperatura"))
    if temp < 18:
        print("Hoje está frio")
    elif temp >18 and temp <25:
        print("Hoje está uma temperatura agradável")
    else:
        print("Hoje está bastante calor")

temperatura()
        
