#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija

calcu = CalculadoraHija()

if __name__ == "__main__":
    try:

        fichero = open(str(sys.argv[1]))
        lineas = fichero.readlines()

        for linea in lineas:

            linea = linea[:-1].split(",")
            result = 0
            operacion = linea[0]
            primera_iteracion = True

            for operando in linea[1:-1]:
                if primera_iteracion is True:
                    operando1 = int(operando)
                    primera_iteracion = False
                else:
                    operando1 = result

                operando2 = int(linea[linea.index(operando) + 1])

                if operacion == "suma":
                    result = calcu.suma(operando1, operando2)
                elif operacion == "resta":
                    result = calcu.resta(operando1, operando2)
                elif operacion == "multiplica":
                    result = calcu.multiplica(operando1, operando2)
                elif operacion == "divide":
                    result = calcu.divide(operando1, operando2)
                else:
                    sys.exit("Error: La primera palabra de la línea " +
                             "debe de indicar sólamente suma, resta," +
                             "multiplica o divide")
            print("El resultado de la operación " + operacion + " es " +
                  str(result))

    except ValueError:
        sys.exit("Error: El argumento 1 y 3 deben de ser números")
    except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")
