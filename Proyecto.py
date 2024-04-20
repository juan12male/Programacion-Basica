dineroRecaudado=0
numeroReservas=0
ingresoContrasena=""
contrasena="manejo25"
espacio=["vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio"]
listaUsuarios=[]
listaNombres=[]
nombre=input("Introduzca su nombre y primer apellido: ")
listaNombres.append(nombre)
usuario=input("Invente su usuario: ")
listaUsuarios.append(usuario)
cedula=float(input("Escriba su número de identificación sin espacios y con los ceros:"))
correoElectronico=input("Ingrese su correo electronico: ")
    
def clasesManejo(dineroRecaudado):
        tipoVehiculo = int(input("1.Propio\n2.Proporcionado\n¿Utilizará vehículo propio o proporcionado?:"))
        horas = int(input("¿Cuántas horas desea contratar? "))
        if horas > 1:
            print("Debe reservar al menos 1 hora")
        else:
            costoTotal=0
            if tipoVehiculo == 1:
                costoTotal=3000*horas
                dineroRecaudado+=costoTotal
                print("El costo es de: ",costoTotal)
            elif tipoVehiculo == 2:
                costoTotal=4000*horas
                dineroRecaudado+=costoTotal
                print("El costo es de: ",costoTotal)
            ingresarEspacio(espacio,nombre,numeroReservas)
            opcion=input("Desea factura electrónica?\n1.Sí\n2.No\n")
            if opcion == 1:
                facturaElectronica()
            else:
                print("Gracias por reservar su clases de manejo con nosotros!")
        
        return dineroRecaudado
        

    
def opcionesAdministrador(dineroRecaudado,numeroReservas):
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
    correoElectronico=input("Ingrese su correo electronico al que se envía la factura: ")
    direccionFisica=input("Por favor ingrese su dirección fisica: ")
    file=open("Factura","w")
    file.write("Escuela de manejo Racing")
    file.write("\nHeredia, Santa Cecilia, del Walmart, 1.3km al oeste, sobre carretera a la Aurora de Heredia")
    file.write("\n+506 8358-3536")
    file.write("\n")
    file.write("\n")
    file.write("Factura a nombre de: "+nombre)
    file.write("\n")
    file.write("Numero de cedula: "+cedula)
    file.write("\n")
    file.write("Correo electronico: "+correoElectronico)
    file.write("\n")
    file.write("Dirección fisica: "+direccionFisica)
    file.write("\n")
    file.close()
    
def ingresarEspacio(matriz,name,numeroReservas):
    while True:
        print("1.8am a 9am\n2.9am a 10am\n3.10am a 11am\n4.11am a 12md\n5.12md a 1pm\n6.2pm a 3pm\n7.4pm a 5pm")
        horario = int(input("Ingrese el número de horario que prefiera:"))
        if espacio[horario-1] == "vacio":
            espacio[horario-1]=nombre
            numeroReservas+=1
            break
        else:
            print("Horario ocupado")
            
            # elif horario == 2:
            #     if espacio[1] == "Vacio":
            #         espacio[1]=nombre
            #     else:
            #         print("Horario ocupado")
            # elif horario == 3:
            #     if espacio[2] == "Vacio":
            #         espacio[2]=nombre
            #     else:
            #         print("Horario ocupado")
            # elif horario == 4:
            #     if espacio[3] == "Vacio":
            #         espacio[3]=nombre
            #     else:
            #         print("Horario ocupado")
            
    return espacio


def liberarHorario(espacio,numeroReservas):
    while True:
        print("1.8am a 9am\n2.9am a 10am\n3.10am a 11am\n4.11am a 12md\n5.12md a 1pm\n6.2pm a 3pm\n7.4pm a 5pm")
        horario = int(input("Ingrese el número de horario que desea liberar:"))
        if espacio[horario-1] != "vacio":
            espacio[horario-1]="vacio"
            numeroReservas-=1
            break

def mostrar(matriz):
    print("1.8am a 9am\n2.9am a 10am\n3.10am a 11am\n4.11am a 12md\n5.12md a 1pm\n6.2pm a 3pm\n7.4pm a 5pm")
    for x in range(len(matriz)):
        if matriz[x] == "Vacio":
            print("El horario",x+1,"esta vacio")
        else:
            print("El horario",x+1,"esta ocupado por:",matriz[x])

def dictamenMedico():
    tipoSangre=input("Escriba su tipo de sangre: ")
    peso=int(input("Digite su peso en kilogramos: "))
    estatura=input("Digite su estatura en metros: ")
    donador=input("Desea ser donador de órganos en caso de muerte en un accidente de tránsito?n\Escriba si o no: ")
    print("La persona llamada",nombre,"con el número de cédula:",cedula,"tipo de sangre:",tipoSangre,"con un peso de",peso,"kilogramos, y una estatura de",estatura,"metros, hace constar en su dicatemen médico, que",donador,"desea ser donador/a de órganos.")


  
opcion = 0

while opcion != 6:
    print("1.Curso Teórico\n2.Clases de manejo\n3.Dictámen Médico\n4.Administrador\n5.Horarios disponibles")
    opcion=int(input("Seleccione la opción: "))
    if opcion==1:
        ingresarEspacio(espacio,nombre,numeroReservas)
    elif opcion==2:
        clasesManejo(dineroRecaudado,numeroReservas)
    elif opcion == 3:
        dictamenMedico()
    elif opcion==4:
        opcionesAdministrador(dineroRecaudado,numeroReservas)
    elif opcion == 5:
        mostrar(espacio)
