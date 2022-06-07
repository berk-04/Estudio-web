def procesar_dato(peso, volumen):
    if peso < 2:
        if volumen < 0.027:
            return True
        else:
            return False
    else:
        return False

# print(procesar_dato(5, 3))

from posixpath import split


def par_impar(numero):
    if numero%2 == 0:
        return True
    else:
        return False

print (par_impar(24))
print (par_impar(33))


def peso_a_euro(pesos):
    euros=pesos/4500
    return euros


print (peso_a_euro(10000))
print (peso_a_euro(50000))
