from controller.usuario_controller import UserController;

def main():
    controlador = UserController()
    
    # Agregar algunos usuarios
    controlador.agregar_usuario('Juan', 30)
    controlador.agregar_usuario('Ana', 25)

    # Listar usuarios
    controlador.listar_usuarios()


if __name__ == "__main__":
    main()

