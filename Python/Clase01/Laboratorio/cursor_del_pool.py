'''
Módulo 3: cursor_del_pool.py (Context Manager para el Cursor)
OBJETIVO: cursor_del_pool.py: Automatizar la apertura del cursor, el manejo transaccional (commit/rollback) y la devolución de conexiones al pool mediante Context Managers (with).

¿Qué problema resuelve este módulo?
Sin un Context Manager, cada vez que hacés una consulta a la base de datos tenés que escribir manualmente:

Pedir una conexión al pool.
Crear un objeto cursor.
Ejecutar la sentencia SQL.
Hacer commit() si salió bien o rollback() si ocurrió un error.
Cerrar el cursor.
Devolver la conexión al pool.

Si ocurre un error inesperado en el medio y te olvidás de liberar la conexión o de hacer rollback(), las conexiones se agotan y la base de datos se bloquea.

La clase CursorDelPool implementa los métodos mágicos __enter__ y __exit__. Esto nos permite usar la sintaxis with CursorDelPool() as cursor: para que la apertura, transacción (commit/rollback) y devolución de la conexión ocurran automáticamente, incluso si salta una excepción.
'''

from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        """Se ejecuta al iniciar el bloque 'with'."""
        log.debug('Inicio del bloque with (CursorDelPool)')
        # 1. Solicita una conexión al pool
        self._conexion = Conexion.obtenerConexion()
        # 2. Crea el cursor a partir de la conexión
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        """Se ejecuta automáticamente al salir del bloque 'with'."""
        log.debug('Ejecutando método __exit__')
        
        # Si ocurrió una excepción dentro del bloque 'with'
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción, se hace rollback: {valor_excepcion} {tipo_excepcion} {traza_error}')
        else:
            # Si todo salió bien, confirma los cambios en la BD
            self._conexion.commit()
            log.debug('Transacción confirmada (commit)')
            
        # Cierra el cursor
        self._cursor.close()
        # Devuelve la conexión de vuelta al pool
        Conexion.liberarConexion(self._conexion)

# Prueba del módulo
if __name__ == '__main__':
    # Probamos el context manager ejecutando una consulta simple
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT 1 + 1;')
        resultado = cursor.fetchone()
        log.debug(f'Resultado de la prueba: {resultado}')