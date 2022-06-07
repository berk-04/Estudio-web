#Ejemplo practico de una bandera booleana

suma_realizada=False
total=0
a=10
b=15
total=a+b
if total>=20:
    if(suma_realizada==False):
        suma_realizada=True

if suma_realizada==True:
    print("Se ha realizado la suma y su valor es ", total)

else:
    print("No se cambio la bandera")