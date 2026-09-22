def resta(a, b):
    """Resta dos números."""
    return a - b


def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b


def suma(a, b):
    """Suma dos números."""
    return a - b


def division(a, b):
    """Divide a por b. Lanza ValueError si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
