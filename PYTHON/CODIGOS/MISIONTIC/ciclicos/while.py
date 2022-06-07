#Hacer un programa para solo  obtener numeros positivos

from random import random

numero=float(input("Ingrese un numero: "))

while numero >= 0:
    print("El numero", numero, "es positivo")
    numero=float(input("Digite un numero: "))
print("El numero es negativo")