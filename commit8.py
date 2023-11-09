    def menu_administracion_clientes(self):
        while True:
            print("\nMenú de Administración de Clientes:")
            print("1. Registrar Cliente")
            print("2. Mostrar Clientes")
            print("3. Buscar Cliente por Nombre")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.registrar_cliente()
            elif opcion == '2':
                self.mostrar_clientes()
            elif opcion == '3':
                nombre_cliente = input("Ingrese el nombre del cliente que desea buscar: ").strip()
                self.buscar_cliente_por_nombre(nombre_cliente)
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def registrar_cliente(self):
        nombre_cliente = input("Nombre del cliente: ").strip()
        correo_cliente = input("Correo del cliente: ").strip()
        cliente = Cliente(nombre_cliente, correo_cliente)
        self.clientes[correo_cliente] = cliente
        print(f"Cliente registrado: {cliente}")

    def mostrar_clientes(self):
        print("Lista de Clientes:")
        for cliente in self.clientes.values():
            print(cliente)

    def buscar_cliente_por_nombre(self, nombre_cliente):
        clientes_encontrados = []
        for cliente in self.clientes.values():
            if cliente.nombre.lower() == nombre_cliente.lower():
                clientes_encontrados.append(cliente)

        if clientes_encontrados:
            print("Clientes encontrados:")
            for cliente in clientes_encontrados:
                print(cliente)
        else:
            print(f"No se encontraron clientes con el nombre: {nombre_cliente}")
    
    def hay_pedido_pendiente(self):
        return any(pedido['estado'] == self.ESTADO_PENDIENTE for pedido in self.cola_pedidos)


def dibujar_estrellas(calificacion):
    print("Calificación:")
    for i in range(1, 6):
        if i <= calificacion:
            print("★", end=" ")  
        else:
            print("☆", end=" ") 
    print()  
