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