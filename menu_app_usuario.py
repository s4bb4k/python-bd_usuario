from usuario import Usuario
from usuario_dao import  UsuarioDao
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios')
    print('2. Agregar usuarios')
    print('3. Modificar usuarios')
    print('4. Eliminar usuarios')
    print('5. Salir')
    opcion = int(input('Escribe una opcion: (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios Insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id de usuario: '))
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id de usuario: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')

else:
    log.info('Salimos de la aplicacion...')