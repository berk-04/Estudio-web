def multiplicarNumeros(lista):
    resultado=1
    for i in lista:
        resultado=resultado*i
    return resultado

print(multiplicarNumeros([2,3,5]))
print(multiplicarNumeros([2,2,2]))