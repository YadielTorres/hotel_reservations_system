"""
Módulo que define el modelo de Usuario para la aplicación.
Este modelo es utilizado por Flask-Login para manejar la autenticación y almacenar la información relevante del usuario.
Clases:
Usuario: Representa a un usuario del sistema.
Autor: Yadiel
Fecha: 12/14/2024
"""

from flask_login import UserMixin
class Usuario(UserMixin):
"""
Clase que representa a un usuario en el sistema.
Atributos:
id (int): Identificador único del usuario.
email (str): Correo electrónico del usuario.
password (str): Contraseña hasheada del usuario.
nombre (str): Nombre completo del usuario.
rol (str): Rol del usuario ('cliente' o 'admin').
"""

def __init__(self, id, email, password, nombre, rol):
self.id = id
self.email = email
self.password = password
self.nombre = nombre
self.rol = rol
