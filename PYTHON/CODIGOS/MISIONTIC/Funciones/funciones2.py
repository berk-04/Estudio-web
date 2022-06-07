#Hacer un programa que calcule el iva de un producto y calcule
#el valor a pagar, utilizando una funcion




def iva():
    costo=float(input("Ingrese el valor de la compra: "))
    valor_iva=costo*0.19
    valorpagar=costo+valor_iva
    print("El IVA del producto es", valor_iva)
    print("El valor a pagar es: ", valorpagar)
    
iva()
iva()