a = [23.56,59,12,-85]
vehiculos  = ["Carro", "moto","camioneta","barco"]
animales=["perro","gato","conejo"]

print(a)
print(vehiculos)

print(3*vehiculos)

#mutabilidad
#Una lista es mutable porque se pueden modificar

subcadena=(" -- ")
print(subcadena.join(vehiculos))

animales.append("Caballo")
print(animales)

#Insert añadimos elementos en una posicion especifica

animales.insert(1,"vaca")
print(animales)

#extend puede añadir elementos a la lista pero de forma iterativa

animales.extend("lagartija")
print(animales)

n=len(animales)
print(n)

#pop quita un elemento de la lista

vehiculos.pop(2)
print(vehiculos)

#remove quita un elemento de la lista por el nombre

animales.remove("vaca")
print(animales)
