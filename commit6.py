    def menu_facturacion_pagos(self):
        while True:
            print("\nMenú de Facturación y Pagos:")
            print("1. Generar Factura")
            print("2. Procesar Pago")
            print("3. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                numero_pedido = int(input("Ingrese el número de pedido para generar la factura: "))
                self.generar_factura(numero_pedido)
            elif opcion == '2':
                numero_pedido = int(input("Ingrese el número de pedido para procesar el pago: "))
                metodo_pago = input("Ingrese el método de pago (efectivo/tarjeta): ").strip().lower()
                self.procesar_pago(numero_pedido, metodo_pago)
            elif opcion == '3':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def generar_factura(self, numero_pedido):
        if 1 <= numero_pedido <= len(self.cola_pedidos):
            pedido = self.cola_pedidos[numero_pedido - 1]
            if pedido['estado'] == self.ESTADO_LISTO:
                hora_pedido = pedido['hora_pedido'].strftime('%Y-%m-%d %H:%M:%S')
                total = pedido['total']
                print(f"Factura para Pedido {numero_pedido} (Hora de Pedido: {hora_pedido}):")
                for item in pedido['productos']:
                    producto = item['producto']
                    cantidad = item['cantidad']
                    precio_unitario = item['precio_unitario']
                    subtotal = cantidad * precio_unitario
                    print(f"{producto}: {cantidad} x Q{precio_unitario:.2f} = Q{subtotal:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
            else:
                print(f"Pedido {numero_pedido} no se ha marcado como listo para servir.")
        else:
            print("Número de pedido no válido.")

    def procesar_pago(self, numero_pedido, metodo_pago):
        if 1 <= numero_pedido <= len(self.cola_pedidos):
            pedido = self.cola_pedidos[numero_pedido - 1]
            if pedido['estado'] == self.ESTADO_LISTO:
                total = pedido['total']
                if metodo_pago == "efectivo":
                    monto_recibido = float(input(f"Ingrese el monto recibido en efectivo (Total: Q{total:.2f}): "))
                    if monto_recibido >= total:
                        cambio = monto_recibido - total
                        print(f"Pedido {numero_pedido} pagado en efectivo. Total: ${total:.2f}. Cambio: Q{cambio:.2f}")
                    else:
                        print("Monto insuficiente. El pago no se ha completado.")
                        return  
                elif metodo_pago == "tarjeta":
                    numero_tarjeta = input("Ingrese el número de tarjeta: ").strip()
                    self.generar_comprobante(numero_pedido, total, numero_tarjeta)
                    print(f"Pedido {numero_pedido} pagado con tarjeta de crédito. Total: Q{total:.2f}")
                else:
                    print("Método de pago no válido. Use 'efectivo' o 'tarjeta'.")
                    return  

                self.cola_pedidos.remove(pedido)  
            else:
                print(f"Pedido {numero_pedido} no se ha marcado como listo para servir.")
        else:
            print("Número de pedido no válido.")

    def generar_comprobante(self, numero_pedido, total, numero_tarjeta):
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        nombre_archivo = f"comprobante_pedido_{numero_pedido}.txt"

        
        numero_tarjeta_oculto = "****-****-****-" + numero_tarjeta[-4:]

        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Comprobante de Pago\n")
            archivo.write(f"Pedido #{numero_pedido}\n")
            archivo.write(f"Fecha y Hora: {hora_actual}\n")
            archivo.write(f"Total a Pagar: Q{total:.2f}\n")
            archivo.write(f"Método de Pago: Tarjeta de Crédito\n")
            archivo.write(f"Número de Tarjeta: {numero_tarjeta_oculto}\n")

        print(f"Comprobante generado exitosamente: {nombre_archivo}")


