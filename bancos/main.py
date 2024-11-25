from cuenta import CuentaBancaria
def menu():
    cuenta = CuentaBancaria("Usuario", 1000)
    while True:
        print("\n=== Menú Simulador de Banco ===")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar retiro")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cuenta.consultar_saldo()
        elif opcion == "2":
            try:
                monto = float(input("Monto a depositar: "))
                if monto > 0:
                    cuenta.depositar(monto)
                else:
                    print("El monto debe ser positivo.")
            except ValueError:
                print("Por favor, ingrese un monto válido.")
        elif opcion == "3":
            try:
                monto = float(input("Monto a retirar: "))
                if monto > 0:
                    cuenta.retirar(monto)
                else:
                    print("El monto debe ser positivo.")
            except ValueError:
                print("Por favor, ingrese un monto válido.")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
if __name__ == "__main__":
    menu()
