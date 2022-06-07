#Hacer un programa que calcule la definitiva de un estudiante

quiz1=float(input("Ingree la nota del primer quiz: "))
quiz2=float(input("Ingree la nota del segundo quiz: "))
quiz3=float(input("Ingree la nota del tercer quiz: "))
nota1=float(input("Ingree la nota del primer trabajo: "))
nota2=float(input("Ingree la nota del segundo trabajo: "))
parcial=float(input("Ingree la nota del parcial: "))

porcentajequices=((quiz1+quiz2+quiz3)/3)*0.4
porcentajenotas=((nota1+nota2)/2)*0.25
porcentajeparcial=parcial*0.35

notadefinitiva=porcentajequices + porcentajenotas + porcentajeparcial

print(notadefinitiva)


35
10
5

5
10
20

alto=float(input())
ancho=float(input())
profundo=float(input())

volumen=alto*ancho*profundo

costo=volumen*5

print(volumen)
print(costo)




