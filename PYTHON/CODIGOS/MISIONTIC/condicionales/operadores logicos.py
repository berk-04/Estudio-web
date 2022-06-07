#operadores logicos
#and y
#or o
#not negacion
#T and F = F

from enum import Flag

print(True and False)
print(True or False)
print("----------------------")
x=5
y=5

print(x>5 or x==5)

print(not(x>5 or x==5))
print("----------------------")

#prioridad de los operadores

calculo=7-2*(13+5)
print(calculo)


print((3+6)*(8-2*4*(8/2)))