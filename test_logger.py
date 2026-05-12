# Prueba rápida del funcionamiento del Logger para verificar registro de eventos y errores

from logger import Logger


# Registro de un evento de prueba
Logger.registrar_evento("Prueba correcta de evento")

# Registro de un error de prueba
Logger.registrar_error("Prueba de error controlado")

print("Logger funcionando correctamente")