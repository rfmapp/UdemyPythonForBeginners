__author__ = 'Rafael'

# Demonstra como lidar com erros de sintaxe.

# Variável.
name = 'Rafael'
# Loop.
if name = 'Rafael' # Aqui o primeiro erro é ter apenas 1 sinal '=', pois num teste deve ser usado 2 '=='. O segundo é a falta de ':' no final da sentença, indicando uma estrutura de controle.
    print('Your name is Rafael')

i = 5
j = 15
k = ((i*j) + (j+i) # Aqui o erro é a falta do parênteses final.

    print k # Por fim, o primeiro erro aqui é que a expressão está indentada de forma errada. Python de fato considera isso um erro. O segundo é a falta dos parênteses depois de 'print'.