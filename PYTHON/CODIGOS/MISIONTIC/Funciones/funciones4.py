# Hacer un programa que determine si una persona es mayor o menor de edad,
# por medio de una funcion.

def edad():
    nombre=input("Ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    if edad>=18:
        print(nombre," tiene una edad de ",edad," años, asi que es mayor de edad")
    else:
        print(nombre," tiene una edad de ",edad," años, asi que es menor de edad")

edad()