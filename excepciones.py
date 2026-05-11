class ErrorSistema(Exception):
<<<<<<< HEAD
=======
    """Clase base para todas las excepciones del sistema."""
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    pass


class ClienteInvalidoError(ErrorSistema):
<<<<<<< HEAD
=======
    """Se lanza cuando los datos del cliente no son válidos."""
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    pass


class ServicioNoDisponibleError(ErrorSistema):
<<<<<<< HEAD
=======
    """Se lanza cuando un servicio no está disponible para reserva."""
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    pass


class ReservaError(ErrorSistema):
<<<<<<< HEAD
=======
    """Se lanza cuando ocurre un error en la creación de reservas."""
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    pass


class OperacionNoPermitidaError(ErrorSistema):
<<<<<<< HEAD
=======
    """Se lanza cuando una operación no está permitida en el sistema."""
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    pass


class CalculoInconsistenteError(ErrorSistema):
<<<<<<< HEAD
=======
    """Se lanza cuando hay inconsistencias en cálculos del sistema."""
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    pass