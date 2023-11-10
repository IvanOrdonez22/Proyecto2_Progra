from datetime import datetime
from collections import deque

class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}"

class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"Nombre: {self.nombre}, Rol: {self.rol}"
    
class Restaurante:
    def __init__(self):
        self.menu = {
            'hamburguesa': 35.99,
            'papas fritas': 10.49,
            'refresco': 6.99,
            'hot dog': 8.99,
            'ensalada': 25.49,
            'nuggets de pollo': 30.99,
            'helado': 4.99,
        }
        self.inventario = {
            'hamburguesa': 100,
            'papas fritas': 200,
            'refresco': 150,
            'hot dog': 100,
            'ensalada': 50,
            'nuggets de pollo': 80,
            'helado': 60,
        }
        self.carrito = []
        self.cola_pedidos = deque()
        self.clientes = {}
        self.ESTADO_PENDIENTE = "pendiente"
        self.ESTADO_PREPARACION = "en preparación"
        self.ESTADO_LISTO = "listo para servir"

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



    def mostrar_inventario(self):
        print("Inventario Actual:")
        for producto, cantidad in self.inventario.items():
            print(f"{producto}: {cantidad} unidades")

    def editar_inventario(self):
        while True:
            print("Editar Inventario:")
            print("1. Agregar producto al inventario")
            print("2. Quitar producto del inventario")
            print("3. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                producto = input("Ingrese el producto que desea agregar al inventario: ").strip().lower()
                cantidad = int(input(f"Ingrese la cantidad de {producto} que desea agregar al inventario: "))
                if producto in self.inventario:
                    self.inventario[producto] += cantidad
                    print(f"Se han agregado {cantidad} unidades de {producto} al inventario.")
                else:
                    print(f"{producto} no se encuentra en el inventario.")
            elif opcion == '2':
                producto = input("Ingrese el producto que desea quitar del inventario: ").strip().lower()
                cantidad = int(input(f"Ingrese la cantidad de {producto} que desea quitar del inventario: "))
                if producto in self.inventario:
                    if cantidad <= self.inventario[producto]:
                        self.inventario[producto] -= cantidad
                        print(f"Se han quitado {cantidad} unidades de {producto} del inventario.")
                    else:
                        print(f"No hay suficiente cantidad de {producto} en el inventario.")
                else:
                    print(f"{producto} no se encuentra en el inventario.")
            elif opcion == '3':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

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
    
