import random as rd

def elegir_usuarios_random(n, maximo, minimo):
    """Elige una cantidad n de numeros random en el rango maximo minimo. 
    Devuleve los numeros elegidos en una lista """
    numeros = []
    for x in range(n):
        