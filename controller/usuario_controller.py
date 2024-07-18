from model.usuario import Usuario
from view.usuario_view import UsuarioView

class UserController:
    
    def __init__(self):
        Usuario.crear_tabla();

    def agregar_usuario(self, nombre, edad):
        usuario = Usuario(nombre, edad);
        usuario.guardar();
        UsuarioView.mostrar_usuario_guardado(usuario);

    def listar_usuarios(self):
        usuarios = Usuario.mostrar_datos();
        UsuarioView.mostrar_usuarios(usuarios);


