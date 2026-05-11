"""
Verifica que los datos sean válidos
Usa expresiones regulares, válida (nombres, documentos, correos, precios y duración)
En el proyecto evita datos corruptos gracias a la válidaciones de la mayoría de datos
"""

import re

# Validacion del nombre
def validar_nombre(nombre):

    if not isinstance(nombre, str):
        return False

    if len(nombre.strip()) < 3:
        return False

    return True

# Validacion de numero de documento
def validar_documento(documento):

    if not documento.isdigit():
        return False

    if len(documento) < 5:
        return False

    return True

# Validacion del correo
# Verifica si el correo tiene formato correcto
def validar_correo(correo):

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'                        # Es una expresión regular (Regex)
                                                                # Detecta el formato correcto para el correo

    return re.match(patron, correo)                             # Si el correo es válido devuelve un objeto válido

# Validacion del precio
def validar_precio(precio):

    if not isinstance(precio, (int, float)):
        return False

    return precio > 0


def validar_duracion(duracion):

    return isinstance(duracion, int) and duracion > 0