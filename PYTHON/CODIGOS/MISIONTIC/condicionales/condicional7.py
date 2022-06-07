#Hacer un programa para calcular el impuesto para una persona 
#que debe de ser mayor de 18 años y tener unos ingresos iguales o
#superiores a 2 M mensuales.
#Preguntar al usuario la edad, los ingresos y determine si debe pagar impuesto o no

edad=int(input("Ingrese su edad: "))
ingreso=int(input("Ingrese su salario: "))

if edad>= 18 and ingreso>=2000000:
    print("Usted paga impuestos")
else:
    print("Usted no paga impuestos")