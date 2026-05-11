# Aquí hacemos el registro de eventos, guarda el historial del sistema
from datetime import datetime

# Clase Logger
class Logger:

    ARCHIVO_LOG = "logs.txt"

    @staticmethod
    def registrar_evento(mensaje):                                      # Guarda acciones normales

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
    def registrar_error(error):                                         # Guarda errores

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