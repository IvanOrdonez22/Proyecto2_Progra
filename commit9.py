if __name__ == '__main__':
    restaurante = Restaurante()
    while True:
        tipo_usuario = input("¿Eres cliente o empleado? ").strip().lower()

        if tipo_usuario == 'cliente':
            restaurante.menu_clientes()
        elif tipo_usuario == 'empleado':
            restaurante.menu_empleados()
        else:
            print("Tipo de usuario no válido. ¡Hasta luego!")