#Hacer un programa con cuatro funciones para calcular la devinitivs de un estudiante
#la cual se debe calcular asi:
#4 notas de quices
#3 notas de trabajos
# 2 notas de parciales
#calcular la definitiva por medio de una funcion

def quices():
    quices=0
    for i in range(4):
        notas=float(input("Ingrese la nota del quiz "+ str(i+1)+" : "))
        quices=quices+notas
    notaquices=quices/4
    return notaquices
def trabajos():
    trabajos=0
    for i in range(3):
        notas=float(input("Ingrese la nota del trabajo "+ str(i+1)+" : "))
        trabajos=trabajos+notas
    notatrabajos=trabajos/3
    return notatrabajos
def parciales():
    parciales=0
    for i in range(2):
        notas=float(input("Ingrese la nota del parcial "+ str(i+1)+" : "))
        parciales=parciales+notas
    notaparciales=parciales/2
    return notaparciales
def definitiva():
    definitiva=(quices()+trabajos()+parciales())/3
    print(round(definitiva,2))

definitiva()