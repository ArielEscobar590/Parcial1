#class Empleado:
    # def Mostrar(self):



#class Evaluacion(Empleado):
    #def Promedio():


empleado = {}
#em = Empleado()
empleadosnum = int(input("Introduzca el numero de empleados ha ingresar: "))
for i in range(empleadosnum):
    codigo = input("\nIntroduzca el codigo del empleado: ")
    nombre = input("Introduzca el nombre del empleado: ")
    departamento = input("Introduzca el departamento: ")
    antiguedad = int(input("Introduzca el antiguedad (en años): "))
    celular = int(input("Introduzca el celular: "))
    correo = input("Introduzca el correo: ")
    print("\nIngrese notas del 0 al 10 para las siguientes evaluaciones: ")
    puntualidad = int(input("Puntualidad: "))
    equipo = int(input("Trabajo en Equipo: "))
    productividad = int(input("Productividad: "))
    observaciones = input("Introduzca alguna(s) observaciones: ")


    empleado[codigo] = {
        nombre : 'nombre',
        departamento : 'departamento',
        antiguedad : 'antiguedad',
        puntualidad : 'puntualidad',
        equipo : 'equipo',
        productividad : 'productividad',
        observaciones : 'observaciones',
        celular : 'celular',
        correo : 'correo'
    }

i = 1
for codigo,dato in empleado.items():
    print(f"\nEmpleado #{i}")
    print(f"El codigo es: {codigo} ")
    print(f"El Nombre es: {dato['nombre']}")
    print(f"La antiguedad en la empresa es: {dato['antiguedad']}")
    print(f"El departamento es: {dato['departamento']} ")
    print(f"La puntualidad es: {dato['puntualidad']}")
    print(f"El trabajo en equipo es: {dato['equipo']}")
    print(f"La productividad es: {dato['productividad']}")
    print(f"El Telefono es: {dato['telefono']}")
    print(f"El Correo es: {dato['correo']}")
    i += 1


