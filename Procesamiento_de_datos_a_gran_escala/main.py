from registros import leer_registros
from analisis import contar_accesos, mostrar_accesos
def menu():
    registros = []

    while True:
        print("\n=== Menú Procesamiento de Datos ===")
        print("1. Leer registros de usuarios")
        print("2. Contar accesos por usuario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registros = leer_registros()
        elif opcion == "2":
            if registros:
                accesos = contar_accesos(registros)
                mostrar_accesos(accesos)
            else:
                print("\nNo hay registros cargados. Por favor, lea los registros primero.")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()