#Hacer un programa que calcule el iva de un producto y calcule
#el valor a pagar, el valor del producto debe ser enviado
# por argumento, utilizando una funcion.

def iva(a):
    valor_iva=costo*0.19
    valorpagar=costo+valor_iva
    print("El IVA del producto es: ",valor_iva)
    print("El valor a pagar es: ",valorpagar)

costo=float(input("Ingrese el valor del producto: "))  
iva(costo)