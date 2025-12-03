"""
Escreva um programa que recebe um num e classifica em uma das seguintes categorias:
    negativo: se o num for menor que 0
    zero: se o num for exatamente o
    positivo e impar: se o num for maior que 0 e impar
    positivo e par: se o num for maior que 0 e par
    divisivel por 3 e 5: se o num for divisivel por 3 e 5
    outros num positivos: se o num for maior que 0, mas nao se encaixar em nenhuma da outras ops
    utilizar match/case e dentro de cada caso utilizar if para varificar as condicoes
"""

import os 

num=int(input("escreva um numero: "))

match (num>0, num==0, num<0):
        case (False,False,True):
            print("Negativo")
        case (False,True,False):
            print("Zero")
        case (True,False,False):
            if num %3 == 0 and num %5 == 0:
                print("divisivel por 3 e 5")
            elif num % 2 == 0:
                print("positivo e par")
            elif num % 2 != 0:
                print("positivo e ímpar")
            else:
                print("outros numeros positivos")
