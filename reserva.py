# Representa el proceso de contratación, debe manejar el control de estados usando validaciones y
# Manejo de excepciones
from excepciones import *
from validaciones import validar_duracion

# Clase reserva
class Reserva:

    # Estados simula el flujo real de una reserva con 4 posibilidades (pendiente, confirmada, cancelada y procesada)
    ESTADOS = [
        "pendiente",
        "confirmada",
        "cancelada",
        "procesada"
    ]

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        if not validar_duracion(duracion):

            raise ReservaError(
                "Duración inválida"
            )

        if not servicio.disponible:

            raise ServicioNoDisponibleError(
                "Servicio no disponible"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    # =========================
    # CAMBIO DE ESTADOS
    # =========================

    def confirmar(self):                                    # Cambia el estado

        if self.estado == "cancelada":

            raise OperacionNoPermitidaError(
                "No se puede confirmar"
            )

        self.estado = "confirmada"

    def cancelar(self):                                     # Evita operaciones inválidas

        if self.estado == "procesada":

            raise OperacionNoPermitidaError(
                "No se puede cancelar"
            )

        self.estado = "cancelada"

    def procesar(self):                                     # Solo funciona si la reserva fue confirmada

        if self.estado != "confirmada":

            raise ReservaError(
                "La reserva debe confirmarse"
            )

        self.estado = "procesada"

    def mostrar_reserva(self):

        print(f"""
        ===== RESERVA =====
        Cliente: {self.cliente.get_nombre()}
        Servicio: {self.servicio.nombre}
        Duración: {self.duracion}
        Estado: {self.estado}
        """)