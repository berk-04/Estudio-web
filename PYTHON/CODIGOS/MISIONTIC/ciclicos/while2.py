# #Obtener el promedio de calificaciones de un grupo de n estudiantes

# #variable acumuladora
# notas=0
# #variable contador
# estudiantes=0

# continuar="s"

# while continuar.lower()=="s":
#     nota=float(input("Digite la nota del estudiante: "))
#     notas=notas+nota
#     estudiantes=estudiantes+1

#     continuar=input("digita s si quiere continuar agregando notas de estudiantes, o" 
#     "cualquier caracter para finalizar: ")

# promedio=notas/estudiantes

# print("El promedio de los ", estudiantes, " estudiantes es: ", promedio)

numestudiantes=int(input("Ingrese la cantidad de estudiantes: "))
notas=0

for i in range(numestudiantes):
    nota=float(input("Ingrese la nota del estudiante: "))


