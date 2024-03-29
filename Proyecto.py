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
        def ingresarEspacio(espacio):
            while True:
                print("Seleccione el horario que le funcione:")
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
    

  
opcion = 0

while opcion != 4:
    print("1.Alguna prueba\n2.Dictamen médico\n3.Opciones de administrador")
    opcion=int(input("Seleccione la opción: "))
    if opcion==1:
        registroUsuario()
    elif opcion==2:
        facturaElectronica()
    elif opcion == 3:
        opcionesAdministrador()
