#Hacer un ejercicio que lea 3 numeros y determine cual es el mayor de ellos
#cual es el del medio y cual es el menor
num1=float(input("Digite el numero 1: "))
num2=float(input("Digite el numero 2: "))
num3=float(input("Digite el numero 3: "))

if num1>num2:
    if num1>num3:
        print("El numero 1 es el mayor", num1)
    else:
        print("El numero 3 es el mayor", num3)
elif num2>num3:
        print("El numero 2 es el mayor", num2)
else:
    print("El numero mayor es: ", num3)













