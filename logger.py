# Aquí hacemos el registro de eventos, guardando el historial del sistema en un archivo
from datetime import datetime


# Clase Logger: encargada de registrar eventos y errores del sistema
class Logger:

    ARCHIVO_LOG = "logs.txt"

    @staticmethod
    def registrar_evento(mensaje):  # Guarda acciones normales del sistema

        try:

            with open(
                Logger.ARCHIVO_LOG,
                "a",
                encoding="utf-8"
            ) as archivo:

                archivo.write(
                    f"[EVENTO] {datetime.now()} -> {mensaje}\n"
                )

        except Exception as e:

            print(f"Error logger: {e}")


    @staticmethod
    def registrar_error(error):  # Guarda errores del sistema

        try:

            with open(
                Logger.ARCHIVO_LOG,
                "a",
                encoding="utf-8"
            ) as archivo:

                archivo.write(
                    f"[ERROR] {datetime.now()} -> {error}\n"
                )

        except Exception as e:

            print(f"Error logger: {e}")