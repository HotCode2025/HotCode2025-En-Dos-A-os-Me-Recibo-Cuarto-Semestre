'''
Módulo 2: conexion.py (Pool de Conexiones)
OBJETIVO: conexion.py: Administrar la creación, reutilización y cierre eficiente de conexiones con PostgreSQL mediante un Pool de Conexiones.

¿Qué problema resuelve este módulo?

Abrir y cerrar una conexión con la base de datos PostgreSQL en cada consulta SQL es una operación costosa y lenta: requiere handshake TCP, autenticación de usuario y consumo de recursos en el servidor Postgres.

Un Pool de Conexiones preasigna y mantiene un conjunto de conexiones abiertas en memoria (MIN_CON). Cuando la aplicación necesita interactuar con la base de datos, toma una conexión prestada del pool, ejecuta la consulta y la devuelve inmediatamente (MAX_CON fija el límite máximo de conexiones simultáneas).
'''
from psycopg2 import pool
from logger_base import log


class Conexion:
    # Atributos de clase (privados por convención con '_')
    _DATABASE = 'laboratorio_usuario'       # Nombre de la base de datos en PostgreSQL
    _USERNAME = 'postgres'      # Usuario de PostgreSQL
    _PASSWORD = 'admin'         # Contraseña del usuario
    _DB_PORT = '5432'           # Puerto por defecto de PostgreSQL
    _HOST = '127.0.0.1'         # Host (localhost)
    _MIN_CON = 1                # Cantidad mínima de conexiones en el pool
    _MAX_CON = 5                # Cantidad máxima de conexiones en el pool
    _pool = None                # Atributo estático que almacenará el pool

    @classmethod
    def obtenerPool(cls):
        """Inicializa el pool de conexiones si no existe y lo retorna."""
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Pool de conexiones creado con éxito: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                raise e
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        """Solicita y retorna una conexión disponible del pool."""
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        """Devuelve una conexión prestada de vuelta al pool."""
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Conexión devuelta al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        """Cierra todas las conexiones del pool al finalizar la aplicación."""
        cls.obtenerPool().closeall()
        log.debug('Todas las conexiones del pool han sido cerradas.')

# Bloque de prueba local
if __name__ == '__main__':
    # 1. Obtener una conexión de prueba
    conn1 = Conexion.obtenerConexion()
    # 2. Devolver la conexión al pool
    Conexion.liberarConexion(conn1)
    # 3. Cerrar el pool completo
    Conexion.cerrarConexiones()