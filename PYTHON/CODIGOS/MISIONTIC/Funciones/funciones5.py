#hacer un programa que determine si un numero es positivo
#o negativo y si es par o impar

def parimpar(numero):
    if numero==0:
        print("El 0 es un número neutro")
    else:
        if numero>0:
            if numero%2==0:
                print("EL número ",numero," es par y positivo")
            else:
                print("EL número ",numero," es impar y positivo")
        else:
            if numero%2==0:
                print("EL número ",numero," es par y negativo")
            else:
                print("EL número ",numero," es impar y negativo")



numero=int(input("Digite un número: "))
parimpar(numero)