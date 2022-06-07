#Hacer un programa que calcule el promedio de un alumno que tiene 7 calificaciones

suma=0
nombre=input("Ingrese su nombre: ")

for i in range(7):
    nota=float(input("Ingrese la nota "+ str(i+1) + ": "))
    suma=suma+nota

promedio=suma/7
print("El estudiante con nombre", nombre,", Saco un promedio de: ", round(promedio, 2))