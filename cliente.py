# Aquí se define cómo es un cliente, para que se registre correctamente debemos usar los métodos
# GET y SET para definir los parametros y los atributos que deben llevar aplicando encapsulamiento
from validaciones import *
from excepciones import ClienteInvalidoError

# Clase cliente
class Cliente: 

    def __init__(self, documento, nombre, correo):

        self.set_documento(documento)
        self.set_nombre(nombre)
        self.set_correo(correo)

    # =========================
    # ENCAPSULAMIENTO
    # =========================

    # Aplicamos SET y GET como métodos principales para proteger la integridad de los datos
    def set_documento(self, documento):

        if not validar_documento(documento):
            raise ClienteInvalidoError(
                "Documento inválido"
            )

        self.__documento = documento

    def get_documento(self):
        return self.__documento

    # Valida antes de guardar
    def set_nombre(self, nombre):

        if not validar_nombre(nombre):
            raise ClienteInvalidoError(
                "Nombre inválido"
            )

        self.__nombre = nombre

    # Devuelve el valor de forma segura
    def get_nombre(self):
        return self.__nombre

    def set_correo(self, correo):

        if not validar_correo(correo):
            raise ClienteInvalidoError(
                "Correo inválido"
            )

        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def mostrar_cliente(self):

        print(f"""
        Cliente: {self.__nombre}
        Documento: {self.__documento}
        Correo: {self.__correo}
        """)