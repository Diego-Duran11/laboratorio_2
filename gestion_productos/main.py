from producto import Producto
from inventario import mostrar_inventario

def menu():
    inventario = [
        Producto("Producto1", 100, 10),
        Producto("Producto2", 200, 5),
        Producto("Producto3", 150, 20),
    ]

    while True:
        print("\n=== Menú Gestión de Productos ===")
        print("1. Mostrar inventario")
        print("2. Aumentar stock")
        print("3. Disminuir stock")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad a aumentar: "))
                for producto in inventario:
                    if producto.nombre == nombre:
                        producto.aumentar_stock(cantidad)
                        print(f"Stock de {nombre} aumentado correctamente.")
                        break
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad a disminuir: "))
                for producto in inventario:
                    if producto.nombre == nombre:
                        producto.disminuir_stock(cantidad)
                        print(f"Stock de {nombre} disminuido correctamente.")
                        break
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()
