    def menu_gestion_pedidos(self):
        while True:
            print("\nMenú de Gestión de Pedidos:")
            print("1. Mostrar Menú")
            print("2. Buscar Producto en el Menú")
            print("3. Agregar al Carrito")
            print("4. Ver Carrito")
            print("5. Procesar Pedido")
            print("6. Ver Cola de Pedidos")
            print("7. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.mostrar_menu()
            elif opcion == '2':
                producto = input("Ingrese el producto que desea buscar: ").strip().lower()
                self.buscar_producto_en_menu(producto)
            elif opcion == '3':
                producto = input("Ingrese el producto que desea agregar: ").strip().lower()
                cantidad = int(input("Ingrese la cantidad que desea agregar: "))
                self.agregar_al_carrito(producto, cantidad)
            elif opcion == '4':
                self.ver_carrito()
            elif opcion == '5':
                if self.carrito:
                    self.procesar_pedido()
                else:
                    print("El carrito está vacío. Agregue productos antes de confirmar un pedido.")
            elif opcion == '6':
                self.mostrar_cola_pedidos()
            elif opcion == '7':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def buscar_producto_en_menu(self, producto):
        if producto in self.menu:
            print(f"{producto} encontrado en el menú. Precio: Q{self.menu[producto]:.2f}")
        else:
            print(f"{producto} no encontrado en el menú.")

    def mostrar_menu(self):
        print("Menú:")
        def bubble_sort(menu):
            items = list(menu.items())
            n = len(items)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if items[j][1] > items[j + 1][1]:
                        items[j], items[j + 1] = items[j + 1], items[j]
            return dict(items)
        menu_ordenado = bubble_sort(self.menu)
        for plato, precio in menu_ordenado.items():
            print(f"{plato}: ${precio}")

    def agregar_al_carrito(self, producto, cantidad):
        if producto in self.menu and producto in self.inventario and self.inventario[producto] >= cantidad:
            precio_unitario = self.menu[producto]
            self.carrito.append({'producto': producto, 'cantidad': cantidad, 'precio_unitario': precio_unitario})
            print(f"{cantidad} {producto} agregado al carrito.")
            self.inventario[producto] -= cantidad
        else:
            print("Producto no disponible en el menú o cantidad insuficiente en el inventario.")

    def ver_carrito(self):
        total = sum(item['cantidad'] * item['precio_unitario'] for item in self.carrito)
        print("Contenido del Carrito:")
        for item in self.carrito:
            print(f"{item['cantidad']} {item['producto']} - Q{item['precio_unitario']:.2f} cada uno")
        print(f"Total: Q{total:.2f}")

    def procesar_pedido(self):
        numero_pedido = len(self.cola_pedidos) + 1
        total = sum(item['cantidad'] * item['precio_unitario'] for item in self.carrito)
        hora_pedido = datetime.now()
        self.cola_pedidos.append({'numero': numero_pedido, 'productos': list(reversed(self.carrito)), 'total': total, 'estado': self.ESTADO_PENDIENTE, 'hora_pedido': hora_pedido})
        self.carrito.clear()
        print(f"Pedido #{numero_pedido} ha sido procesado. Total: Q{total:.2f}")

    def mostrar_cola_pedidos(self):
        if not self.cola_pedidos:
            print("La cola de pedidos está vacía.")
        else:
            print("Cola de Pedidos:")
            for pedido in self.cola_pedidos:
                print(f"Pedido #{pedido['numero']}")
                print("Productos:")
                for item in pedido['productos']:
                    print(f"{item['cantidad']} {item['producto']} - Q{item['precio_unitario']:.2f} cada uno")
                print(f"Total: Q{pedido['total']:.2f}")
                print(f"Estado: {pedido['estado']}")
                print(f"Hora de pedido: {pedido['hora_pedido']}\n")
