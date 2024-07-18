class UsuarioView:
    
    @staticmethod
    def mostrar_usuario_guardado(usuario):
        print(f" El usuario guardado:  {usuario.nombre}, {usuario.edad} anios");

    @staticmethod
    def mostrar_usuarios(usuarios):
        for usuario in usuarios:
             print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}")