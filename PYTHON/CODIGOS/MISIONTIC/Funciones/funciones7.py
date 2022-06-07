#hACER UNA FUNCION QUE PIDA DOS NUMEROS Y LE CALCULE LAS 4 
#OPERACIONES BASICS. POR MEDIO DE UNA FUNCION O FUNCIONES.

# def funciones_basicas():
#     a=float(input("Ingrese un numero: "))
#     b=float(input("Ingrese otro numero: "))
#     suma=a+b
#     resta=a-b
#     multiplicacion=a*b
#     division=a/b
#     print("La suma es: ",suma,", la resta es: ",resta,
#     ", la multiplicacion es: ",multiplicacion,", la division es: ", division)

# funciones_basicas()


def operaciones(num1,num2):
    suma=num1+num2
    resta=num1-num2
    multiplicar=num1*num2
    dividir=num1/num2
    print("Los numeros son ",num1, " y ",num2)
    print("La suma de los dos numeros es: ",suma)
    print("La resta de los dos numeros es: ",resta)
    print("La multiplicacion de los dos numeros es: ",multiplicar)
    print("La division de los dos numeros es: ",dividir)

num1=float(input("Digite un numero: "))
num2=float(input("Digite un numero: "))
operaciones(num1,num2)