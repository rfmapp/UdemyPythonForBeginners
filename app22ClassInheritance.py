__author__ = 'rafael'

# Exemplificando o conceito de Herança.

# Classe mãe.
class Animals:
    def eat(self):
        print("I can eat.")
    def talk(self):
        print("I can talk.")

# Classe filha. A associação de herança é definida pela passagem da classe mãe como um parâmetro da classe filha.
# Pode herdar os métodos da classe mãe, mas pode alterar esses métodos, bem como criar novos.
class Cat(Animals):
    def talk(self):
        print("meow")
    def move(self):
        print("I can move")

# Outra classe filha. Nesse caso, não altera nenhum método da classe mãe, nem implementa nenhum novo.
class Dog(Animals):
    pass

# Criação do objeto da classe Cat.
muffin = Cat()
# Exemplo de método que está presente na classe mãe, mas foi alterado na classe filha.
muffin.talk()
# Exemplo do método presente apenas na classe filha.
muffin.move()
# Exemplo do método existente na classe mãe e que não foi alterado na classe filha.
muffin.eat()
# Criação do objeto da classe Dog.
sky = Dog()
# Fazendo uso dos métodos da classe mãe.
sky.talk()
sky.eat()