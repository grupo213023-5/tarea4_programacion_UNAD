from excepciones import *
from validaciones import validar_duracion

class Reserva:

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

    def confirmar(self):

        if self.estado == "cancelada":

            raise OperacionNoPermitidaError(
                "No se puede confirmar"
            )

        self.estado = "confirmada"

    def cancelar(self):

        if self.estado == "procesada":

            raise OperacionNoPermitidaError(
                "No se puede cancelar"
            )

        self.estado = "cancelada"

    def procesar(self):

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