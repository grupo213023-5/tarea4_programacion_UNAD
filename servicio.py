from abc import ABC, abstractmethod
from excepciones import *
from validaciones import *

class Servicio(ABC):

    def __init__(self, codigo, nombre, precio):

<<<<<<< HEAD
        if not validar_precio(precio):
            raise CalculoInconsistenteError(
                "Precio inválido"
            )
=======
        if not codigo or not nombre:
            raise ClienteInvalidoError("Código o nombre inválido")

        if not validar_precio(precio):
            raise CalculoInconsistenteError("Precio inválido")
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    @abstractmethod
    def mostrar_detalles(self):
        pass

    # =========================
<<<<<<< HEAD
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

=======
    # CÁLCULO DE COSTO
    # =========================

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):

        if cantidad <= 0:
            raise CalculoInconsistenteError("Cantidad inválida")

        if impuesto < 0 or descuento < 0:
            raise CalculoInconsistenteError("Valores inválidos en impuesto o descuento")

        subtotal = self.precio * cantidad
        total_impuesto = subtotal * impuesto
        total = subtotal + total_impuesto - descuento

        if total < 0:
            raise CalculoInconsistenteError("Total inconsistente")

        return total


# =========================
# SALA
# =========================

class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio, capacidad):

        super().__init__(codigo, nombre, precio)

        if capacidad <= 0:
            raise CalculoInconsistenteError("Capacidad inválida")

>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
        self.capacidad = capacidad

    def mostrar_detalles(self):

        print(f"""
        Servicio: {self.nombre}
        Tipo: Sala
        Capacidad: {self.capacidad}
<<<<<<< HEAD
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

=======
        Precio: {self.precio}
        """)


# =========================
# EQUIPO
# =========================

class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio, tipo_equipo):

        super().__init__(codigo, nombre, precio)

        if not tipo_equipo:
            raise ClienteInvalidoError("Tipo de equipo inválido")

>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
        self.tipo_equipo = tipo_equipo

    def mostrar_detalles(self):

        print(f"""
        Servicio: {self.nombre}
        Tipo Equipo: {self.tipo_equipo}
<<<<<<< HEAD
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

=======
        Precio: {self.precio}
        """)


# =========================
# ASESORÍA
# =========================

class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio, especialista):

        super().__init__(codigo, nombre, precio)

        if not especialista:
            raise ClienteInvalidoError("Especialista inválido")

>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
        self.especialista = especialista

    def mostrar_detalles(self):

        print(f"""
        Servicio: {self.nombre}
        Especialista: {self.especialista}
<<<<<<< HEAD
=======
        Precio: {self.precio}
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
        """)