    def menu_preparar_pedidos(self):
        while True:
            print("\nMenú de Preparar Pedidos:")
            print("1. Marcar Pedido como Listo")
            print("2. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                numero_pedido = int(input("Ingrese el número de pedido a marcar como listo: "))
                self.marcar_listo_para_servir(numero_pedido)
            elif opcion == '2':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def marcar_listo_para_servir(self, numero_pedido):
        if 1 <= numero_pedido <= len(self.cola_pedidos):
            pedido = self.cola_pedidos[numero_pedido - 1]
            if pedido['estado'] == self.ESTADO_PENDIENTE:
                pedido['estado'] = self.ESTADO_LISTO
                print(f"Pedido {numero_pedido} marcado como listo para servir.")
            else:
                print(f"Pedido {numero_pedido} no se puede marcar como listo. Estado incorrecto.")
        else:
            print("Número de pedido no válido.")