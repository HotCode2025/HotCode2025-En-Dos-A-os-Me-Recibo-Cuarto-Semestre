'''
Módulo 1: logger_base.py
OBJETIVO: logger_base.py: Centralizar el registro y auditar eventos y errores del sistema tanto en la terminal como en un archivo físico (capa_datos.log).

¿Qué problema resuelve este módulo?

En un entorno profesional no se utiliza print() para monitorear una aplicación backend. print() pierde la información al cerrar la consola, no registra la hora exacta, el archivo ni la línea donde ocurrió un evento, y no permite clasificar los mensajes según su gravedad.

El módulo logging de Python permite:

Guardar un historial persistente en un archivo físico (capa_datos.log).
Mostrar alertas simultáneamente en la consola.
Diferenciar niveles de severidad (DEBUG, INFO, WARNING, ERROR, CRITICAL).
'''

import logging as log

# Configuración básica del sistema de logging
log.basicConfig(
    level=log.DEBUG,  # Establece el nivel mínimo de mensajes a capturar
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Formato del mensaje
    datefmt='%I:%M:%S %p',  # Formato de hora (12h con AM/PM)
    handlers=[
        log.FileHandler('capa_datos.log'),  # Envía los eventos al archivo físico
        log.StreamHandler()                 # Envía los eventos a la consola
    ]
)

# Bloque de prueba local
if __name__ == '__main__':
    log.debug('Mensaje a nivel DEBUG: Detalle técnico para depurar')
    log.info('Mensaje a nivel INFO: Evento general de funcionamiento')
    log.warning('Mensaje a nivel WARNING: Advertencia que no detiene el programa')
    log.error('Mensaje a nivel ERROR: Fallo en una operación')
    log.critical('Mensaje a nivel CRITICAL: Fallo grave del sistema')