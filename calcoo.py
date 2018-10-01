#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora(object):

    def suma(self, operando1, operando2):
        return(operando1 + operando2)

    def resta(self, operando1, operando2):
        return(operando1 - operando2)


calcu = Calculadora()

if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: arguments 1 and 3 must be numbers")

    if sys.argv[2] == "suma":
        result = calcu.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calcu.resta(operando1, operando2)
    else:
        sys.exit("Error: argument 2 must be suma or resta")

    print("The result is " + str(result))
