"""
Aquí podemos defirnir errores propios del sistema, errores personalizados que nos permiten saber
Exactamente qué falló, en lugar de mostrarnos errores genéricos, nos muestra errores precisos y detallados
Del estado de los registros y consultas
Definimos una clase por cada excepcion y le indicamos que la clase existe pero hasta que no se ejecute una
Accion no tiene codigo interno adicional, esto crea excepciones personalizadas
Usamos pass para evitar clases vacias y que arroje error
"""

class ErrorSistema(Exception):
    """Clase base para todas las excepciones personalizadas del sistema."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Se lanza cuando los datos del cliente no son válidos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se lanza cuando un servicio no está disponible para reserva."""
    pass


class ReservaError(ErrorSistema):
    """Se lanza cuando ocurre un error al crear o procesar una reserva."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se lanza cuando una operación no está permitida en el sistema."""
    pass


class CalculoInconsistenteError(ErrorSistema):
    """Se lanza cuando hay inconsistencias en cálculos internos del sistema."""
    pass
