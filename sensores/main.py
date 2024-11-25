from matriz import generar_matriz
from analisis import detectar_valores_criticos

def menu():
    """
    Función principal que muestra el menú y ejecuta las opciones seleccionadas por el usuario.
    """
    while True:
        print("\n=== Menú Red de Sensores ===")
        print("1. Generar y analizar matriz de sensores")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                n = int(input("Ingrese el número de filas: "))
                m = int(input("Ingrese el número de columnas: "))
                matriz = generar_matriz(n, m)
                print("\nMatriz generada:")
                for fila in matriz:
                    print(fila)
                detectar_valores_criticos(matriz)
            except ValueError:
                print("Entrada inválida, intente nuevamente.")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()