def menu():
 
    print("\nCalculadora de Áreas de Figuras Geométricas")
    print("1. Área de un Cuadrado")
    print("2. Área de un Triángulo")
    print("3. Área de un Círculo")
    print("4. Área de un Rectángulo")
    print("5. Área de un Rombo")
    print("6. Área de un Romboide")
    print("7. Área de un Trapecio")
    print("8. Área de un Pentágono")
    print("9. Salir")
    return int(input("Seleccione una opción: "))


def opcion_seleccionada(op):
    """
    Muestra el nombre de la figura seleccionada en el menú.
    Retorna el valor de la opción seleccionada.
    """
def opcion_seleccionada(op):
    """
    Muestra la figura seleccionada según la opción del menú.
    Retorna el valor de la opción seleccionada o un mensaje de error si no es válida.
    """
    CUADRADO = 1
    TRIANGULO = 2
    CIRCULO = 3
    RECTANGULO = 4
    ROMBO = 5
    ROMBOIDE = 6
    TRAPECIO = 7
    PENTAGONO = 8
    SALIR = 9

    if op == CUADRADO:
        print("Usted seleccionó la opción Cuadrado.")
        return CUADRADO
    elif op == TRIANGULO:
        print("Usted seleccionó la opción Triángulo.")
        return TRIANGULO
    elif op == CIRCULO:
        print("Usted seleccionó la opción Círculo.")
        return CIRCULO
    elif op == RECTANGULO:
        print("Usted seleccionó la opción Rectángulo.")
        return RECTANGULO
    elif op == ROMBO:
        print("Usted seleccionó la opción Rombo.")
        return ROMBO
    elif op == ROMBOIDE:
        print("Usted seleccionó la opción Romboide.")
        return ROMBOIDE
    elif op == TRAPECIO:
        print("Usted seleccionó la opción Trapecio.")
        return TRAPECIO
    elif op == PENTAGONO:
        print("Usted seleccionó la opción Pentágono.")
        return PENTAGONO
    elif op == SALIR:
        print("Saliendo de la calculadora...")
        return SALIR
    else:
        print("Opción no válida!")
        return "Opción no válida!"

def datos_cuadrado():
    lado = float(input("Digite el lado del cuadrado: "))
    return lado


def datos_triangulo():
    base = float(input("Digite la base del triángulo: "))
    altura = float(input("Digite la altura del triángulo: "))
    return base, altura


def datos_circulo():
    radio = float(input("Digite el radio del círculo: "))
    return radio


def datos_rectangulo():
    base = float(input("Digite la base del rectángulo: "))
    altura = float(input("Digite la altura del rectángulo: "))
    return base, altura


def datos_rombo():
    diagonal_mayor = float(input("Digite la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Digite la diagonal menor del rombo: "))
    return diagonal_mayor, diagonal_menor


def datos_romboide():
    base = float(input("Digite la base del romboide: "))
    altura = float(input("Digite la altura del romboide: "))
    return base, altura


def datos_trapecio():
    base_mayor = float(input("Digite la base mayor del trapecio: "))
    base_menor = float(input("Digite la base menor del trapecio: "))
    altura = float(input("Digite la altura del trapecio: "))
    return base_mayor, base_menor, altura


def datos_pentagono():
    perimetro = float(input("Digite el perímetro del pentágono: "))
    apotema = float(input("Digite el apotema del pentágono: "))
    return perimetro, apotema


def mostrar_cuadrado(area):
    print(f"El área del cuadrado es: {area}")


def mostrar_triangulo(area):
    print(f"El área del triángulo es: {area}")


def mostrar_circulo(area):
    print(f"El área del círculo es: {area}")


def mostrar_rectangulo(area):
    print(f"El área del rectángulo es: {area}")


def mostrar_rombo(area):
    print(f"El área del rombo es: {area}")


def mostrar_romboide(area):
    print(f"El área del romboide es: {area}")


def mostrar_trapecio(area):
    print(f"El área del trapecio es: {area}")


def mostrar_pentagono(area):
    print(f"El área del pentágono es: {area}")
