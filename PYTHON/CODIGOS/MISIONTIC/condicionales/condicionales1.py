#Hacer un programa que lea la edad de una persona y determine si es mayor o menor de edad

edad=int(input("Ingrese su edad: "))

if edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")



password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
else:
    print('Tu contraseña es muy corta e insegura.')

    if (password != 'miClaveSegura'):
        print("Además, es incorrecta (por supuesto).")
