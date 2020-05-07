# -*- coding: iso-8859-1 -*-

"""
StringIO

para mexer em arquivos do sistema precisamos ter permiss�o.
    permiss�o para ler e escrever neles.

StringIO -> usado pra criar e ler arquivos em mom�ria

"""
# fazer import
from io import StringIO

mensagem = 'String normal '

# podemos criar um arquivo em mem�ria ja com uma string ou mesmo vazia
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# agora tendo o arquivo podemos utilizar tudo o que sabemos
print(arquivo.read())

# escrevendo outros textos
arquivo.write(' Novos testes')

# Movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
