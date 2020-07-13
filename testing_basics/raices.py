#!/usr/bin/python3
import math

def raiz(lista):
    """
    Funcion que obtiene la raiz cuadrada de los numeros en lista

    >>>lista = []
    >>>for i in [4, 9, 19]:
    ...    lista.append(i)
    >>>raiz(lista)
    [2.0, 3.0, 4.0]
    
    """
    return [math.sqrt(n) for n in lista]

import doctest
doctest.testmod()
