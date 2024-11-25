def contar_accesos(registros):
   
    accesos = {}
    for registro in registros:
        usuario = registro[0].strip() 
        accesos[usuario] = accesos.get(usuario, 0) + 1
    return accesos


def mostrar_accesos(accesos):
  
    print("\nAccesos por usuario:")
    for usuario, cantidad in accesos.items():
        print(f"{usuario}: {cantidad} accesos")
