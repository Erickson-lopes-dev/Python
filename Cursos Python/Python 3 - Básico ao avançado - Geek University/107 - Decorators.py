# -*- coding: iso-8859-1 -*-

"""
O que s�o Decoradores?

    - Decorators s�o fun��es
    -  que envolvem outras fun��es e tem uma sintax pr�pria, usando "@" (syntact Sugar)

"""


# def seja_educado(funcao):
#     def sendo():
#         print('Foi um prazer conhecer voc�!')
#         funcao()
#         print('Tenha um �timo dia!')
#
#     return sendo()
#
#
# def saudacao():
#     print('Seja bem vindo ao meu curso')
#
#
# def raiva():
#     print('Ja pode se retirar')
#

# seja_educado(saudacao)
# print()
# seja_educado(raiva)

def seja_educado(funcao):
    def sendo():
        print('seja bem vindo')
        funcao()
        print('otimo dia ')

    return sendo()


@seja_educado
def legal():
    print('estou inserido aqui')



