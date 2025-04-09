'''Primeiro exercício prático de Python com condicionais'''
def maioridade():
    idade= int(input("digite a idade da pessoa que deseja entrar na festa"))
    if idade >= 18:
        print("Sua entrada foi permitida, boa festa")
    else:
        print("Você não pode entrar pois não é maior de 18 anos")

maioridade()