# Sistema Integral de Gestión (UNAD - Tarea 4)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![OOP](https://img.shields.io/badge/Paradigma-POO-green.svg)

Este proyecto fue desarrollado bajo los parametros de la programación orientada a objetos usando el lenguaje de programación python para su codificación, se implemento una arquitectura modular en **Python** bajo el paradigma de Programación Orientada a Objetos (POO). basada en clases abstractas, herencia, encapsulación y manejo robusto de excepciones. La aplicación gestiona clientes, servicios y reservas mediante objetos y listas internas, manteniendo estabilidad mediante validaciones estrictas y registros de eventos y errores en archivos log.
 
El archivo principal por donde se ejecuta el codigó es main.py en el se agrupa toda la funcionalidad interna como y debe capturar y mostrar los principales servicios (reservas de salas, alquiler de equipos, asesorías especializadas)
 
El sistema permite:
* Registrar clientes
* Crear servicios
* Generar reservas
* Validar datos
* Controlar errores
* Registrar eventos en logs
* Mantener estabilidad

## Arquitectura y Componentes Técnicos

### 1. Validación de Datos (`validaciones.py`)
Para garantizar la integridad de la información y evitar datos corruptos, el sistema implementa **expresiones regulares** que validan:
* **Nombres, documentos, correos, precios y duración.**
* La función `validar_correo()` verifica específicamente que el formato sea el estándar técnico.
* El sistema evita la entrada de datos inconsistentes gracias a la validación previa de la mayoría de los campos.

### 2. Manejo de Excepciones Personalizadas
Para un control de errores más eficiente y específico, se implementó la clase:
* `class ClienteInvalidoError(Exception)`: Permite saber exactamente qué falló durante el proceso de validación del cliente, proporcionando un manejo de errores más granular y técnico.

### 3. Trazabilidad y Logs (`logger.py`)
Cada evento del sistema se documenta en un historial que se refleja en los archivos logs mediante dos funciones principales:
* **`registrar_evento()`**: Guarda acciones normales del flujo del programa.
* **`registrar_error()`**: Documenta errores y excepciones para mantener un historial de fallos.

---

## Flujo Real del Programa
El sistema sigue un proceso lógico estricto para asegurar la estabilidad:

1. **Selección:** El usuario selecciona "Registrar cliente" en `main.py`.
2. **Recepción:** `main.py` recibe los datos iniciales.
3. **Instanciación:** Se intenta crear el objeto `cliente()`.
4. **Validación:** `cliente.py` valida los datos suministrados.
5. **Persistencia:** Si todo es correcto, `sistema.registrar_cliente()` guarda el objeto en `SistemaGestion`.
6. **Registro Exitoso:** `logger.py` registra el evento: *"cliente registrado"*.
7. **Captura de Excepción:** En caso de error, el bloque `except Exception as e` captura la falla.
8. **Registro de Error:** `logger.py` guarda el error técnico ocurrido.

---

## Estructura de Clases y Métodos
* **`SistemaGestion`**: Representa la empresa completa y gestiona las listas maestras:
    * `self.clientes = []`, `self.servicios = []`, `self.reservas = []`.
* **`cliente.py`**: Contiene la clase `cliente` con atributos (documento, nombre, correo) y métodos (`get_nombre`, `set_nombre`, `mostrar_cliente`).
* **`servicio.py`**: Define la clase abstracta `Servicio(ABC)` de la cual heredan `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`.
* **Polimorfismo:** Cada clase redefine `mostrar_detalles()` y aplica una sobrecarga lógica en `calcular_costo(cantidad, impuesto, descuento)`.
* **`reserva.py`**: Simula el flujo real (Pendiente, Confirmada, Cancelada, Procesada) y ejecuta acciones según el comportamiento de la clase.

---
**Desarrollado bajo parámetros de arquitectura modular y POO - UNAD.**