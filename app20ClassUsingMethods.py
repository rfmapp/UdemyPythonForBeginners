__author__ = 'rafael'

# Como utilizar os métodos.

class Person:
    # Método de inicialização da classe
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name
    # Método de exibição dos dados.
    def display(self):
        print("You're a", self.gender, "and your name is", self.name)

# Criação do objeto(instância da classe).
person = Person('Male', 'Rafael')
person.display()