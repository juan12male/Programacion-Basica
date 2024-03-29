dineroRecaudado=0
numeroReservas=0
ingresoContrasena=""
contrasena="manejo25"
espacio=["vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio"]
listaUsuarios=[]
listaNombres=[]
nombre=input("Introduzca su nombre y primer apellido: ")
listaNombres.append(nombre)
usuario=input("Escriba su usuario: ")
listaUsuarios.append(usuario)
cedula=float(input("Escriba su número de identificación sin espacios y con los ceros:"))
correoElectronico=input("Ingrese su correo electronico: ")

def calcularCosto(curso, horas):
    costo_por_hora = 2000 if curso == 'teorico' else 3000
    return costo_por_hora * horas

def registroUsuario():
    curso = input("¿Qué curso desea tomar? (teorico/practico): ")

    if curso == 'practico':
        tipo_vehiculo = input("¿Utilizará vehículo propio o proporcionado? (propio/proporcionado): ")
        horas = int(input("¿Cuántas horas desea contratar? "))
        costo_total = calcularCosto(curso, horas)
        print(f" Costo total: {costo_total} colones")
    else:
        horas = int(input("¿Cuántas horas desea contratar? "))
        costo_total = calcularCosto(curso, horas)
        print(f"¡Registro exitoso! Costo total: {costo_total} colones")
    
    
def opcionesAdministrador():
    ingresoContrasena=input("Ingrese su contraseña de administrador: ")
    while ingresoContrasena != contrasena:
            print("Contraseña incorrecta. Por favor intente nuevamente.")
            break
            
    else:
        print("Bienvenido a sus opciones de administrador.")
        print("1. Ver dinero recaudado.\n2. Ver numero de reservas.")
        opcionAdmin=int(input("Ingrese la opcion deseada:"))
        if opcionAdmin == 1:
            print("El dinero recaudado es:",dineroRecaudado)
        elif opcionAdmin == 2:
            print("El numero de reservas es:",numeroReservas)

def facturaElectronica():
    nombre=input("Por favor ingrese su nombre: ")
    cedula=(input("Escriba su número de identificación sin espacios y con los ceros: "))
    correoElectronico=input("Ingrese su correo electronico: ")
    file=open("Factura","w")
    file.write("Factura a nombre de: "+nombre)
    file.write("\n")
    file.write("Numero de cedula: "+cedula)
    file.write("\n")
    file.write("Correo electronico: "+correoElectronico)
    file.write("\n")
    file.close()
    
def ingresarEspacio(espacio):
    while True:
        print("Seleccione el horario que le funcione: \n.Seleccione 4 para reservar de 8am a 9am\n.Seleccione 5 para reservar de 9am a 10am\n.Seleccione 6 para reservar de 10am a 11am\n.Seleccione 7 para reservar de 11am a 12md\n.Seleccione 8 para reservar de 12md a 1pm\n.Seleccione 9 para reservar de 2pm a 3pm\n.Seleccione 10 para reservar de 4pm a 5pm")
        horario = int(input("Ingrese el número de horario que prefiera:"))

        if horario >=4 and horario<=10:
            if espacio[horario-1] == "Vacio":
                espacio[horario-1]= nombre
                break
            else:
                print("El horario seleccionado se encuentra ocupado por",nombre)
        else:
            print("El horario seleccionado no existe")
    return espacio

def liberarHorario(espacio):
    while True:
        horario = int(input("Ingrese el numero de horario que selecciono:"))

        if horario >=4 and horario<=10:
            if espacio[horario-1] == "Vacio":
                print("El horario seleccioando esta vacio")
            else:
                espacio[horario-1]= "Vacio"
                print("El horario seleccionado anteriormente ha sido liberado")
                break
        else:
            print("El horario seleccionado no existe")
    return espacio

def mostrar(espacio):
    for x in range(len(espacio)):
        if espacio[x] == "Vacio":
            print("El horario",x+1,"esta vacio")
        else:
            print("El horario",x+1,"esta ocupado por:",espacio[x])
opcion =1

while opcion !=3:
    print("1.Reservar horario\n2.Liberar horario\n3.Salir")
    opcion = int(input("Seleccione la opción que desea:"))
    if opcion ==1:
        espacio = ingresarEspacio(espacio)
        mostrar(espacio)
    elif opcion ==2:
        espacio =liberarHorario(espacio)
        mostrar(espacio)
    elif opcion==3:
        print("Mucha gracias")
    else:
        print("Opcion incorrecta")

  
opcion = 0

while opcion != 5:
    print("1.Alguna prueba\n2.Dictamen médico\n3.Opciones de administrador\n4.Seleccionar horario clases de manejo")
    opcion=int(input("Seleccione la opción: "))
    if opcion==1:
        registroUsuario()
    elif opcion==2:
        facturaElectronica()
    elif opcion == 3:
        opcionesAdministrador()
    elif opcion==4:
        ingresarEspacio()
