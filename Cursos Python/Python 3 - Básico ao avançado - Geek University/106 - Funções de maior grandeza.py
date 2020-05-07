# -*- coding: iso-8859-1 -*-
"""
Fun��es de maior grandeza

 - fun��es com argumentos para outras fun��es

"""


def soma(a, b):
    return a + b


def calculo(a, b, funcao):
    return funcao(a, b)


print(calculo(5, 3, soma))

"""
fun��es aninhadas

em python podemos ter fun��es dentro de fun��es (fun��es internas)

"""

from random import choice


def cumprimentar(pessoa):
    def humor():
        return choice(['Estou feliz,', 'Estou triste,', 'Estou bem,'])
    return humor() + pessoa


print(cumprimentar(' Gean'))
