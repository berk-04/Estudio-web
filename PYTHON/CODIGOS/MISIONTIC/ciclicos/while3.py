#Hacer un programa para un supermercado en donde el cajero captura los precios
#de los articulos que los clientes compran e indica a cada cliente
#cual es el monto de lo que deben pagar. Al final del dia le indica a su supervisor
#cuanto fue lo que cobro en total a los 5 clientes que pasaron por la caja
totalclientes=0
for i in range(5):
    continuar="s"
    sumaprecio=0
    while continuar.lower()=="s":
        precio=float(input("Ingrese el valor del articulo: "))
        sumaprecio=sumaprecio+precio
        continuar=input("Desea comprar algun articulo, si lo desea marque s, sino escriba cualquier otra cosa: ")
    print("El valor a pagar del cliente "+ str(i+1),"es de: "+ str(sumaprecio))
    totalclientes=totalclientes+sumaprecio

print("El valor total vendido en el dia es de: ",totalclientes)
