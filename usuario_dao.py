
from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario


class UsuarioDao:

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario (username, password) VALUES (%s, %s)'
    _UPDATE = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuario')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Insertando usuario: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Actualizando usuario: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._UPDATE, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Eliminando usuario: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._DELETE, valores)
            return cursor.rowcount