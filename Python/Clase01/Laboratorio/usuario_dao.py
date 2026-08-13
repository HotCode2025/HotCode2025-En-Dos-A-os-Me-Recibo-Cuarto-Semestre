'''
Módulo 5: usuario_dao.py (Patrón Data Access Object)
OBJETIVO: usuario_dao.py: Aislar la capa de persistencia (SQL) ejecutando las operaciones CRUD (Select, Read, Update, Delete) sobre la base de datos.

¿Qué problema resuelve este módulo?
El patrón DAO (Data Access Object) aísla la lógica de acceso a la base de datos de la lógica de negocio.

Sin DAO, tendrías consultas SQL repartidas por toda la aplicación (menú, controladores, vistas). Si mañana cambia la estructura de la tabla o el motor de base de datos, tendrías que modificar código en decenas de archivos. Con DAO, todas las sentencias SQL y la interacción directa con CursorDelPool residen en un solo archivo.
'''

from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class UsuarioDao:
    # Sentencias SQL como constantes de clase (subrayadas en el UML)
    _SELECCIONAR = 'SELECT id_usuario, username, password FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        """Recupera todos los registros de la tabla usuario y los mapea a una lista de objetos Usuario."""
        with CursorDelPool() as cursor:
            log.debug(f'Sentencia a ejecutar: {cls._SELECCIONAR}')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                # registro = (id_usuario, username, password)
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        """Inserta un nuevo objeto Usuario en la base de datos."""
        with CursorDelPool() as cursor:
            log.debug(f'Sentencia a ejecutar: {cls._INSERTAR}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado correctamente: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        """Actualiza un usuario existente filtrado por su id_usuario."""
        with CursorDelPool() as cursor:
            log.debug(f'Sentencia a ejecutar: {cls._ACTUALIZAR}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado correctamente: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        """Elimina un usuario filtrado por su id_usuario."""
        with CursorDelPool() as cursor:
            log.debug(f'Sentencia a ejecutar: {cls._ELIMINAR}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado con id: {usuario.id_usuario}')
            return cursor.rowcount


# Prueba del módulo
if __name__ == '__main__':
    # 1. Probar inserción
    usuario_nuevo = Usuario(username='ramiro', password='secretpassword')
    # UsuarioDao.insertar(usuario_nuevo)

    # 2. Probar actualización
    usuario_actualizar = Usuario(1, 'ramiro_actualizado', 'newpass123')
    # UsuarioDao.actualizar(usuario_actualizar)

    # 3. Probar eliminación
    usuario_eliminar = Usuario(id_usuario=2)
    # UsuarioDao.eliminar(usuario_eliminar)

    # 4. Probar selección / listado
    usuarios = UsuarioDao.seleccionar()
    for u in usuarios:
        log.debug(u)