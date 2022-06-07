#Una drogueria tiene una promocion segun el color de la balota
#que saque el usuario, segun el valor de la compra realizada.
#Si la balota es de color rojo tiene un descuento del 
#20% si la compra es mayor a 100 mil.
#Si la balota es de color azul tiene un descuento del 
#15% si la compra es mayor a 100 mil
#Si la balota es de color verde tiene un descuento del 
#8% si la compra es mayor a 100 mil
#Si la balota es de color blanco tiene un descuento del 
#10% si la compra es mayor a 100 mil

balota=input("Ingrese el color de la balota: ")
compra=float(input("Ingrese el valor de la compra: "))

if balota.lower() == "rojo":
    if compra>100000:
        descuento=compra*0.2
        valorpagar=compra-descuento
    else:
        descuento=0
        valorpagar=compra-descuento
elif balota.lower() == "azul":
    if compra>100000:
        descuento=compra*0.25
        valorpagar=compra-descuento
    else:
        descuento=0
        valorpagar=compra-descuento
elif balota.lower() == "verde":
    if compra>100000:
        descuento=compra*0.8
        valorpagar=compra-descuento
    else:
        descuento=0
        valorpagar=compra-descuento
elif balota.lower=="blanco":
    descuento=compra*0.1
    valorpagar=compra-descuento
else:
    print("No obtiene ningun descuento.")
print("El descuento es de: ",descuento,". El valor a pagar es de: ",valorpagar)