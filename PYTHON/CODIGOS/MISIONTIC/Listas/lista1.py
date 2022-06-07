def sumatoria(lista):
    suma=0
    for i in lista:
        suma=suma+i
    return suma

def numerosMenores(lista,limite):
    newlist=[]
    for n in lista:
        if n<limite:
            newlist.append(n)
    return newlist

#Hacer un programa que solicite al usuario que ingrese numeros, los cuales se deben
#guardar en una lista. Finalizar al ingresar el numero 0, el cual no 
#debe guardarse.

numeros=[]
numero=int(input("Ingrese numeros: "))
while numero != 0:
    numeros.append(numero)
    numero=int(input("Ingrese otro numero: "))

print(numeros)

#a continuacion, solicitar al usuario que ingrese un numero y si el numero esta en la lista
#eliminar su primero ocurrencia. Mostrar un mensaje
#si no es posible eliminar

eliminar=int(input("Ingrese numero a eliminar: "))

if eliminar in numeros:
    numeros.remove(eliminar)
    print(numeros)
else:
    print("Ese numero no esta en la lista")

#imprimir la sumatorio de todos los numeros de la lista

print("La sumatoria de los numero es: ", sumatoria(numeros))

a=len(numeros)
print("La cantidad de elementos de la lista es: ", a)

#print(sorted(a,reverse=True))

#solicitar al usuario otro numero y crear una lista con los elementos de la lista original
#que sean menores que el numero digitado. Imprimir esta nueva lista,iterando con ella.

limite=int(input("Filtrar numeros menores a: "))

for i in numerosMenores(numeros,limite):
    print(i)

