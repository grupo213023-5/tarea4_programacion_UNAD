"""
main es el archivo de ejecución, en el importamos cliente, servicio, sistema y logger
para trabajar las clases y sus funcionalidades que definimos en los archivos por separado, debe
mostrar un menú de opciones que reciba datos del usuario para registrar y hacer posteriormente la gestión
de los clientes, los servicios y las reservas del sistema llamando las funciones del mismo y controlando el
flujo general sin que se detenga aun si se presentan errores
Hacemos uso de try-except para el control de excepciones del sistema
"""

from cliente import Cliente
from servicio import *
from sistema import SistemaGestion
from logger import Logger

sistema = SistemaGestion()

# =========================
# FUNCIONES AUXILIARES
# =========================

def mostrar_menu():                                 # Función del menú: muestra las opciones del menú

    print("""
    ===================================
           SOFTWARE FJ
    Sistema de Gestión Empresarial
    ===================================

    1. Registrar cliente
    2. Crear servicio sala
    3. Crear servicio equipo
    4. Crear asesoría
    5. Crear reserva
    6. Listar reservas
    7. Simulación automática
    0. Salir
    """)


# =========================
# REGISTRO CLIENTE
# =========================

def registrar_cliente():                            # Función para crear al cliente: Solicita información y crea un cliente

    try:

        # Registra los datos ingresados por teclado del usuario
        documento = input("Documento: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        cliente = Cliente(
            documento,
            nombre,
            correo
        )

        sistema.registrar_cliente(cliente)          # Llama al método del objeto
                                                    # Sistema es la instancia de la clase

        print("Cliente registrado correctamente")

    except Exception as e:                          # Captura cualquier error mientras se ejecuta
                                                    # almacena el error en la variable e

        Logger.registrar_error(e)                   # Guarda el error en el archivo logs.txt
                                                    # Muestra el historial de errores

        print(f"Error creando cliente: {e}")

        return


# =========================
# CREAR SERVICIO SALA
# =========================

# Se crea una sucesion de codigo ahora con la funcion para crear la sala
# Registramos los datos ingresados por el usuario y hacemos el llamado de la instancia de la clase
# Capturamos los errores y mostramos en pantalla
def crear_sala():

    try:

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        capacidad = int(input("Capacidad: "))

        sala = ReservaSala(
            codigo,
            nombre,
            precio,
            capacidad
        )

        sistema.agregar_servicio(sala)

        print("Sala creada")

    except Exception as e:

        Logger.registrar_error(e)

        print(f"Error: {e}")


# =========================
# CREAR SERVICIO EQUIPO
# =========================

def crear_equipo():

    try:

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        tipo = input("Tipo equipo: ")

        equipo = AlquilerEquipo(
            codigo,
            nombre,
            precio,
            tipo
        )

        sistema.agregar_servicio(equipo)

        print("Equipo creado")

    except Exception as e:

        Logger.registrar_error(e)

        print(f"Error: {e}")


# =========================
# CREAR ASESORÍA
# =========================

def crear_asesoria():

    try:

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        especialista = input("Especialista: ")

        asesoria = AsesoriaEspecializada(
            codigo,
            nombre,
            precio,
            especialista
        )

        sistema.agregar_servicio(asesoria)

        print("Asesoría creada")

    except Exception as e:

        Logger.registrar_error(e)

        print(f"Error: {e}")


# =========================
# CREAR RESERVA
# =========================

def crear_reserva():

    try:

        if not sistema.clientes:
            print("No hay clientes")
            return

        if not sistema.servicios:
            print("No hay servicios")
            return

        print("\nCLIENTES")

        for i, cliente in enumerate(sistema.clientes):

            print(
                i,
                cliente.get_nombre()
            )

        indice_cliente = int(
            input("Seleccione cliente: ")
        )

        print("\nSERVICIOS")

        for i, servicio in enumerate(sistema.servicios):

            print(
                i,
                servicio.nombre
            )

        indice_servicio = int(
            input("Seleccione servicio: ")
        )

        duracion = int(
            input("Duración: ")
        )

        reserva = sistema.crear_reserva(
            sistema.clientes[indice_cliente],
            sistema.servicios[indice_servicio],
            duracion
        )

        if reserva:

            reserva.confirmar()

            reserva.procesar()

            print("Reserva completada")

    except Exception as e:

        Logger.registrar_error(e)

        print(f"Error: {e}")


# =========================
# SIMULACIÓN AUTOMÁTICA
# =========================

def simulacion():

    print("""
    ===================================
         SIMULACIÓN AUTOMÁTICA
    ===================================
    """)

    operaciones = 0

    # =========================
    # CLIENTES VÁLIDOS
    # =========================

    # Creamos una lista que almacene varios registros de clientes
    # Para esta simulación agrupamos los datos en tuplas para una mejor organizacion
    datos_validos = [

        ("10001", "Carlos Ramirez", "carlos@gmail.com"),

        ("10002", "Laura Torres", "laura@gmail.com"),

        ("10003", "Andres Perez", "andres@gmail.com")

    ]

    # Usamos un ciclo for para recorrer la lista, debe tomar la tupla y separar valores automaticamente
    # Muestra el resultado ordenado evitando errores como iteración
    # LLama al archivo cliente.py y valida el documento y se construye un objeto completo
    # Guarda al cliente en memoria
    for doc, nom, correo in datos_validos:

        try:

            cliente = Cliente(doc, nom, correo)

            sistema.registrar_cliente(cliente)

            print(f"Cliente válido -> {nom}")

            operaciones += 1                                        # Contador de operaciones, incrementa el contador

        except Exception as e:                                      # Captura cualquier error
                                                                    # Nos permite saber cuantas operaciones se ejecutaron

            print(e)

    # =========================
    # CLIENTES INVÁLIDOS
    # =========================

    datos_invalidos = [

        ("abc", "Juan", "juan@gmail.com"),

        ("100", "A", "correo_mal"),

        ("", "", "")

    ]

    for doc, nom, correo in datos_invalidos:

        try:

            cliente = Cliente(doc, nom, correo)

            sistema.registrar_cliente(cliente)

        except Exception as e:

            Logger.registrar_error(e)

            print(f"Cliente inválido -> {e}")

            operaciones += 1

    # =========================
    # SERVICIOS CORRECTOS
    # =========================

    try:

        sala = ReservaSala(
            "S01",
            "Sala Premium",
            200000,
            20
        )

        sistema.agregar_servicio(sala)

        print("Servicio válido -> Sala")

        operaciones += 1

    except Exception as e:

        print(e)

    # =========================
    # SERVICIO INCORRECTO
    # =========================

    try:

        servicio_malo = ReservaSala(
            "S02",
            "Sala Defectuosa",
            -5000,
            10
        )

    except Exception as e:

        Logger.registrar_error(e)

        print(f"Servicio inválido -> {e}")

        operaciones += 1

    # =========================
    # RESERVA VÁLIDA
    # =========================

    try:

        reserva = sistema.crear_reserva(
            sistema.clientes[0],
            sistema.servicios[0],
            3
        )

        if reserva:

            reserva.confirmar()

            reserva.procesar()

            print("Reserva válida")

            operaciones += 1

    except Exception as e:

        print(e)

    # =========================
    # RESERVA INVÁLIDA
    # =========================

    try:

        reserva_error = sistema.crear_reserva(
            sistema.clientes[0],
            sistema.servicios[0],
            -2
        )

    except Exception as e:

        Logger.registrar_error(e)

        print(f"Reserva inválida -> {e}")

        operaciones += 1

    print(f"""
    ===================================
    Operaciones ejecutadas: {operaciones}
    Simulación finalizada
    ===================================
    """)


# =========================
# BUCLE PRINCIPAL
# =========================

while True:

    try:

        mostrar_menu()

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            crear_sala()

        elif opcion == "3":
            crear_equipo()

        elif opcion == "4":
            crear_asesoria()

        elif opcion == "5":
            crear_reserva()

        elif opcion == "6":
            sistema.listar_reservas()

        elif opcion == "7":
            simulacion()

        elif opcion == "0":

            print("Saliendo del sistema")

            break

        else:

            print("Opción inválida")

    except Exception as e:

        Logger.registrar_error(e)

        print("Error crítico controlado")