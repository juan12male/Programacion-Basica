#manejo de contraseña proyecto
contrasena="manejo25"
opcion=int(input("Ingrese la opcion deseada:"))

dineroRecaudado=0
numeroReservas=0
ingresoContrasena=""
    
if opcion == 3:
    while ingresoContrasena != contrasena:
        ingresoContrasena=input("Ingrese la contraseña de administrador:")
        print("Contraseña incorrecta. Por favor intente nuevamente.")
        
    else:
        print("Bienvenido a sus opciones de administrador.")
        print("1. Ver dinero recaudado.\n2. Ver numero de reservas.")
        opcionAdmin=int(input("Ingrese la opcion deseada:"))
        if opcionAdmin == 1:
            print("El dinero recaudado es:",dineroRecaudado)
        elif opcionAdmin == 2:
            print("El numero de reservas es:",numeroReservas)