#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

if __name__ == "__main__":
    try:
        calcu = CalculadoraHija()
        lineas = []

        with open(sys.argv[1]) as File:
            file = csv.reader(File, delimiter=" ")
            for linea in file:
                elementos = " ".join(linea) + "\n"
                lineas.append(elementos)

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
                    sys.exit("Error: The first word in each line " +
                             "must be suma, resta," +
                             "multiplica or divide")
            print("The result of the operation " + operacion + " is " +
                  str(result))

    except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")
    except FileNotFoundError:
        sys.exit("File or directory '" + str(sys.argv[1]) + "' not found")
