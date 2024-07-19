class Persona:
    def __init__(self, id, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def actualizar_datos(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono


class Cliente(Persona):
    def __init__(self, id, nombre, direccion, telefono, tipo):
        super().__init__(id, nombre, direccion, telefono)
        self.tipo = tipo
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, animal):
        self.animales.remove(animal)


class Empleado(Persona):
    def __init__(self, id, nombre, direccion, telefono, puesto, salario):
        super().__init__(id, nombre, direccion, telefono)
        self.puesto = puesto
        self.salario = salario

    def atender_cita(self, cita):
        cita.empleado = self


class Veterinaria:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        self.clientes = []
        self.empleados = []
        self.citas = []
        self.servicios = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def programar_cita(self, cita):
        self.citas.append(cita)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)


class Animal:
    def __init__(self, id, nombre, raza, edad, cliente):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.cliente = cliente

    def actualizar_historia(self, historial):
        self.historial = historial


class Cita:
    def __init__(self, id, fecha, cliente, animal, empleado, servicio):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente
        self.animal = animal
        self.empleado = empleado
        self.servicio = servicio

    def confirmar(self):
        print(f"Cita {self.id} confirmada.")

    def cancelar(self):
        print(f"Cita {self.id} cancelada.")


class Servicio:
    def __init__(self, id, nombre, descripcion, costo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo

    def actualizar_costo(self, costo):
        self.costo = costo


class Vacuna:
    def __init__(self, tipo):
        self.tipo = tipo

    def administrar_vacuna(self):
        print(f"Vacuna {self.tipo} administrada.")


class Consulta:
    def __init__(self, duracion):
        self.duracion = duracion

    def realizar_consulta(self):
        print("Consulta realizada.")
