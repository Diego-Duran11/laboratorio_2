class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes.")
    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")
