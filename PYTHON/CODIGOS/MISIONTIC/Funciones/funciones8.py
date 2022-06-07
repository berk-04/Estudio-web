#Hacer un menu por medio de una funcion para ejecutar
#diferentes programas

def menu():
    print("\n")
    print("Menu de programas con Funciones")
    print("---------------------------------")
    print("\n Selecciona una opcion")
    print("\n 1 - Mayor o Menor de Edad")
    print("\n 2 - Valor a pagar")
    print("\n 3 - Descuento")
    print("\n 4 - Valor total de la compra")
    print("\n 0 - Salir")
    print("\n")

def mayormenor():
    edad=int(input("Digite su edad:"))
    if edad>=18:
        print("Eres una persona mayor de edad")
    else:
        print("Eres una persona menor de edad")

def valorPagar():
    #Funcion que pide un valor de producto y una cantidad
    #Calcular el iva y el valor a pagar
    costo=float(input("Digite el precio del producto: "))
    cantidad=int(input("Digite la cantidad a comprar: "))
    cantidadcosto=costo*cantidad
    iva=cantidadcosto*0.19
    valorpagar=cantidadcosto+iva
    print("El valor a pagar es de: ", valorpagar)

def descuento():
    #Funcion que pide un numero de productos, si el costo total
    #es mayor a 100k tiene descuento de 12%, de lo contrario
    #tiene descuento del 5%
    cantidad_productos=int(input("Ingrese la cantidad de productos: "))
    costototal=0
    for i in range(cantidad_productos):
        costo=float(input("Digite el costo del "+ str(i+1)+" producto"))
        costototal=costototal+costo
    if costototal>100000:
        descuento=costototal*0.12
    else:
        descuento=costototal*0.05
    valorpagar=costototal-descuento
    print("El valor a pagar de los ",cantidad_productos," es de: ",valorpagar)

def costoproducto(valorproducto,cantidad):
    #Hacer una funcion que reciba el valor del producto y la cantidad y calcule el costo
    #Ese costo calculado enviarlo a otra funcion que calcule el descuento del 5% y ese
    #nuevo valor le saque el iva para calcular el valor total a pagar
    costoprod=valorproducto*cantidad
    return costoprod

def valortotal(a):
    descuento=a*0.05
    valor=a-descuento
    iva=valor*0.19
    valortotal=valor+iva
    print("El valor total a pagar es ",valortotal)

#cuerpo del programa
while True:
    menu()

    try:   
        opcion=int(input("\nIngrese el numero de la opcion escogida: "))
    except:
        opcion=-1
    
    if opcion==1:
        mayormenor()
    elif opcion==2:
        valorPagar()
    elif opcion==3:
        descuento()
    elif opcion==4:
        valorproducto=float(input("Digite el valor del producto: "))
        cantidad=int(input("Digite la cantidad a comprar: "))
        a=costoproducto(valorproducto,cantidad)
        valortotal(a)
    elif opcion==0:
        break
    else:
        print("\n La opcion ingresada es incorrecta, indica una opcion valida")
