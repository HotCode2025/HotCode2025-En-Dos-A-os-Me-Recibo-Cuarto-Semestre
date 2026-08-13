'''
Módulo 4: usuario.py (Clase Entidad / Dominio)
OBJETIVO: usuario.py: Representar la entidad de dominio Usuario encapsulando sus atributos (id_usuario, username, password) con sus métodos Getters y Setters.

¿Qué problema resuelve este módulo?
Representa la tabla usuario de la base de datos como un objeto en Python (Modelo de Dominio / POO). En lugar de manipular tuplas sueltas o diccionarios, encapsulamos los datos en una clase con validaciones, getters, setters y representación en texto. Esto nos permite pasar instancias de Usuario entre las distintas capas de la aplicación con total tipado y seguridad.
'''

from logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    # --- GETTERS Y SETTERS ---

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    # --- MÉTODO DUNDER __str__ ---

    def __str__(self):
        return f'Usuario [ID: {self._id_usuario}, Username: {self._username}, Password: {self._password}]'


# Prueba del módulo
if __name__ == '__main__':
    # Crear usuario completo
    usr1 = Usuario(1, 'rmunoz', '123456')
    log.debug(usr1)

    # Crear usuario para inserción (sin ID aún)
    usr2 = Usuario(username='jperez', password='password123')
    log.debug(usr2)