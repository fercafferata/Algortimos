from tdalista import *
from random import choice, randint
from math import pow, sqrt


def crearTA(tamanio):
    tabla = []
    for i in range(0, tamanio):
        tabla.append(Lista())
    return tabla


def crearTC(tamanio):
    tabla = []
    for i in range(0, tamanio):
        tabla.append(None)
    return tabla


def barridoTA(tabla):
    for l in tabla:
        if l.tamanio != 0:
            barrido(l)


def barridoTC(tabla):
    for e in tabla:
        if e is not None:
            print(e)


def rehash(tabla, original):
    indice = original + 1
    if indice == len(tabla):
        indice = 0
    while tabla[indice] is not None and indice != original:
        indice += 1
        if indice == len(tabla):
            indice = 0
    
    if indice == original:
        indice = None
    
    return indice
