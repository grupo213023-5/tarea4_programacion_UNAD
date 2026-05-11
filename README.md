# tarea4_programacion_UNAD
Tarea 4 del curso de programación (Sistema integral de gestión de clientes, servicios y reservas)

El proyecto fue desarrollado bajo los parametros de la programación orientada a objetos usando el lenguaje de programación python para su codificación, se implemento una arquitectura modular basada en clases abstractas, herencia, encapsulación y manejo robusto de excepciones. La aplicación gestiona clientes, servicios y reservas mediante objetos y listas internas, manteniendo estabilidad mediante validaciones estrictas y registros de eventos y errores en archivos log.

El archivo principal por donde se ejecuta el codigó es main.py en el se agrupa toda la funcionalidad interna como y debe capturar y mostrar los principales servicios (reservas de salas, alquiler de equipos, asesorías especializadas)

El sistema permite:
* Registrar clientes
* Crear servicios
* Generar reservas
* Validar datos
* Controlar errores
* Registrar eventos en logs
* Mantener estabilidad

A través del archivo main usado como cabecera para el proyecto en general, muestra el menú, recibe
datos del usuario, llama las funciones del sistema y controla el flujo general, es la parte con la
que el usuario interactúa.

La clase principal es:

* class SistemaGestion: (representa la empresa completa)

Para almacenar objetos en memoria, las instancias de las clases,usamos listas internas, definidas como:

*self.clientes = []
*self.servicios = []
*self.reservas = []

Las funciones principales que estan delimitadas son:

* registrar_cliente() (guarda clientes)
* agregar_servicio () (guarda servicios)
* crear_reserva() (crea una reserva, conectando cliente, 
  servicios y duración)

Creamos un archivo cliente.py para los clientes que contenga la clase cliente:

* class cliente:

Cuenta con atributos:
    documento (str)
    nombre (str)
    correo (str)

Y los metodos:
    get_nombre()
    set_nombre()
    mostrar_cliente()

la clase abstracta creada en servicio.py:

* class Servicio(ABC)

Crea la clase principal de donde heredan las clases:

* ReservaSala
* AlquilerEquipo
* AsesoriaEspecializada

todas comparten (código, nombre y precio)

Cada clase redefine mostrar_detalles() de forma diferente
Lo que crea polimorfismo y para permitir distintos escenarios
de cálculo necesarios según el servicio registrado, usamos una sobrecarga lógica:

calcular_costo(
    cantidad,
    impuesto,
    descuento
)

La clase reserva creada en reserva.py simula el flujo real de una reserva:

* Pendiente
* Confirmada
* Cancelada
* Procesada

Adicional creamos una accion segun el tipo de comportamiento de la clase como (confirmar, cancelar y procesar reserva)

Para realizar la correcta validación de los datos y que la información ingresada concuerda con la funcionalidad del sistema creamos un archivo de validaciones.py y usamos expresiones regulares:

* validar_correo()

Valida nombres, documentos, correos, precios, duración

Si queremos hacer una personalización en las excepciones y manejar errores mas eficientemente para casos más concretos, como es validar al cliente:

* class ClienteInvalidoError(Exception):

Permite saber que fué lo que falló, cada evento y cada error se guarda en el archivo logger.py que crea un historial y se refleja en el logs

Guarda aaciones normales:
* registrar_evento()

Guarda errores:
* registrar_error()

Flujo real del programa:

1. Usuario selecciona (Registrar cliente)
2. main.py recibe los datos
3. Se crea cliente()
4. cliente.py válida datos.
5. Si todo está correcto: 
    sistema.registrar_cliente()
6. SistemaGestion guarda el objeto
7. logger.py registra: 
    cliente registrado
8. En caso de un error: 
    except Exception as e
9. logger.py guarda el error