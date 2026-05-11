import re

<<<<<<< HEAD
=======
# =========================
# NOMBRE
# =========================

>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
def validar_nombre(nombre):

    if not isinstance(nombre, str):
        return False

<<<<<<< HEAD
    if len(nombre.strip()) < 3:
=======
    nombre = nombre.strip()

    if len(nombre) < 3:
        return False

    if not nombre.replace(" ", "").isalpha():
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
        return False

    return True


<<<<<<< HEAD
def validar_documento(documento):

=======
# =========================
# DOCUMENTO
# =========================

def validar_documento(documento):

    if not isinstance(documento, str):
        return False

    documento = documento.strip()

>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
    if not documento.isdigit():
        return False

    if len(documento) < 5:
        return False

    return True


<<<<<<< HEAD
def validar_correo(correo):

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(patron, correo)


=======
# =========================
# CORREO
# =========================

def validar_correo(correo):

    if not isinstance(correo, str):
        return False

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(patron, correo) is not None


# =========================
# PRECIO
# =========================

>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
def validar_precio(precio):

    if not isinstance(precio, (int, float)):
        return False

    return precio > 0


<<<<<<< HEAD
def validar_duracion(duracion):

    return isinstance(duracion, int) and duracion > 0
=======
# =========================
# DURACIÓN
# =========================

def validar_duracion(duracion):

    if not isinstance(duracion, int):
        return False

    return duracion > 0
>>>>>>> 2d39c90 (mejoras en sistema, validaciones y estructura)
