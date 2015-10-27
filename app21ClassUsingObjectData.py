__author__ = 'rafael'

# Mostrando como definir valore à variáveis e recuperar esses valores através de métodos.

class Example:
    # Inicializamos a classe, passando como parâmetro uma lista não definida. O parâmetro **kwargs refere-se à passagem de um dicionário. Se fosse *kwargs seria uma tulpa.
    def __init__(self, **kwargs):
        self.variables = kwargs

    # Temos um método que define uma chave(k) e respectivo valor(v) ao dicionário.
    def set_vars(self,k,v):
        self.variables[k] = v

    # Temos um método que retorna o valor de uma chave(passada como parâmetro) do dicionário. Se não encontrar, retorna 'None'.
    def get_vars(self,k):
        return self.variables.get(k, None)

# Criação da instância (objeto) da classe.
var = Example()
# Aqui será retornado 'None', pois não definimos nenhuma chave e valor.
print(var.get_vars('status'))
# Aqui fazemos a definição de uma chave e seu valor.
var.set_vars('name','Rafael')
# Exibição do valor da chave passada.
print(var.get_vars('name'))
var.set_vars('age', 32)
var.set_vars('country', 'Brasil')
print(var.get_vars('age'))
print(var.get_vars('country'))

# Outra maneira de se passar as chaves e valores seria na inicialização da classe. Aqui pode-se passar quantas chaves
# e valores quiser.
var2 = Example(eyes='Green', skin='White')
print(var2.get_vars('eyes'))
print(var2.get_vars('skin'))