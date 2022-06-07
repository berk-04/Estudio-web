#Hacer un programa que registre los partidos de futbol de la Uis.

def menu():
    print("\n")
    print(" PROGRAMA PARA REGISTRO DE PARTIDOS UIS ")
    print("------------------------")
    print("\n selecciona una opcion")
    print("\n 1 - REGISTRAR PARTIDO ")
    print("\n 2 - VER RESULTADO ")
    print("\n 3 - TABLA CLASIFICACION ")
    print("\n 0  - salir ")
    print("\n")
    
def entrarDia():
    while True:
        try:
            print("\n")
            print("  * INGRESE LA FECHA DEL PARTIDO *")
            print("\n")
            dia=int(input("DIGITE EL DIA (1-31): "))
            if dia>0 and dia<32:
                return dia
            else:
                print(" DEBE INGRESAR UN DIA VALIDO  !!! ")
        except:
            print("el dia debe tener un valor numerico")
            
def entrarMes ():
    while True:
        try:
            mes=int(input("DIGITE EL MES (1-12): "))
            if mes>0 and mes<13:
                return mes
            else:
                print("DEBE INGRESAR UN MES VALIDO  !!! ")
        except:
            print("el mes  debe tener un valor numerico")
            
def entrarAño ():
    while True:
        try:
            año=int(input("DIGITE UN AÑO MAYOR A 2021 (>2021) : "))
            if año>=2022:
                return año
            else:
                print("DEBE INGRESAR UN AÑO VALIDO  !!! ")
        except:
            print("el año  debe tener un valor numerico")

def entrarRival ():
    while True :
        rival=input("INGRESE EL NOMBRE  DEL EQUIPO RIVAL: ")
        if rival =="":
            print("EL NOMBRE  NO PUEDE ESTAR VACIO !!! ")
        else:
            return rival

 
def entrarGolRival():
    while True:
        try:
            golrival=int(input("INGRESE  LOS GOLES DEL EQUIPO RIVAL : "))
            if golrival>=0:
                return golrival
            else:
                print("NO PUEDE INGRESAR VALORES NEGATIVOS !!! ")
        except:
            print("EL GOL DEBE TENER UN VALOR NUMERICO ")       
            
def entrarGolUis():
    while True:
        try:
            goluis=int(input("INGRESE  LOS GOLES DE LA UIS : "))
            if goluis>=0:
                return goluis
            else:
                print("NO PUEDE INGRESAR VALORES NEGATIVOS !!! ")
        except:
            print("EL GOL DEBE TENER UN VALOR NUMERICO ")



#cuerpo del programa
partidos=[]

while True:
    menu()
    try:
        opcion=int(input("\n ingrese el numero de la opcion escogida:" ))
    except:
        opcion=-1
        
    if opcion==1:
        resp="s"
        while resp=="s" or resp=="S":
            partidos.append([entrarDia(), entrarMes(), entrarAño(), entrarRival(), entrarGolRival(), "UIS", entrarGolUis()])
            resp=input("\n ¿ DESEA REGISTRAR OTRO PARTIDO ? (s/n) : ")
        print(partidos)
        
    #elif opcion==2:
        
    #elif opcion==3:
        
    #elif opcion==4:
        
   # elif opcion==0:
        break
    else:
        print("\n  la opcion ingresada es incorrecta")