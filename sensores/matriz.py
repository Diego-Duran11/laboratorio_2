import random

def generar_matriz(n, m):
    """
    Genera una matriz de dimensiones n x m con valores aleatorios entre 50 y 100.
    """
    return [[random.randint(50, 100) for _ in range(m)] for _ in range(n)]