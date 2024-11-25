def area_cuadrado(lado):
    """
    Calcula el área del cuadrado.
    Fórmula: a = lado * lado
    Tipo float
    """
    return lado * lado


def area_triangulo(base, altura):
    """
    Calcula el área del triángulo.
    Fórmula: a = (base * altura) / 2
    Tipo float
    """
    return (base * altura) / 2


def area_circulo(radio):
    """
    Calcula el área del círculo.
    Fórmula: a = pi * radio^2
    Tipo float
    """
    from math import pi
    return pi * radio ** 2


def area_rectangulo(base, altura):
    """
    Calcula el área del rectángulo.
    Fórmula: a = base * altura
    Tipo float
    """
    return base * altura


def area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área del rombo.
    Fórmula: a = (diagonal_mayor * diagonal_menor) / 2
    Tipo float
    """
    return (diagonal_mayor * diagonal_menor) / 2


def area_romboide(base, altura):
    """
    Calcula el área del romboide.
    Fórmula: a = base * altura
    Tipo float
    """
    return base * altura


def area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área del trapecio.
    Fórmula: a = ((base_mayor + base_menor) * altura) / 2
    Tipo float
    """
    return ((base_mayor + base_menor) * altura) / 2


def area_pentagono(perimetro, apotema):
    """
    Calcula el área del pentágono.
    Fórmula: a = (perímetro * apotema) / 2
    Tipo float
    """
    return (perimetro * apotema) / 2
