'''
Módulo 6: menu_app_usuario.py (Interfaz Interactiva)
Objetivo del Módulo: Proveer una interfaz por consola para interactuar con el sistema de forma interactiva. 
Integrar todas las capas desarrolladas (logger_base, conexion, cursor_del_pool, usuario, usuario_dao) en un menú por consola que le permita al usuario listar, agregar, actualizar y eliminar registros de la base de datos de forma interactiva.
'''

"""
MÓDULO: menu_app_usuario.py
OBJETIVO: Presentar la interfaz por consola para interactuar con la entidad Usuario
utilizando todas las capas del sistema (DAO, Entidad, Pool de Conexiones y Logging).
"""

from usuario_dao import UsuarioDao
from usuario import Usuario
from logger_base import log

opcion = None

while opcion != 5:
    print('''
    --- Menú de Opciones del Sistema ---
    1. Listar usuarios
    2. Agregar usuario
    3. Actualizar usuario
    4. Eliminar usuario
    5. Salir
    ''')
    try:
        opcion = int(input('Escribe tu opción (1-5): '))
        
        if opcion == 1:
            usuarios = UsuarioDao.seleccionar()
            print('\n--- Listado de Usuarios ---')
            for u in usuarios:
                log.info(u)
                
        elif opcion == 2:
            username_var = input('Escribe el username: ')
            password_var = input('Escribe el password: ')
            usuario = Usuario(username=username_var, password=password_var)
            usuarios_insertados = UsuarioDao.insertar(usuario)
            log.info(f'Usuarios insertados: {usuarios_insertados}')
            
        elif opcion == 3:
            id_usuario_var = int(input('Escribe el id_usuario a actualizar: '))
            username_var = input('Escribe el nuevo username: ')
            password_var = input('Escribe el nuevo password: ')
            usuario = Usuario(id_usuario_var, username_var, password_var)
            usuarios_actualizados = UsuarioDao.actualizar(usuario)
            log.info(f'Usuarios actualizados: {usuarios_actualizados}')
            
        elif opcion == 4:
            id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
            usuario = Usuario(id_usuario=id_usuario_var)
            usuarios_eliminados = UsuarioDao.eliminar(usuario)
            log.info(f'Usuarios eliminados: {usuarios_eliminados}')
            
    except Exception as e:
        log.error(f'Ocurrió un error en el menú: {e}')
        
else:
    log.info('Salimos de la aplicación. ¡Hasta luego!')