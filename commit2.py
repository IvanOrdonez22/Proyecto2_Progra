def menu_clientes(self):
        while True:
            print("\nMenú de Clientes:")
            print("1. Ver Menú")
            print("2. Realizar Pedido")
            print("3. Ver Estado de Pedidos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.mostrar_menu()
            elif opcion == '2':
                self.menu_gestion_pedidos()
            elif opcion == '3':
                self.mostrar_cola_pedidos()
            elif opcion == '4':
                calificacion = input("Por favor, califica nuestro servicio (1-5 estrellas): ").strip()
                try:
                    calificacion = int(calificacion)
                    if 1 <= calificacion <= 5:
                        dibujar_estrellas(calificacion)
                        print(f"¡Gracias por tu calificación de {calificacion} estrellas! ¡Esperamos verte de nuevo!")
                    else:
                        print("Calificación no válida. Debe ser un número entre 1 y 5.")
                except ValueError:
                    print("Calificación no válida. Debe ser un número entero.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")