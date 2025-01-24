'''Este archivo realiza las cuatro operaciones básicas y verifica 
si el resultado de cada una es par o impar.'''

def verificar_paridad(numero):
    """
    Verifica si un número es par o impar.

    Args:
        numero (int): El número a verificar.

    Returns:
        str: 'par' si el número es par, 'impar' si es impar.
    """
    return "par" if numero % 2 == 0 else "impar"


def realizar_suma(a, b):
    """
    Realiza la suma de dos números e imprime el resultado y su paridad.

    Args:
        a (int): Primer número.
        b (int): Segundo número.
    """
    resultado = a + b
    paridad = verificar_paridad(resultado)
    print(f"El resultado de la suma es: {resultado}, y es {paridad}.")


def realizar_resta(a, b):
    """
    Realiza la resta de dos números e imprime el resultado y su paridad.

    Args:
        a (int): Primer número.
        b (int): Segundo número.
    """
    resultado = a - b
    paridad = verificar_paridad(resultado)
    print(f"El resultado de la resta es: {resultado}, y es {paridad}.")


def realizar_multiplicacion(a, b):
    """
    Realiza la multiplicación de dos números e imprime el resultado y su paridad.

    Args:
        a (int): Primer número.
        b (int): Segundo número.
    """
    resultado = a * b
    paridad = verificar_paridad(resultado)
    print(f"El resultado de la multiplicación es: {resultado}, y es {paridad}.")


def realizar_division(a, b):
    """
    Realiza la división de dos números e imprime el resultado.

    Args:
        a (int): Numerador.
        b (int): Denominador.

    Notes:
        La paridad no se verifica para números decimales.
    """
    if b != 0:
        resultado = a / b
        print(
            f"El resultado de la división es: {resultado}, "
            "y la paridad no aplica."
        )
    else:
        print("La división no se puede realizar (división por cero).")


# Valores de entrada
VALOR_UNO = 10
VALOR_DOS = 3

# Llamadas a las funciones
realizar_suma(VALOR_UNO, VALOR_DOS)
realizar_resta(VALOR_UNO, VALOR_DOS)
realizar_multiplicacion(VALOR_UNO, VALOR_DOS)
realizar_division(VALOR_UNO, VALOR_DOS)
