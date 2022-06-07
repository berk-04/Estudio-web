#Hacer un ejercicio que lea 3 numeros y determine cual es el mayor de ellos
#cual es el del medio y cual es el menor
num1=float(input("Digite el numero 1: "))
num2=float(input("Digite el numero 2: "))
num3=float(input("Digite el numero 3: "))

if num1==num2 and num2==num3:
    print("Todos los numeros son iguales")
elif num1==num2:
    if num1>num3:
        print(num1, " y ",num2," son iguales, ademas son mayores", "y el numero menor es: ",num3)
    else:
        print(num3, " es mayor y ",num1," y ",num2, " son iguales y son menores")
elif num1==num3:
    if num1>num2:
        print(num1, " y ",num3," son iguales, ademas son mayores", "y el numero menor es: ",num2)
    else:
        print(num2, " es mayor y ",num1," y ",num3, " son iguales y son menores")
elif num3==num2:
    if num3>num1:
        print(num3, " y ",num2," son iguales, ademas son mayores", "y el numero menor es: ",num1)
    else:
        print(num1, " es mayor y ",num2," y ",num3, " son iguales y son menores")
elif num1>num2 and num1>num3:
    if num2>num3:
        print("EL numero mayor es: ", num1," ; El numero del medio es: ", num2, "y el numero menor es: ", num3)
    else:
        print("EL numero mayor es: ", num1," ; El numero del medio es: ", num3, "y el numero menor es: ", num2)
elif num2>num1 and num2>num3:
    if num1>num3:
        print("EL numero mayor es: ", num2," ; El numero del medio es: ", num1, "y el numero menor es: ", num3)
    else:
        print("EL numero mayor es: ", num2," ; El numero del medio es: ", num3, "y el numero menor es: ", num1)
else:
    if num1>num2:
        print("EL numero mayor es: ", num3," ; El numero del medio es: ", num1, "y el numero menor es: ", num2)
    else:
        print("EL numero mayor es: ", num3," ; El numero del medio es: ", num2, "y el numero menor es: ", num1)