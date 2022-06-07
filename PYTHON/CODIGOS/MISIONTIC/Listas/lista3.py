#Hacer un programa que utilice dos funciones y que cargue
#un diccionario con los productos de una venta.
#Por medio de las funciones calcule el precio unitario
#y el valor a pagar

import json

with open('Listas/productos.json') as file:
    tienda=json.load(file)


#funciones

def precioUnitario(nombre,precio,cantidad):
    valor=precio*cantidad
    return valor

def valorpagar(dic,descuento):
    total=0
    for i in dic:
        nombre=i['Nombre']
        precio=i['Precio']
        cantidad=i['Cantidad']
        total=total+precioUnitario(nombre,precio,cantidad)
    descuento=(total*descuento)/100
    total=total-descuento
    return total






#cuerpo del programa

print("El valor a pagar por la compra es: ", valorpagar(tienda['Producto'],10))