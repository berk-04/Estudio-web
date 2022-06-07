print("Hola mundo")

#Tipos de datos

a = 5        # int = entero
b ="Hola"    # str = string-cadena
c = 3.12     # float = flotante-decimal
d = True     # bool = booleano- true o false


#Operadores

#Operadores aritmeticos

print(2+2)    # + suma
print(5-3)    # - resta
print(4*5)    # * multiplicacion
print(15/4)    # / divison
print(15//4)    # // division entera
print(2**3)    # ** exponenciacion
print(13%3)    # % modulo-residuo

#Nota: la función print sirve para imprimir por pantalla

#Operadores de comparación

3 == 3      # == igual que
3 != 3      # != diferente que
4 > 3       # >  mayor que
5 < 6       # <  menor que
7 >= 3      # >= mayor o igual que
9 <= 5      # <= menor o igual que

#Operadores logicos

# and
# or
# not

x=3

if x==3 and x<4:
    x **=3
    print(x)
else:
    print("nada")

#Operadores de asignacion

a = 3     # = igual asigna un valor a una variable
a += 9    # += incremento
a -= 45    # -= Decremento
a **= 4   # **= exponenciacion
a /= 7    # /= Division
a //= 1   # //= Division entera
a %= 1    # %= modulo
a *= 1    # *= multiplicacion



#Para pedir un dato por teclado utilizamos la funcion input()

a = input()

#Debemos tener en cuenta que cuando ingresamos un dato por pantalla
#el tipo de dato es string por lo que en algunos momentos debemos convertirlo a otro tipo de dato asi:

a= int(input("Ingrese un numero: "))     #Dentro de los parentesis del input podemos poner entre comillas lo que
                                         #queremos que el usuario vea

#Tambien podemos pasar de un tipo de dato a otro asi:

a = 3   #En este caso sabemos que a es un dato tipo entero y lo debemos pasar a un string

print(type(a))              #La funcion type nos arroja el tipo de dato de la variable
a = str(a)
print(type(a))



#Estructuras condicionales

#La estructura basica deriva de tres intrucciones basicas: if, elif y else.

num=int(input("Ingrese un número: "))

if num<100:
    print("Es un numero de dos cifras")
elif num>=100 and num<1000:
    print("Es un numero de tres cifras")
else:
    print("Es un numero de cuatro cifras")

#Condicionales anidados

if num<100:
    if num%2==0:
        print("Es un número par menor que 100")
    else:
        print("Es un numero impar menor que 100")
else:
    if num%2==0:
        print("Es un número par mayor que 100")
    else:
        print("Es un numero impar mayor que 100")

#Nota: Realizar esto en caso de ser necesario puesto que muchas
#veces es mucho mas facil utilizar los operadores logicos



#Variables de control y ciclos iterativos

#Variables de control

#Banderas

# la bandera o flag se refiere a uno o más bits que se utilizan para almacenar
#un valor binario o código que tiene asignado un significado.
#Es decir puede indicarnos un punto de salida y un punto de llegada.

suma_realizada = False
total=8
a=5
b=10
if suma_realizada ==False:
    total=a+b
    suma_realizada=True

if suma_realizada == True:
    print("La suma es ",total)


#Acumuladores

#Como su nombre lo indica nos permite acumular procesos

#Contadores

#Del mismo modo que los acumuladores nos permiten contar el numero 
#de veces que se realiza o ejecuta el codigo

#Ciclos iterativos

#En los ciclo utilizamos el ciclo While o el ciclor For

manzanas=5
contador=0

while contador<5:
    print("Se añadio la ",(contador+ 1), " manzana al carrito")
    contador +=1

for i in range(manzanas):
    print("Se añadio la ",(i+ 1), " manzana al carrito")



#Funciones

#una funcion es un bloque de codigo que recibe o no una serie de argumentos(parametros) de entrada
#que siguen una serie de instrucciones especificas y que retornan un valor

#Estructura

# def <nombre_function> <argumentos>:
#        <secuencia de instrucciones>
#        <retorno>

#Funciones y modulos predefinidos en python

#los modulos predefinidos son todos aquellos que tienen metodos predefinidos en si mismos (es decir funciones)
#a esto tambien lo llamamos librerias, las cuales podemos importar utilizando la funcion import.
#Para importar elementos dentro del modulo utilizamos la funcion from, asi:

# from <nombre_del_modulo> import <nombre_elemento>

#algunos modulos serian os, glob, sys, math, random, datetime

saludo="ama"
print(saludo.count("a"))   #Cuenta cuantos caracteres hay en una cadena

print(saludo.find("a"))    #Busca la posicion primera de un caracter en una cadena

#Imagen en whatsapp

print()      #Nos permite imprimir por pantalla
help()       #Nos permite ver para que sirven las funciones
sorted()     #Nos permite ordenar una lista en orden ascendente
min()        #Nos permite hallar el minimo elemento en una lista
max()        #Nos permite hallar el maximo elemento en una lista
len()        #Nos permite hallar la longitud de una lista
#sqrt()       #Nos permite hallar la raiz cuadrada de un numero
input()      #Nos permite ingresar por teclado un dato
dir()        #Ayuda Kevin
type()       #Nos permite saber el tipo de dato de una variable o valor


#Modulo OS

#Nos permite interactuar con el sistema operativo

import os

os.getcwd()

os.path.isfile()       # o tambien isdir




#Colecciones de datos

#conjuntos(Set)  Coleccion de datos que tiene elementos que se repiten
#Listas(list) Coleccion de datos que tienen elementos que se pueden repetir
#Tuplas(tuple) Lista que no se puede modificar despues de su creacion
#Diccionarios Define los datos uno a uno entre un campo y un valor

