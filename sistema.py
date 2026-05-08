from logger import Logger
from reserva import Reserva
from excepciones import *

class SistemaGestion:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    # =========================
    # CLIENTES
    # =========================

    def registrar_cliente(self, cliente):

        try:

            self.clientes.append(cliente)

            Logger.registrar_evento(
                "Cliente registrado"
            )

        except Exception as e:

            Logger.registrar_error(e)

    # =========================
    # SERVICIOS
    # =========================

    def agregar_servicio(self, servicio):

        try:

            self.servicios.append(servicio)

            Logger.registrar_evento(
                "Servicio agregado"
            )

        except Exception as e:

            Logger.registrar_error(e)

    # =========================
    # RESERVAS
    # =========================

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

            return reserva

        except ErrorSistema as e:

            Logger.registrar_error(e)

            print(f"Error controlado: {e}")

        except Exception as e:

            Logger.registrar_error(e)

            print("Error crítico controlado")

    def listar_reservas(self):

        for reserva in self.reservas:
            reserva.mostrar_reserva()