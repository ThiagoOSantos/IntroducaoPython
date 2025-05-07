# Exercicio 1 - lista 7
'''letra d'''
# Exercicio 2 - lista 7
'''letra c'''
# Exercicio 3 - lista 7
'''class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print(f"Olá, {self.nome}!")

p = Pessoa("Lucas")
p.saudacao()

o código acima imprime "Olá, Lucas"
'''
# Exercicio 4 - lista 7
'''o python ignora e segue o codigo, letra a'''
# Exercicio 5 - lista 7
'''class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_idade(self):
        print(f"{self.nome} tem {self.idade}")'''

# Exercicio 6 - lista 7
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar():
        print(f"{self.nome} custa R${self.preco}") # O Erro está em não ter o self dentro da função mostrar
'''
# Exercicio 7 - lista 7
'''class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self,valor):
        self.preço += self.preco - (self.preco*valor/100)
        print(f"{self.nome} custa R${self.preco} com desconto de {valor}%")
'''
# Exercicio 8 - lista 7
'''letra b, é a forma q determina a construção da classe, chamado na criação do objeto  '''
# Exercicio 9 - lista 7
'''class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

c = Circulo(2) #a saída é 12,56
print(c.area())'''

# Exercicio 10 - lista 7
'''um atributo é uma variavel dentro de uma classe/funçao, e o método é a criação de uma função dentro de uma classe'''
