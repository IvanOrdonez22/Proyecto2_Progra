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