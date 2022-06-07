#Hacer un  programa que determine cuantos hombres y mujeres se encuentran en un
#grupo de n personas

numpersonas=int(input("Ingrese el numero de personas: "))
hombres=0
mujeres=0
personas=1

for i in range(numpersonas):
    sexo=input("Ingrese su sexo, si es hombre marque 1, si es mujer marque 2: ")
    if sexo=="1":
        hombres=hombres+1
    elif sexo=="2":
        mujeres=mujeres+1
    else:
        print("Es incorrecto")
print("El numero de hombres es: ",hombres,
" y el numero de mujeres es: ",mujeres)

while  personas<=numpersonas:
    sexo=input("Ingrese su sexo: ")
    if sexo=="hombre":
        hombres=hombres+1 
        personas=personas+1   
    elif sexo=="mujer":
        mujeres=mujeres+1
        personas=personas+1
    else:
        print("Es incorrecto")
print("El número de hombres es: ", hombres,
" y el número de mujeres es de: ", mujeres)

masculino=0
femenino=0

seguir="S"

while seguir.lower()=="s":
    sexo=input("Digite su sexo (M o F): ")
    if sexo.lower()=="m":
        masculino=masculino+1
    elif sexo.lower()=="f":
        femenino=femenino+1
    else:
        print("Ese genero es invalido")
        break

    seguir=input("¿Desea seguir agregando generos?")

print("Hay " + str(masculino) + " hombres y " + str(femenino) +" mujeres")
