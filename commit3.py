def menu_empleados(self):
        while True:
            print("\nMenú de Empleados:")
            print("1. Preparar Pedidos")
            print("2. Marcar Pedido como Listo")
            print("3. Generar Factura")
            print("4. Procesar Pago")
            print("5. Ver Inventario")
            print("6. Editar Inventario")
            print("7. Salir")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.menu_preparar_pedidos()
            elif opcion == '2':
                numero_pedido = int(input("Ingrese el número de pedido a marcar como listo: "))
                self.marcar_listo_para_servir(numero_pedido)
            elif opcion == '3':
                numero_pedido = int(input("Ingrese el número de pedido para generar la factura: "))
                self.generar_factura(numero_pedido)
            elif opcion == '4':
                numero_pedido = int(input("Ingrese el número de pedido para procesar el pago: "))
                metodo_pago = input("Ingrese el método de pago (efectivo/tarjeta): ").strip().lower()
                self.procesar_pago(numero_pedido, metodo_pago)
            elif opcion == '5':
                self.mostrar_inventario()
            elif opcion == '6':
                self.editar_inventario()
            elif opcion == '7':
                break
            else:
                print("Opción no válida. Intente de nuevo.")