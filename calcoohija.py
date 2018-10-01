#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplica(self, operando1, operando2):
        return(operando1 * operando2)

    def divide(self, operando1, operando2):
        return(operando1 / operando2)


calcu = CalculadoraHija()

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        operacion = str(sys.argv[2])

        if operacion == "suma":
            result = calcu.suma(operando1, operando2)
        elif operacion == "resta":
            result = calcu.resta(operando1, operando2)
        elif operacion == "multiplica":
            result = calcu.multiplica(operando1, operando2)
        elif operacion == "divide":
            result = calcu.divide(operando1, operando2)
        else:
            sys.exit("Error: argument 2 must be suma " +
                     "resta, multiplica or divide")
    except ValueError:
        sys.exit("Error: arguments 1 and 3 must be numbers")
    except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")

    print("El resultado es " + str(result))
