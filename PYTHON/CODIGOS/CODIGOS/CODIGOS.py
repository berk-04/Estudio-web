# num =int(input("Enter the range: "))
# for n in range(2,num):
#     for i in range(2,n):
#         if(n%i==0):
#             break
#     else:
#         print(n)  


# n=4
# for i in range(10,34):
#     print("Va al comienzo", end="")
#     if i==5:
#         print("Va a mitad de camino")
#     else:
#         print()
# n = int(input("Enter number: "))

# if(n == 0 or n < 0):
#     print("Value of n should be greater than 1")
# else:
#     fact = 1
#     while(n!=0):
#         fact *= n
#         n = n-1
#     print("Factorial is ",fact)


# n = int(input("Enter range: ")) 
# while(n!=0):
#     print(n, end=" ")
#     n = n - 1

# n = int(input("Enter range: ")) 
# while(n!=0):
#     print(n)
#     n = n - 1


# list=["pera",5,7]

# x,y,z = list

# print(x)
# print(y)
# print(z)


# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# for x in "banana":
#   print(x)

# txt = "The best things in life are free!"
# print("free" in txt)

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])


# n="yo que me alegro"

# m="hola que pasa chavales, todo bien, todo correcto y {}"

# print(m.format(n))


# a="apa hola\raasas"

# print(a)

# string=input("Ingrese una cadena de texto: ")
# string_1=input("Ingrese una cadena de texto: ")
# longitud_cadena=len(string)

# def first_middle_end(string,longitud_cadena):
#     mitad=longitud_cadena//2
#     a=string[0]+string[mitad]+string[longitud_cadena-1]
#     return a

# def three_middle(string,longitud_cadena):
#     mitad=longitud_cadena//2
#     print(string[mitad-1:mitad+2])

# def concatenate(string,string_1):
#     longitud_cadena=len(string)
#     longitud_cadena_1=len(string_1)
#     a=first_middle_end(string,longitud_cadena)
#     b=first_middle_end(string_1,longitud_cadena_1)
#     string=a[0]+b[0]+a[1]+b[1]+a[2]+b[2]
#     return string


# print(first_middle_end(string,longitud_cadena))
# three_middle(string,longitud_cadena)
# print(concatenate(string,string_1))


# def saludar():
#     print("hola")

# saludar()


a="hola"
b="paulina benjumea mejia"
print(len(a))

print(a[0])

print(a[4:])

print(a.upper())    
print(a.lower())
print(a.replace("la","LA"))
print(a.capitalize())
print(b.title())
print(b.encode())
m=b.split(" ")

a="texto"
b="Esto es un {0} de ayuda {2} {1} {4} {3}"

print(b.format(a,3,7,8,"hola"))

print(len(m))
