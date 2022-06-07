#Hacer un progrma que lea tres calificaciones de un estudiante
# y calcule su definitiva
#Si la definitiva es mayor a 4.5 debe imprimir sobresaliente
#Si la definitiva es mayor a 4 debe imprimir excelente
#Si la definitiva es mayor a 3 debe imprimir regular
#y si la definitiva es menor a 3 debe imprimir deficiente

a=float(input("Ingrese la primer nota: "))
b=float(input("Ingrese la segunda nota: "))
c=float(input("Ingrese la tercer nota: "))

definitiva=(a+b+c)/3
if definitiva>=4.5:
    print(str(round(definitiva,2))+ " - Su calificacion fue sobresaliente")
elif definitiva>=4 and definitiva<4.5:
    print(str(round(definitiva,2))+ " - Su calificacion fue excelente")
elif definitiva>3 and definitiva<4:
    print(str(round(definitiva,2))+ " - Su calificacion fue regular")
else:
    print(str(round(definitiva,2))+ " - Su calificacion fue deficiente")
