#ejemplo practico de una bandera tipo string o cadena

contagio_valido="No"
paciente="Juan"

if contagio_valido=="No":
    print("El paciente ", paciente, "aun no se ha realizado su prueba para validar" +
    "si se encuentra contagiado, se recomienda aplicar la prueba PCR")
    print("Aplicando prueba...")
    contagio_valido="Pendiente"

if contagio_valido=="Pendiente":
    print(paciente, ", por favor valide en su correo el resultado de la prueba ")
    contagio_valido="Si"

if contagio_valido=="Si":
    print(paciente, ", de acuerdo a su resultado por favor mantengase alejado de las personas")