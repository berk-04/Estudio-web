#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzeria Bella Napoli. \nTipos de pizza: \n\t1- Vegetariana \n\t2- No vegetariana\n")

tipopizza=input("Introduce el número correspondiente al número de pizza que quieres: ")

if tipopizza=="1":
    print("\tMENÚ \n\t1- Pimiento \n\t2- Tofu\n")
    ingrediente=input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozarella, tomate y ",end="")
    if ingrediente=="1":
        print("Pimiento")
    else:
        print("Tofu") 
else:
    print("\tMENÚ \n\t1- Peperoni \n\t2- Jamón \n\t3- Salmón\n")
    ingrediente=input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozarella, tomate y ",end="")
    if ingrediente=="1":
        print("Peperoni")
    elif ingrediente=="2":
        print("Jamón")
    else:
        print("Salmón")
