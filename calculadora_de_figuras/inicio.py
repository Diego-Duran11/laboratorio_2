from interfaz1 import (menu,
                       opcion_seleccionada,
                       datos_triangulo,
                       datos_circulo,
                       datos_cuadrado,
                       datos_rectangulo,
                       datos_rombo,
                       datos_romboide,
                       datos_trapecio,
                       datos_pentagono,
                       mostrar_circulo,
                       mostrar_cuadrado,
                       mostrar_triangulo,
                       mostrar_rectangulo,
                       mostrar_rombo,
                       mostrar_romboide,
                       mostrar_trapecio,
                       mostrar_pentagono)

from figuras import (area_cuadrado,
                     area_circulo,
                     area_triangulo,
                     area_rectangulo,
                     area_rombo,
                     area_romboide,
                     area_trapecio,
                     area_pentagono)

def main():
    opcion = 0
    while opcion != 9:  
        op = menu()
        opcion = opcion_seleccionada(op)

        if opcion == 1:
            lado = datos_cuadrado()
            area = area_cuadrado(lado)
            mostrar_cuadrado(area)
        
        elif opcion == 2:
            base, altura = datos_triangulo()
            area = area_triangulo(base, altura)
            mostrar_triangulo(area)

        elif opcion == 3:
            radio = datos_circulo()
            area = area_circulo(radio)
            mostrar_circulo(area)

        elif opcion == 4:
            base, altura = datos_rectangulo()
            area = area_rectangulo(base, altura)
            mostrar_rectangulo(area)

        elif opcion == 5:
            diagonal_mayor, diagonal_menor = datos_rombo()
            area = area_rombo(diagonal_mayor, diagonal_menor)
            mostrar_rombo(area)

        elif opcion == 6:
            base, altura = datos_romboide()
            area = area_romboide(base, altura)
            mostrar_romboide(area)

        elif opcion == 7:
            base_mayor, base_menor, altura = datos_trapecio()
            area = area_trapecio(base_mayor, base_menor, altura)
            mostrar_trapecio(area)

        elif opcion == 8:
            perimetro, apotema = datos_pentagono()
            area = area_pentagono(perimetro, apotema)
            mostrar_pentagono(area)

        elif opcion == 9:
            print("Gracias por usar la calculadora de figuras")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()