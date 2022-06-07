#Hacer un programa que lea un nombre de un estudiante, lea tres notas y calcule la definitiva
nombre=input("Ingrese el nombre del estudiante: ")
num1=float(input("Ingrese la primera nota: "))
num2=float(input("Ingrese la segunda nota: "))
num3=float(input("Ingrese la tercer nota: "))

definitiva=(num1+num2+num3)/3

print("El nombre del estudiantes es: " + nombre)
print("La definitiva es: ", definitiva)