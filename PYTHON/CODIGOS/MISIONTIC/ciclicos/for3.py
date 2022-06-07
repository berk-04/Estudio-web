#Hacer un programa que imprima los numeros pares de un numero digitado por el usuario

numero=int(input("Ingrese un numero: "))

for i in range(1,numero+1):
    if i % 2==0:
        print("El numero ",i, " es par")
