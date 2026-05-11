"""
El archivo central se comunica con el resto permitiendo añadir las funciones centrales necesarias
para el correcto funcionamiento del sistema, debe almacenar y manejar las listas internas para ver
resultados en el archivo main por donde se ejecuta
"""

from logger import Logger
from reserva import Reserva
from excepciones import *

# Clase principal: Representa la empresa completa
class SistemaGestion:                   

    # Listas internas: aquí se almacenan objetos en memoria
    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    # =========================
    # CLIENTES
    # =========================

    def registrar_cliente(self, cliente):               # Función para definir a los clientes

        try:

            self.clientes.append(cliente)               # Se almacena dentro de la lista

            Logger.registrar_evento(
                "Cliente registrado"
            )

        except Exception as e:

            Logger.registrar_error(e)

    # =========================
    # SERVICIOS
    # =========================

    def agregar_servicio(self, servicio):               # Guarda servicios

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

    """
    Conecta cliente, servicio y duración, así se crea una nueva reserva
    Centraliza la logica dentro una sola función que será aprovechada cuando se le llame
    """
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