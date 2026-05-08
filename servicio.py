from abc import ABC, abstractmethod
from excepciones import *
from validaciones import *

class Servicio(ABC):

    def __init__(self, codigo, nombre, precio):

        if not validar_precio(precio):
            raise CalculoInconsistenteError(
                "Precio inválido"
            )

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    @abstractmethod
    def mostrar_detalles(self):
        pass

    # =========================
    # SOBRECARGA DE MÉTODOS
    # =========================

    def calcular_costo(
        self,
        cantidad=1,
        impuesto=0,
        descuento=0
    ):

        if cantidad <= 0:
            raise CalculoInconsistenteError(
                "Cantidad inválida"
            )

        subtotal = self.precio * cantidad

        total_impuesto = subtotal * impuesto

        total = subtotal + total_impuesto - descuento

        if total < 0:
            raise CalculoInconsistenteError(
                "Total inconsistente"
            )

        return total
    
class ReservaSala(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio,
        capacidad
    ):

        super().__init__(codigo, nombre, precio)

        self.capacidad = capacidad

    def mostrar_detalles(self):

        print(f"""
        Servicio: {self.nombre}
        Tipo: Sala
        Capacidad: {self.capacidad}
        """)


class AlquilerEquipo(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio,
        tipo_equipo
    ):

        super().__init__(codigo, nombre, precio)

        self.tipo_equipo = tipo_equipo

    def mostrar_detalles(self):

        print(f"""
        Servicio: {self.nombre}
        Tipo Equipo: {self.tipo_equipo}
        """)


class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio,
        especialista
    ):

        super().__init__(codigo, nombre, precio)

        self.especialista = especialista

    def mostrar_detalles(self):

        print(f"""
        Servicio: {self.nombre}
        Especialista: {self.especialista}
        """)