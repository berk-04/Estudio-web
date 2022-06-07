#Hacer un programa que calcule el promedio de un alumno que tiene 3 calificaciones
#de quices, 4 calificaciones de trabajos y dos
#calificaciones de parciales

quices=0
trabajos=0
parciales=0

for i in range(3):
    nota=float(input("Ingrese la nota del quiz "+ str(i+1) + ": "))
    quices=quices+nota
for i in range(4):
    nota=float(input("Ingrese la nota del trabajo "+ str(i+1) + ": "))
    trabajos=trabajos+nota
for i in range(2):
    nota=float(input("Ingrese la nota del parcial "+ str(i+1) + ": "))
    parciales=parciales+nota

promedioquices=quices/3
promediotrabajos=trabajos/4
promedioparciales=parciales/2

promediogeneral=(promedioquices+promediotrabajos+promedioparciales)/3
print("Su promedio general es de: ", round(promediogeneral,2))
