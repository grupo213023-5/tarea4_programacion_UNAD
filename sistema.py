from logger import Logger
from reserva import Reserva
from excepciones import *

class SistemaGestion:

    def __init__(self):
<<<<<<< HEAD

=======
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
        self.clientes = []
        self.servicios = []
        self.reservas = []

    # =========================
    # CLIENTES
    # =========================

    def registrar_cliente(self, cliente):
<<<<<<< HEAD

        try:

            self.clientes.append(cliente)

            Logger.registrar_evento(
                "Cliente registrado"
            )

        except Exception as e:

            Logger.registrar_error(e)
=======
        try:
            if cliente is None:
                raise ValueError("Cliente inválido")

            self.clientes.append(cliente)

            Logger.registrar_evento("Cliente registrado")

        except Exception as e:
            Logger.registrar_error(e)
            print(f"Error registrando cliente: {e}")
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)

    # =========================
    # SERVICIOS
    # =========================

    def agregar_servicio(self, servicio):
<<<<<<< HEAD

        try:

            self.servicios.append(servicio)

            Logger.registrar_evento(
                "Servicio agregado"
            )

        except Exception as e:

            Logger.registrar_error(e)
=======
        try:
            if servicio is None:
                raise ValueError("Servicio inválido")

            self.servicios.append(servicio)

            Logger.registrar_evento("Servicio agregado")

        except Exception as e:
            Logger.registrar_error(e)
            print(f"Error agregando servicio: {e}")
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)

    # =========================
    # RESERVAS
    # =========================

<<<<<<< HEAD
    def crear_reserva(
        self,
        cliente,
        servicio,
        duracion
    ):

        try:

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            self.reservas.append(reserva)

            Logger.registrar_evento(
                "Reserva creada"
            )
=======
    def crear_reserva(self, cliente, servicio, duracion):

        try:
            if cliente is None or servicio is None:
                raise ValueError("Cliente o servicio inválido")

            if duracion <= 0:
                raise ValueError("Duración inválida")

            reserva = Reserva(cliente, servicio, duracion)

            self.reservas.append(reserva)

            Logger.registrar_evento("Reserva creada")
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)

            return reserva

        except ErrorSistema as e:
<<<<<<< HEAD

            Logger.registrar_error(e)

            print(f"Error controlado: {e}")

        except Exception as e:

            Logger.registrar_error(e)

            print("Error crítico controlado")

    def listar_reservas(self):
=======
            Logger.registrar_error(e)
            print(f"Error controlado: {e}")

        except ValueError as e:
            Logger.registrar_error(e)
            print(f"Error de validación: {e}")

        except Exception as e:
            Logger.registrar_error(e)
            print("Error crítico controlado")

        return None

    # =========================
    # LISTAR RESERVAS
    # =========================

    def listar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas")
            return
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)

        for reserva in self.reservas:
            reserva.mostrar_reserva()