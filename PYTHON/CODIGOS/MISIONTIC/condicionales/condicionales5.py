num1=float(input("Digite el numero 1: "))
num2=float(input("Digite el numero 2: "))
num3=float(input("Digite el numero 3: "))

if num1==num2 or num1==num3 or num2==num3:
    print("Hay dos o mas numeros iguales. Cambielos")
else:
    if num1>num2:
        if num1>num3:
            print("El mayor es el numero 1: ", num1)
            if num2>num3:
                print("El del medio es el numero 2: ", num2)
                print("El menor es el numero 3: ", num3)
            else:
                print("El del medio es el numero 3: ", num3)
                print("El menor es el numero 2: ", num2)
        else:
            print("El mayor es el numero 3: ", num3)
            print("El del medio es el numero 1: ")






