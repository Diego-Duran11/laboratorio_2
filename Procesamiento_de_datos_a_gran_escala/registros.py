def leer_registros():
    registros = []
    print("\nIngrese registros de actividad (nombre_usuario, hora_entrada, hora_salida).")
    print("Escriba 'fin' para terminar.")

    while True:
        entrada = input("Registro (nombre_usuario,hora_entrada,hora_salida): ")
        if entrada.lower() == "fin":
            break
        partes = entrada.split(",")
        if len(partes) == 3:
            registros.append(partes)
        else:
            print("Formato inválido. Asegúrese de ingresar los datos separados por comas y que sean 3 valores.")
    
    return registros