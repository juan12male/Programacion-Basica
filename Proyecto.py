dineroRecaudado=0
numeroReservas=0
ingresoContrasena=""
contrasena="manejo25"
nombre=input("Introduzca su nombre y primer apellido: ")
usuario=input("Escriba su usuario: ")
cedula=float(input("Escriba su número de identificación sin espacios y con los ceros:"))
correoElectronico=input("Ingrese su correo electronico: ")

def calcular_costo(curso, horas):
    costo_por_hora = 2000 if curso == 'teorico' else 3000
    return costo_por_hora * horas

def registro_usuario():
    curso = input("¿Qué curso desea tomar? (teorico/practico): ")

    if curso == 'practico':
        tipo_vehiculo = input("¿Utilizará vehículo propio o proporcionado? (propio/proporcionado): ")
        horas = int(input("¿Cuántas horas desea contratar? "))
        costo_total = calcular_costo(curso, horas)
        print(f" Costo total: {costo_total} colones")
    else:
        horas = int(input("¿Cuántas horas desea contratar? "))
        costo_total = calcular_costo(curso, horas)
        print(f"¡Registro exitoso! Costo total: {costo_total} colones")
    
    def opcionesAdministrador():

opcion =0
while opcion != 4:
    print("1.Alguna prueba\n2.Dictamen médico\n3.Opciones de administrador")
    opcion=int(input("Seleccione la opción: "))
    if opcion==1:
        registro_usuario()
    elif opcion==2:
        break
    elif opcion == 3:
        









