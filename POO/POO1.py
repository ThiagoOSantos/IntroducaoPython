# Entendendo o que é uma Classe - Programação Orientada a Objetos

'''class Pessoa: # Em termos de hieraqruia, a classe sempre virá primeiro
    def __init__(self, nome, idade): # Função construtora e requerimentos
        self.nome = nome # criação da variável self.nome e atribuição a nome
        self.idade = idade # criação da variável self.idade e atribuição a idade

    def apresentar(self): #Todas as fuunções recebem o 'self'
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Isadora", 19) # Criando um objeto Pessoa e atribuindo uma variável
p2 = Pessoa("Isabela", 33)
p1.apresentar() # Utilizando o objeto criado para utilizar uma função da classe
p2.apresentar()'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, porcentagem):
        desconto = self.preco *(porcentagem/100)
        self.preco -= desconto

    def mostrar_produto(self):
        print(f"{self.nome} custa R${self.preco:.2f}")

produto = Produto("Monitor", 1200)
produto.mostrar_produto()
produto.aplicar_desconto(10)
produto.mostrar_produto()