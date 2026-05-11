# Prueba rápida del funcionamiento del archivo logger para comprobación
from logger import Logger

Logger.registrar_evento("Prueba correcta")

Logger.registrar_error("Prueba error")

print("Funcionando")