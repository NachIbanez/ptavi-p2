#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora(object):

    def suma(self, operando1, operando2):
        return(operando1 + operando2)

    def resta(self, operando1, operando2):
        return(operando1 - operando2)


class CalculadoraHija(Calculadora):

    def multiplicar(self, operando1, operando2):
        return(operando1 * operando2)

    def dividir(self, operando1, operando2):
        return(operando1 / operando2)

calcu = CalculadoraHija()

try:
    operando1 = int(sys.argv[1])
    operando2 = int(sys.argv[3])
    operacion = str(sys.argv[2])

    if operacion == "suma":
        result = calcu.suma(operando1, operando2)
    elif operacion == "resta":
        result = calcu.resta(operando1, operando2)
    elif operacion == "multiplicar":
        result = calcu.multiplicar(operando1, operando2)
    elif operacion == "dividir":
        result = calcu.dividir(operando1, operando2)
    else:
        sys.exit("Error: El argumento 2 debe de indicar sólamente suma, " +
                 "resta, multiplicar o dividir")
except ValueError:
        sys.exit("Error: El argumento 1 y 3 deben de ser números")
except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")

print("El resultado es " + str(result))

