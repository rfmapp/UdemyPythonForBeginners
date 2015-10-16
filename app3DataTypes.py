__author__ = 'rafael'

# numeros.
a = 50;
# exibicao do tipo de dado da variavel e seu valor.
print(type(a),a);
# aqui vemos que um numero aparentemente igual nao tem o mesmo tipo de dado.
b = 50.0;
print(type(b),b);
# pode-se contornar isso com o uso de uma função do tipo 'type casting', que seria uma conversao de tipos de dados.
c = int(50.0);
print(type(c),c);
# com o uso dessa funcao, os valores sao sempre arrendondados para baixo.
d = int(50.9);
print(type(d),d);
# também há uma forma de contornar isso, usando outra funcao.
e = round(50.9);
print(type(e),e);
# assim, para que possamos trabalhar de forma mais precisa com numeros de ponto flutuante, o ideal seria usar sua funcao.
# tanto o tipo de dado como o valor fica melhor representado, tenha ele o '.' ou nao.
f = float(50.9);
g = float(50);
print(type(f),f);
print(type(g),g);

print("");

# strings.
h = "This is a String.";
print(type(h),h);
i = 'This is a String too.';
print(type(i),i);
j = '''
    This
    is
    also
    a
    String.
''';
print(type(j),j);
# podemos usar caracteres de escape. nesse caso, 'quebramos' a exibicao em outra linha.
l = 'This is \nanother String.';
print(type(l),l);
# mas caso queira exibir aqueles caracteres especiais, basta 'escapar' com outra barra.
m = 'This (\\n) is a escape caracter.';
print(type(m),m);
# podemos inserir uma String dentro de outra, algo tambem conhecido como concatenacao.
# vejamos a maneira mais moderna de realizar isso.
n = 'Rafael Marques';
o = 'My name is {}.'.format(n);
print(type(o),o);
# a maneira obsoleta seria.
p = 'Repeting: my name is %s.' % n;
print(type(p),p);

print("");

# listas(arrays). podem ser tulpas e listas.
# tulpas.
q = (1,2,3,4,5);
print(type(q),q);
# o problema de se usar uma tulpa e que nao se pode modificar seu valor. uma vez definida a lista, ela nao muda.
# listas.
r = [1,2,3,4,5];
print(type(r),r);
# ja uma lista podemos modificar. adicionando um novo item.
r.append(6);
print(type(r),r);

print("");

# dicionarios. sao como arrays associativos. existe uma chave e um valor associado a ela.
# as chaves sempre sao declaradas usando aspas simples. os valores de acordo com o tipo de dado.
s = {'first':'Rafael','last':'Marques'};
t = {'id': 203,'username':'rafael'};
print(type(s),s);
print(type(t),t);
# outra maneira de declarar dicionarios seria. visualmente, essa e a maneira mais legivel. aqui tambem ha diferenca na
# declaracao das chaves, que passam a ser declaradas como variaveis, sem as aspas simples.
u = dict(
    first_name = 'Rafael',
    last_name = 'Marques'
);
print(type(u),u);

print("");

# boolean.
v = True;
print(type(v),v);
