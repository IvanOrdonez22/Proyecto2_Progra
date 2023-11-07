from datetime import datetime
from collections import deque


menu = {
    'hamburguesa': 5.99,
    'papas fritas': 2.49,
    'refresco': 1.99,
    'hot dog': 3.99,
    'ensalada': 4.49,
    'nuggets de pollo': 4.99,
    'helado': 2.99,
}
inventario = {
    'hamburguesa': 100,
    'papas fritas': 200,
    'refresco': 150,
    'hot dog': 100,
    'ensalada': 50,
    'nuggets de pollo': 80,
    'helado': 60,
    
}

carrito = []
cola_pedidos = deque()

ESTADO_PENDIENTE = "pendiente"
ESTADO_PREPARACION = "en preparación"
ESTADO_LISTO = "listo para servir"

clientes = {}

def menu_principal():
    while True:
        print("Menú Principal:")
        print("1. Gestión de Pedidos")
        print("2. Preparar Pedidos")
        print("3. Facturación y Pagos")
        print("4. Administración de Clientes")
        print("5. Mostrar Inventario")
        print("6. Editar Inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            menu_gestion_pedidos()
        elif opcion == '2':
            menu_preparar_pedidos()
        elif opcion == '3':
            menu_facturacion_pagos()
        elif opcion == '4':
            menu_administracion_clientes()
        elif opcion == '5':
            mostrar_inventario()
        elif opcion == '6':
            editar_inventario()
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
#commit 1
# Submenú para la Gestión de Pedidos
def menu_gestion_pedidos():
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
            mostrar_menu()
        elif opcion == '2':
            producto = input("Ingrese el producto que desea buscar: ").strip().lower()
            buscar_producto_en_menu(producto)
        elif opcion == '3':
            producto = input("Ingrese el producto que desea agregar: ").strip().lower()
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            agregar_al_carrito(producto, cantidad)
        elif opcion == '4':
            ver_carrito()
        elif opcion == '5':
            if carrito:
                procesar_pedido()
            else:
                print("El carrito está vacío. Agregue productos antes de confirmar un pedido.")
        elif opcion == '6':
            mostrar_cola_pedidos()
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Submenú para Preparar Pedidos
def buscar_producto_en_menu(producto):
    if producto in menu:
        print(f"{producto} encontrado en el menú. Precio: ${menu[producto]:.2f}")
    else:
        print(f"{producto} no encontrado en el menú.")

def menu_preparar_pedidos():
    while True:
        print("\nMenú de Preparar Pedidos:")
        print("1. Marcar Pedido como Listo")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            numero_pedido = int(input("Ingrese el número de pedido a marcar como listo: "))
            marcar_listo_para_servir(numero_pedido)
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_facturacion_pagos():
    while True:
        print("\nMenú de Facturación y Pagos:")
        print("1. Generar Factura")
        print("2. Procesar Pago")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            numero_pedido = int(input("Ingrese el número de pedido para generar la factura: "))
            generar_factura(numero_pedido)
        elif opcion == '2':
            numero_pedido = int(input("Ingrese el número de pedido para procesar el pago: "))
            metodo_pago = input("Ingrese el método de pago (efectivo/tarjeta): ").strip().lower()
            procesar_pago(numero_pedido, metodo_pago)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_administracion_clientes():
     while True:
        print("\nMenú de Administración de Clientes:")
        print("1. Registrar Cliente")
        print("2. Mostrar Clientes")
        print("3. Buscar Cliente por Nombre")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            mostrar_clientes()
        elif opcion == '3':
            nombre_cliente = input("Ingrese el nombre del cliente que desea buscar: ").strip()
            buscar_cliente_por_nombre(nombre_cliente)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función para mostrar el inventario
def mostrar_inventario():
    print("Inventario Actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")

# Función para mostrar el menú
def mostrar_menu():
    print("Menú:")
    for producto, precio in menu.items():
        print(f"{producto}: ${precio:.2f}")

# Función para agregar un producto al carrito
def agregar_al_carrito(producto, cantidad):
    if producto in menu and producto in inventario and inventario[producto] >= cantidad:
        precio_unitario = menu[producto]
        carrito.append({'producto': producto, 'cantidad': cantidad, 'precio_unitario': precio_unitario})
        print(f"{cantidad} {producto} agregado al carrito.")
        inventario[producto] -= cantidad
    else:
        print("Producto no disponible en el menú o cantidad insuficiente en el inventario.")

# Función para ver el contenido del carrito
def ver_carrito():
    total = sum(item['cantidad'] * item['precio_unitario'] for item in carrito)
    print("Contenido del Carrito:")
    for item in carrito:
        print(f"{item['cantidad']} {item['producto']} - ${item['precio_unitario']:.2f} cada uno")
    print(f"Total: ${total:.2f}")

# Función para procesar un pedido
def procesar_pedido():
    numero_pedido = len(cola_pedidos) + 1
    total = sum(item['cantidad'] * item['precio_unitario'] for item in carrito)
    hora_pedido = datetime.now()
    cola_pedidos.append({'numero': numero_pedido, 'productos': list(reversed(carrito)), 'total': total, 'estado': ESTADO_PENDIENTE, 'hora_pedido': hora_pedido})
    carrito.clear()
    print(f"Pedido #{numero_pedido} ha sido procesado. Total: ${total:.2f}")

# Función para mostrar la cola de pedidos
def mostrar_cola_pedidos():
    if not cola_pedidos:
        print("La cola de pedidos está vacía.")
    else:
        print("Cola de Pedidos:")
        for pedido in cola_pedidos:
            print(f"Pedido #{pedido['numero']}")
            print("Productos:")
            for item in pedido['productos']:
                print(f"{item['cantidad']} {item['producto']} - Q{item['precio_unitario']:.2f} cada uno")
            print(f"Total: Q{pedido['total']:.2f}")
            print(f"Estado: {pedido['estado']}")
            print(f"Hora de pedido: {pedido['hora_pedido']}\n")

# Función para preparar un pedido
def preparar_pedido(numero_pedido):
    if 1 <= numero_pedido <= len(cola_pedidos):
        pedido = cola_pedidos.popleft()
        if pedido['estado'] == ESTADO_PENDIENTE:
            pedido['estado'] = ESTADO_PREPARACION
            print(f"Pedido {numero_pedido} en preparación.")
        else:
            print(f"Pedido {numero_pedido} no se puede preparar. Estado incorrecto.")
    else:
        print("Número de pedido no válido.")

# Función para marcar un pedido como "listo para servir"
def marcar_listo_para_servir(numero_pedido):
    if 1 <= numero_pedido <= len(cola_pedidos):
        pedido = cola_pedidos[numero_pedido - 1]
        if pedido['estado'] == ESTADO_PREPARACION:
            pedido['estado'] = ESTADO_LISTO
            print(f"Pedido {numero_pedido} marcado como listo para servir.")
        else:
            print(f"Pedido {numero_pedido} no se puede marcar como listo. Estado incorrecto.")
    else:
        print("Número de pedido no válido.")

# Función para generar una factura
def generar_factura(numero_pedido):
    if 1 <= numero_pedido <= len(cola_pedidos):
        pedido = cola_pedidos[numero_pedido - 1]
        if pedido['estado'] == ESTADO_LISTO:
            hora_pedido = pedido['hora_pedido'].strftime('%Y-%m-%d %H:%M:%S')
            total = pedido['total']
            print(f"Factura para Pedido {numero_pedido} (Hora de Pedido: {hora_pedido}):")
            for item in pedido['productos']:
                producto = item['producto']
                cantidad = item['cantidad']
                precio_unitario = item['precio_unitario']
                subtotal = cantidad * precio_unitario
                print(f"{producto}: {cantidad} x ${precio_unitario:.2f} = ${subtotal:.2f}")
            print(f"Total a pagar: ${total:.2f}")
        else:
            print(f"Pedido {numero_pedido} no se ha marcado como listo para servir.")
    else:
        print("Número de pedido no válido.")

# Función para procesar el pago
def procesar_pago(numero_pedido, metodo_pago):
    if 1 <= numero_pedido <= len(cola_pedidos):
        pedido = cola_pedidos[numero_pedido - 1]
        if pedido['estado'] == ESTADO_LISTO:
            total = pedido['total']
            if metodo_pago == "efectivo":
                print(f"Pedido {numero_pedido} pagado en efectivo. Total: Q{total:.2f}")
                cola_pedidos.pop(numero_pedido - 1)  # Elimina el pedido de la cola después del pago
            elif metodo_pago == "tarjeta":
                print(f"Pedido {numero_pedido} pagado con tarjeta de crédito. Total: Q{total:.2f}")
                cola_pedidos.pop(numero_pedido - 1)  # Elimina el pedido de la cola después del pago
            else:
                print("Método de pago no válido. Use 'efectivo' o 'tarjeta'.")
        else:
            print(f"Pedido {numero_pedido} no se ha marcado como listo para servir.")
    else:
        print("Número de pedido no válido.")

#funcion para mostrar inventario
def editar_inventario():
    while True:
        print("Editar Inventario:")
        print("1. Agregar producto al inventario")
        print("2. Quitar producto del inventario")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            producto = input("Ingrese el producto que desea agregar al inventario: ").strip().lower()
            cantidad = int(input(f"Ingrese la cantidad de {producto} que desea agregar al inventario: "))
            if producto in inventario:
                inventario[producto] += cantidad
                print(f"Se han agregado {cantidad} unidades de {producto} al inventario.")
            else:
                print(f"{producto} no se encuentra en el inventario.")
        elif opcion == '2':
            producto = input("Ingrese el producto que desea quitar del inventario: ").strip().lower()
            cantidad = int(input(f"Ingrese la cantidad de {producto} que desea quitar del inventario: "))
            if producto in inventario:
                if cantidad <= inventario[producto]:
                    inventario[producto] -= cantidad
                    print(f"Se han quitado {cantidad} unidades de {producto} del inventario.")
                else:
                    print(f"No hay suficiente cantidad de {producto} en el inventario.")
            else:
                print(f"{producto} no se encuentra en el inventario.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función para registrar un cliente
def registrar_cliente():
    nombre_cliente = input("Nombre del cliente: ").strip()
    correo_cliente = input("Correo del cliente: ").strip()
    clientes[correo_cliente] = nombre_cliente
    print(f"Cliente registrado: {nombre_cliente}, Correo: {correo_cliente}")

# Función para mostrar la lista de clientes
def mostrar_clientes():
    print("Lista de Clientes:")
    for correo, nombre in clientes.items():
        print(f"Nombre: {nombre}, Correo: {correo}")
#Funcion para buscar cliente
def buscar_cliente_por_nombre(nombre_cliente):
    clientes_encontrados = []
    for correo, nombre in clientes.items():
        if nombre.lower() == nombre_cliente.lower():
            clientes_encontrados.append((nombre, correo))

    if clientes_encontrados:
        print("Clientes encontrados:")
        for nombre, correo in clientes_encontrados:
            print(f"Nombre: {nombre}, Correo: {correo}")
    else:
        print(f"No se encontraron clientes con el nombre: {nombre_cliente}")

if __name__ == '__main__':
    menu_principal()

#ACTUALIZAR MENU MEDIANTE LA EDICION DEL INVENTARIO
#CREAR UN SISTEMA DE VALORACION
#IMPEDIR QUE SALGA DEL PROGRAMA SI NO HA PAGADO
#CREAR PERFIL DE CLIENTE Y DE EMPLEADO