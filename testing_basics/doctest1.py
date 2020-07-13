#!/usr/bin/pytho3

def area(base, altura):
    """
    Calcula el área de un triángulo
    
    >>> area(3, 6)
    'El área del triángulo es: 9.0'

    >>> area(2, 4)
    'El área del triángulo es: 4.0'

    >>> area(3, 9)
    'El área del triángulo es: 13.5'

    """
    return "El área del triángulo es: " + str((base * altura) / 2)

import doctest
doctest.testmod()
