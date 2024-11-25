def mostrar_inventario(inventario):
    print("\nInventario actual:")
    for producto in inventario:
        print(f"{producto.nombre} - Precio: ${producto.precio} - Stock: {producto.cantidad}")
