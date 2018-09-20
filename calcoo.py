#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora(object):
	
	def suma(self,operando1, operando2):
		return (operando1 + operando2)
	
	def resta(self,operando1, operando2):
		return (operando1 - operando2)

calcu = Calculadora()

try:
	operando1 = int(sys.argv[1])
	operando2 = int(sys.argv[3])
except ValueError:
		sys.exit("Error: El argumento 1 y 3 deben de ser números enteros o reales")

if sys.argv[2] == "suma":
	result = calcu.suma(operando1, operando2)
elif sys.argv[2] == "resta":
	result = calcu.resta(operando1, operando2)
else:
	sys.exit("Error: El argumento 2 debe de indicar sólamente suma o resta")

print("El resultado es " + str(result))



