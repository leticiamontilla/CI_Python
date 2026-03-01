class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad


def mostrar_inventario(productos):
    print("--- Inventario Actual ---")
    for p in productos:
        # QODANA PODRÍA SUGERIR f-strings AQUÍ SI USAMOS FORMATOS ANTIGUOS.
        print(f"Producto: {p.nombre} | Stock: {p.cantidad} | Total: ${p.calcular_valor_total()}")


def buscar_producto(productos, nombre):
    # UN ERROR COMÚN: no manejar si el producto no existe.
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            return p
    return None


if __name__ == "__main__":
    # CREAMOS UNA LISTA DE EJEMPLO.
    tienda = [
        Producto("Monitor", 150.0, 10),
        Producto("Teclado", 25.5, 0),  # Stock agotado
        Producto("Ratón", 15.0, 45)
    ]

    mostrar_inventario(tienda)