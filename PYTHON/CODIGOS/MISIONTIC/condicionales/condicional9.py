#Hacer un programa que tenga en cuenta los rangos impositivos para la declaracion de renta:
#menos de 10 M: 5%
#entre 10 M y 20 M: 15%
#entre 20 M y 35 M: 20%
#entre 35 M y 60 M: 30%
#mas de 60 M: 45%
#El usuario debe digitar su renta anual y muestre por pantalla
#el tipo impositivo y el valor a pagar

renta=int(input("Ingrese su renta anual: "))

if renta<10000000:
    tipo="5%"
    impuesto=renta*0.05
elif renta<20000000:
    tipo="15%"
    impuesto=renta*0.15
elif renta<35000000:
    tipo="20%"
    impuesto=renta*0.2
elif renta<60000000:
    tipo="30%"
    impuesto=renta*0.3
else:
    tipo="45%"
    impuesto=renta*0.45
print("El tipo impositivo es de: ",tipo, ", la renta es de: ",renta, ", el valor a pagar es de: ",impuesto)