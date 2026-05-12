# Representa el proceso de contratación, debe manejar el control de estados usando validaciones y
# manejo de excepciones personalizadas para garantizar el flujo correcto de la reserva.

from excepciones import *
from validaciones import validar_duracion


# Clase Reserva: modela el ciclo completo de vida de una reserva dentro del sistema
class Reserva:

    # Estados que simulan el flujo real de una reserva en el sistema
    # (pendiente, confirmada, cancelada y procesada)
    ESTADOS = [
        "pendiente",
        "confirmada",
        "cancelada",
        "procesada"
    ]

    def __init__(self, cliente, servicio, duracion):

        # Validación de duración de la reserva
        # Se asegura que la duración cumpla con las reglas del sistema
        if not validar_duracion(duracion):

            raise ReservaError(
                "Duración inválida"
            )

        # Validación de disponibilidad del servicio
        # Evita que se creen reservas sobre servicios no disponibles
        if not servicio.disponible:

            raise ServicioNoDisponibleError(
                "Servicio no disponible"
            )

        # Asignación de atributos principales de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        # Estado inicial de toda reserva al crearse
        self.estado = "pendiente"

    # =========================
    # CAMBIO DE ESTADOS
    # =========================

    def confirmar(self):  # Cambia el estado de la reserva a confirmada

        # No se permite confirmar una reserva cancelada
        if self.estado == "cancelada":

            raise OperacionNoPermitidaError(
                "No se puede confirmar una reserva cancelada"
            )

        # Cambio de estado a confirmada
        self.estado = "confirmada"

    def cancelar(self):  # Permite cancelar la reserva si es válido

        # No se puede cancelar una reserva ya procesada
        if self.estado == "procesada":

            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva ya procesada"
            )

        # Cambio de estado a cancelada
        self.estado = "cancelada"

    def procesar(self):  # Procesa la reserva solo si está confirmada

        # Validación de estado previo obligatorio
        if self.estado != "confirmada":

            raise ReservaError(
                "La reserva debe estar confirmada antes de procesarse"
            )

        # Cambio de estado a procesada
        self.estado = "procesada"

    def mostrar_reserva(self):

        # Muestra la información completa de la reserva
        print(f"""
        ===== RESERVA =====
        Cliente: {self.cliente.get_nombre()}
        Servicio: {self.servicio.nombre}
        Duración: {self.duracion}
        Estado: {self.estado}
        """)