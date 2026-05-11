"""
Aquí podemos defirnir errores propios del sistema, errores personalizados que nos permiten saber
Exactamente qué falló, en lugar de mostrarnos errores genéricos, nos muestra errores precisos y detallados
Del estado de los registros y consultas
Definimos una clase por cada excepcion y le indicamos que la clase existe pero hasta que no se ejecute una
Accion no tiene codigo interno adicional, esto crea excepciones personalizadas
Usamos pass para evitar clases vacias y que arroje error
"""

class ErrorSistema(Exception):
    pass


class ClienteInvalidoError(ErrorSistema):
    pass


class ServicioNoDisponibleError(ErrorSistema):
    pass


class ReservaError(ErrorSistema):
    pass


class OperacionNoPermitidaError(ErrorSistema):
    pass


class CalculoInconsistenteError(ErrorSistema):
    pass