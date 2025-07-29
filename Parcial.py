class Empleado:
    def Mostrar(self):
        i=1
        for codigo,dato in empleado.items():
            print(f"Empleado #{i}")
            print(f"El codigo es: {codigo} ")
            print(f"El Nombre es: {dato['nombre']}")
            print(f"La antiguedad en la empresa es: {dato['antiguedad']}")
            print(f"El departamento es: {dato['departamento']} ")
            for evalucion, dato in dato.items():
                print(f"La puntualidad es: {dato['puntualidad']}")
                print(f"El trabajo en equipo es: {dato['equipo']}")
                print(f"La productividad es: {dato['productividad']}")
                print()
            for contacto in dato['contactos']:
                print(f"La contacto es: {contacto}")
            i+=1


#class Evaluacion(Empleado):
    #def Promedio():




empleado = {}

empleadosnum = int(input("Introduzca el numero de empleados ha ingresar: "))
for i in range(empleadosnum):
    codigo = input("Introduzca el codigo del empleado: ")
    nombre = input("Introduzca el nombre del empleado: ")
    departamento = input("Introduzca el departamento: ")
    antiguedad = int(input("Introduzca el antiguedad (en años): "))
    empleado['codigo'] = {
        nombre : 'nombre',
        departamento : 'departamento',
        antiguedad : 'antiguedad'
    }

    print("Ingrese notas del 0 al 10 para las siguientes evaluaciones: ")
    puntualidad = int(input("Puntualidad: "))
    equipo = int(input("Trabajo en Equipo: "))
    productividad = int(input("Productividad: "))
    observaciones = input("Introduzca alguna(s) observaciones: ")

    empleado['codigo']['evaluacion'] = {
        puntualidad : 'puntualidad',
        equipo : 'equipo',
        productividad : 'productividad',
        observaciones : 'observaciones'
    }

    celular = int(input("Introduzca el celular: "))
    correo = input("Introduzca el correo: ")
    empleado['codigo']['contacto'] = {
        correo : 'correo',
        celular : 'celular'
    }
Empleado().Mostrar()


