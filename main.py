from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from sistema import SistemaGestion
from logger import Logger

sistema = SistemaGestion()

# =========================
# MENÚ
# =========================

def mostrar_menu():
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
# CLIENTE
# =========================

def registrar_cliente():
    try:
        documento = input("Documento: ").strip()
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()

        if not documento or not nombre or not correo:
            print("Todos los campos son obligatorios")
            return

        cliente = Cliente(documento, nombre, correo)
        sistema.registrar_cliente(cliente)

        print("Cliente registrado correctamente")

    except Exception as e:
        Logger.registrar_error(e)
        print(f"Error creando cliente: {e}")

# =========================
# SALA
# =========================

def crear_sala():
    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: "))
        capacidad = int(input("Capacidad: "))

        if precio <= 0 or capacidad <= 0:
            print("Precio y capacidad deben ser mayores a cero")
            return

        sala = ReservaSala(codigo, nombre, precio, capacidad)
        sistema.agregar_servicio(sala)

        print("Sala creada correctamente")

    except ValueError:
        print("Datos numéricos inválidos")

    except Exception as e:
        Logger.registrar_error(e)
        print(f"Error: {e}")

# =========================
# EQUIPO
# =========================

def crear_equipo():
    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        tipo = input("Tipo equipo: ").strip()
        precio = float(input("Precio: "))

        if not codigo or not nombre or not tipo:
            print("Todos los campos son obligatorios")
            return

        if precio <= 0:
            print("El precio debe ser mayor a cero")
            return

        equipo = AlquilerEquipo(codigo, nombre, precio, tipo)
        sistema.agregar_servicio(equipo)

        print("Equipo creado correctamente")

    except ValueError:
        print("Precio inválido")

    except Exception as e:
        Logger.registrar_error(e)
        print(f"Error: {e}")

# =========================
# ASESORÍA
# =========================

def crear_asesoria():
    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        especialista = input("Especialista: ").strip()
        precio = float(input("Precio: "))

        if not codigo or not nombre or not especialista:
            print("Todos los campos son obligatorios")
            return

        if precio <= 0:
            print("El precio debe ser mayor a cero")
            return

        asesoria = AsesoriaEspecializada(codigo, nombre, precio, especialista)
        sistema.agregar_servicio(asesoria)

        print("Asesoría creada correctamente")

    except Exception as e:
        Logger.registrar_error(e)
        print(f"Error: {e}")

# =========================
# RESERVA
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
            print(i, cliente.get_nombre())

        indice_cliente = int(input("Seleccione cliente: "))

        print("\nSERVICIOS")
        for i, servicio in enumerate(sistema.servicios):
            print(i, servicio.nombre)

        indice_servicio = int(input("Seleccione servicio: "))
        duracion = int(input("Duración: "))

        if duracion <= 0:
            print("Duración inválida")
            return

        reserva = sistema.crear_reserva(
            sistema.clientes[indice_cliente],
            sistema.servicios[indice_servicio],
            duracion
        )

        if reserva:
            reserva.confirmar()
            reserva.procesar()
            print("Reserva completada")

    except (ValueError, IndexError):
        print("Selección inválida")

    except Exception as e:
        Logger.registrar_error(e)
        print(f"Error: {e}")

# =========================
# SIMULACIÓN
# =========================

def simulacion():
    print("SIMULACIÓN AUTOMÁTICA")

    operaciones = 0

    datos_validos = [
        ("10001", "Carlos Ramirez", "carlos@gmail.com"),
        ("10002", "Laura Torres", "laura@gmail.com"),
        ("10003", "Andres Perez", "andres@gmail.com")
    ]

    for doc, nom, correo in datos_validos:
        try:
            cliente = Cliente(doc, nom, correo)
            sistema.registrar_cliente(cliente)
            operaciones += 1
        except Exception:
            pass

    try:
        sala = ReservaSala("S01", "Sala Premium", 200000, 20)
        sistema.agregar_servicio(sala)
        operaciones += 1
    except Exception:
        pass

    try:
        reserva = sistema.crear_reserva(
            sistema.clientes[0],
            sistema.servicios[0],
            3
        )

        if reserva:
            reserva.confirmar()
            reserva.procesar()
            operaciones += 1

    except Exception:
        pass

    print(f"Operaciones ejecutadas: {operaciones}")

# =========================
# LOOP PRINCIPAL
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