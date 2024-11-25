def detectar_valores_criticos(matriz, umbral=80):
 
    print("\nValores críticos encontrados:")
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor > umbral:
                print(f"Sensor ({i}, {j}): {valor}°C")
