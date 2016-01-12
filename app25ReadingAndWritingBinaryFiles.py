__author__ = 'Rafael'

# Lendo e escrevendo informações binárias de arquivos.
buffersize = 100000
input = open('app25SupportFile.jpg', 'rb')
output = open('app25NewSupportFile.jpg', 'wb')
buffer = input.read(buffersize)

while len(buffer):
    output.write(buffer)
    print('.', end = '')
    buffer = input.read(buffersize)