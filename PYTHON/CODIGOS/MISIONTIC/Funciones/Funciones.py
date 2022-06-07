#Funciones

#Max() nos permite hallar el maximo numero en una lista
#Sorted() nos permite retornar una lista ordenada
#len() nos permite medir la longitud de un objeto

# caracteres='hola'
# print(caracteres.capitalize())

# caracteres = 'asombroso'
# valor ='o'
# print(caracteres.count(valor))

# caracteres= "Hola a todos, bienvenidos a este curso"
# valor="este"
# print(caracteres.find(valor))

# caracteres= "2 3 1 6 4 5"
# print(caracteres.split("1"))
# caracteres= "datos.text"
# print(caracteres.split("."))

# cadena="Hola {}, ¡bienvenido a este curso de {}!"
# nombre="Juan"
# curso="Python"
# print(cadena.format(nombre,curso))

# cadena="Hola {1}, ¡bienvenido a este curso de {0}!"
# nombre="Juan"
# curso="Python"
# print(cadena.format(curso,nombre))

# letras="abcdefg"
# delimitador=","
# print(delimitador.join(letras))

# letras=["Hola", "como", "estas"]
# delimitador=" "
# print(delimitador.join(letras))

# frase="Hola que mas pues"
# print(frase.replace("Hola","Hi"))

# palabra1="Estado"
# palabra2="estado"
# print(palabra1.casefold()==palabra2.casefold())

def digahola():
    print("Hello!!")

def holaconnombre(name):
    print("Hello "+ name + "!!!")

digahola()
holaconnombre("Juan Esteban")