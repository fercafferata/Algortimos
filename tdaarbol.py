from tdalista import *
import random
import json
from sys import getsizeof


class NodoArbol():
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.altura = 0
        self.info = info

# Arbol de decision


class NodoArbolD():
    def __init__(self, info, num=0):
        self.izq = None
        self.der = None
        self.num = num
        self.info = info


def insertarDecision(raiz, dato, num):
    if raiz is None:
        raiz = NodoArbolD(dato, num)
    else:
        if num < raiz.num:
            raiz.izq = insertarDecision(raiz.izq, dato, num)
        else:
            raiz.der = insertarDecision(raiz.der, dato, num)
    return raiz


def imprimirArbol(raiz, espacios=0):
    ''' Imprime arbol, girado hacia la izquierda'''
    if raiz is not None:
        espacios += 5
        imprimirArbol(raiz.der, espacios)
        print(" " * espacios, str(raiz.info))
        imprimirArbol(raiz.izq, espacios)


def altura(raiz):
    if raiz is None:
        return 0
    else:
        return raiz.altura


def act_altura(raiz):
    if altura(raiz.izq) > altura(raiz.der):
        raiz.altura = altura(raiz.izq) + 1
    else:
        raiz.altura = altura(raiz.der) + 1
    return raiz


def rot_simple(raiz, c):
    if c:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    act_altura(raiz)
    act_altura(aux)
    raiz = aux
    return raiz


def rot_doble(raiz, c):
    if c:
        raiz.izq = rot_simple(raiz.izq, False)
        raiz = rot_simple(raiz, True)
    else:
        raiz.der = rot_simple(raiz.der, True)
        raiz = rot_simple(raiz, False)
    return raiz


def balancear(raiz):
    if raiz is not None:
        if (altura(raiz.izq) - altura(raiz.der) == 2):
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rot_simple(raiz, True)
            else:
                raiz = rot_doble(raiz, True)
        elif (altura(raiz.der) - altura(raiz.izq) == 2):
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rot_simple(raiz, False)
            else:
                raiz = rot_doble(raiz, False)
    return raiz


def insertar(raiz, dato):
    if raiz is None:
        raiz = NodoArbol(dato)
        raiz.info = dato
    else:
        if dato < raiz.info:
            raiz.izq = insertar(raiz.izq, dato)
        else:
            raiz.der = insertar(raiz.der, dato)
    act_altura(raiz)
    raiz = balancear(raiz)
    return raiz


def busqueda(raiz, buscado):
    pos = None
    if raiz is not None:
        if raiz.info == buscado:
            pos = raiz
        else:
            if buscado < raiz.info:
                pos = busqueda(raiz.izq, buscado)
            else:
                pos = busqueda(raiz.der, buscado)
    return pos


def busquedaProximidad(raiz, buscado):
    aux = None
    if (raiz is not None):
        if (buscado in raiz.info):
            return raiz
        else:
            aux = busquedaProximidad(raiz.izq, buscado)
            if aux is None:
                aux = busquedaProximidad(raiz.der, buscado)
    return aux


def busquedaProxCampo(raiz, buscado, campo):
    aux = None
    if (raiz is not None):
        if (buscado in raiz.info[campo]):
            return raiz
        else:
            aux = busquedaProxCampo(raiz.izq, buscado, campo)
            if aux is None:
                aux = busquedaProxCampo(raiz.der, buscado, campo)
    return aux


def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def reemplazar(raiz):
    if raiz.der is not None:
        raiz.der == reemplazar(raiz.der)
    else:
        aux = raiz
        raiz = raiz.izq
    return(raiz, aux)


def eliminar(raiz, clave):
    x = None
    if (raiz is not None):
        if (raiz.info > clave):
            raiz.izq, x = eliminar(raiz.izq, clave)
        else:
            if(raiz.info < clave):
                raiz.der, x = eliminar(raiz.der, clave)
            else:
                if (raiz.izq is None):
                    x = raiz.info
                    raiz = raiz.der
                else:
                    if(raiz.der is None):
                        x = raiz.info
                        raiz = raiz.izq
                    else:
                        raiz.izq, aux = reemplazar(raiz.izq)
                        raiz.info = aux.info
    return(raiz, x)


def hoja(raiz):
    if raiz.der is None and raiz.izq is None:
        return True


def repetidos(raiz):
    if raiz is not None:
        if busqueda(raiz.izq, raiz.info) is not None:
            print('Repetido', raiz.info)
        if busqueda(raiz.der, raiz.info) is not None:
            print('Repetido', raiz.info)
        repetidos(raiz.izq)
        repetidos(raiz.der)


def numParImpar(raiz):
    if raiz is not None:
        if raiz.info % 2 == 0:
            return(1 + numParImpar(raiz.izq)[0] + numParImpar(raiz.der)[0], 0 + numParImpar(raiz.izq)[1] + numParImpar(raiz.der)[1])
        else:
            return(0 + numParImpar(raiz.izq)[0] + numParImpar(raiz.der)[0], 1 + numParImpar(raiz.izq)[1] + numParImpar(raiz.der)[1])
    else:
        return 0, 0


def operacion(operador, der, izq):
    resultado = 0
    if operador == '*':
        resultado = izq * der
    elif operador == '/':
        resultado = izq / der
    elif operador == '+':
        resultado = izq + der
    elif operador == '-':
        resultado = izq - der
    return resultado


def calcular(raiz):
    if hoja(raiz):
        return raiz.info
    else:
        return operacion(raiz.info, calcular(raiz.der), calcular(raiz.izq))


def hijo_derecho(raiz):
    return raiz.der


def hijo_izquierdo(raiz):
    return raiz.izq


def villanos(raiz):
    if raiz is not None:
        villanos(raiz.izq)
        if not raiz.info[1]:
            print(raiz.info)
        villanos(raiz.der)


def sh_con_c(raiz):
    if raiz is not None:
        sh_con_c(raiz.izq)
        if raiz.info[0][0] == 'C' and raiz.info[1]:
            print(raiz.info)
        sh_con_c(raiz.der)


def barridoInvertido(raiz):
    if raiz is not None:
        barridoInvertido(raiz.der)
        print(raiz.info)
        barridoInvertido(raiz.izq)


def separarHyV(raiz, bosque):
    if raiz is not None:
        separarHyV(raiz.izq, bosque)
        separarHyV(raiz.der, bosque)
        if raiz.info[1]:
            bosque[0] = insertar(bosque[0], raiz.info)
        else:
            bosque[1] = insertar(bosque[1], raiz.info)


def pesoArbol(raiz):
    if raiz is not None:
        return 1 + pesoArbol(raiz.izq) + pesoArbol(raiz.der)
    else:
        return 0


def minimo(raiz):
    aux = raiz
    while aux.izq is not None:
        aux = aux.izq
    return aux


def maximo(raiz):
    aux = raiz
    while aux.der is not None:
        aux = aux.der
    return aux


def nodosxnivel(raiz, nivel, nivel_ingresado=0):
    c = 0
    if raiz is not None:
        if nivel == nivel_ingresado:
            c += 1
        nivel_ingresado += 1
        c += nodosxnivel(raiz.izq, nivel, nivel_ingresado)
        c += nodosxnivel(raiz.der, nivel, nivel_ingresado)
        return c
    else:
        return 0


def nodostotalXnivel(nivel):
    return 2**nivel


def contarHojas(raiz):
    if raiz is not None:
        if raiz.izq is None and raiz.der is None:
            return 1
        else:
            return contarHojas(raiz.izq) + contarHojas(raiz.der)
    else:
        return 0


def infoHojas(raiz):
    if raiz is not None:
        infoHojas(raiz.izq)
        if hoja(raiz):
            print(raiz.info)
        infoHojas(raiz.der)


def padre(raiz, nodo):
    aux = None
    if raiz is not None:
        if raiz.info == nodo:
            aux = nodo
        elif (raiz.izq is not None and raiz.izq.info == nodo) or (raiz.der is not None and raiz.der.info == nodo):
            aux = raiz
        else:
            if nodo < raiz.info:
                aux = padre(raiz.izq, nodo)
            else:
                aux = padre(raiz.der, nodo)
    return aux


class NodoHuffman():

    def __init__(self, valor, dato, izq=None, der=None):
        self.izq = izq
        self.der = der
        self.info = dato
        self.valor = valor


def crearArbolHuffman(lista):
    nodos = []
    for item in lista:
        nodo = NodoHuffman(item[0], item[1])
        nodos.append(nodo)
    while len(nodos) > 1:
        nodo_nuevo1 = nodos.pop(0)
        nodo_nuevo2 = nodos.pop(0)
        nuevo = nodo_nuevo1.valor + nodo_nuevo2.valor
        nodo_nuevo3 = NodoHuffman(nuevo, None, nodo_nuevo1, nodo_nuevo2)
        nodos.append(nodo_nuevo3)
        nodos = sorted(nodos, key=lambda nodo: nodo.valor)
    
    return nodos[0]


def codificar(mensaje, diccionario):
    mensaje_comprimido = ''
    for caracter in mensaje:
        mensaje_comprimido += diccionario.get(caracter)
    return mensaje_comprimido


def decodificar(arbol, mensaje):
    mensajeDecodificado = ''
    raiz = arbol
    while len(mensaje) >= 1:
        while not hoja(raiz):
            if len(mensaje) > 0:
                caracter = mensaje[0]
                mensaje = mensaje[1:]
            if caracter == "0":
                raiz = raiz.izq
            else:
                raiz = raiz.der
        mensajeDecodificado += raiz.info
        raiz = arbol
    return mensajeDecodificado


def generarNiveles(niveles=0):
    arbol = None
    arbol = insertar(arbol, random.randint(0, 1000))
    while arbol.altura <= niveles:
        arbol = insertar(arbol, random.randint(0, 1000))
    return arbol


def cortarNiveles(raiz, bosque, nivel, actual=0):
    if raiz is not None:
        if actual <= nivel:
            if actual == nivel:
                bosque.append(raiz)
            cortarNiveles(raiz.izq, bosque, nivel, actual+1)
            cortarNiveles(raiz.der, bosque, nivel, actual+1)


def arbolcompleto(raiz):
    nodos = 0
    for i in range(altura(raiz)):
        nodos += 2**i
    if nodos == pesoArbol(raiz):
        return True
    else:
        return False

    
def morse_decod(arbol, codigo):
    aux = arbol
    msj_decod = ''
    for i in range(len(codigo)):
        if codigo[i] == ' ':
            msj_decod = msj_decod + aux.info
            aux = arbol
        if codigo[i] == '.':
            if aux.izq is None:
                msj_decod = msj_decod + aux.info
                aux = arbol
            else:
                aux = aux.izq
        if codigo[i] == '-':
            if aux.der is None:
                msj_decod = msj_decod + aux.info
                aux = arbol
            else:
                aux = aux.der
        if codigo[i] == '/':
            msj_decod = msj_decod + ' '
            aux = arbol
    return msj_decod


def HeroesyMisiones():
    r = None
    lista = ['Itergalactica', ['Guardianas de la galaxia', 'Capitana Marvel'], 'En equipo', 'Guardianas de la galaxia', 'Recuperacion', ['AntMan', 'Capitan America', 'Black Widow', 'SpiderMan'], 'Habilidoso', ['SpiderMan', 'AntMan'], 'Defensa', ['Capitan America', 'SpiderMan', 'IronMan'], 'Estrategia', ['IronMan', 'Doctor Strange'], 'Destruccion', ['Thor, Hulk'], 'Rescate']
    codigos = [6000, 5000, 4000, 3000, 2000, 1000, 14000, 13000, 10000, 9000, 12000, 11000, 8000, 7000, 16000]
    for i in range(0, len(lista)):
        r = insertarDecision(r, lista[i], codigos[i])
    return r


def superheroe_para_mision(mision):
    r = HeroesyMisiones()
    decision = False
    superHeroes = ''
    while decision is not True and r is not None:
        if r.info == mision:
            superHeroes = r.izq.info
            decision = True
        else:
            r = r.der
    if len(superHeroes) > 0:
        print('Los superheroes indicados para esta mision son: ')
        print(superHeroes)
    else:
        print('No se encontro o la mision o los superheroes')


def mensajeSatelite():
    estado_del_tiempo = random.choice(['Despejado', 'Nublado', 'Lluvia'])
    humedad = random.choice(['Baja', 'Alta'])
    cod1 = random.choice(['1', '2'])
    cod2 = random.choice(['3', '5'])
    cod3 = random.choice(['7', '8'])
    mensaje = estado_del_tiempo + '-' + humedad + '-' + cod1 + '-' + cod2 + '-' + cod3
    return mensaje


def codificar_mensajeSatelite(diccionario, mensaje):
    mensaje_codificado = ''
    caracteres = mensaje.split('-')
    for caracter in caracteres:
        mensaje_codificado += diccionario.get(caracter)
    return mensaje_codificado


# mensaje 1 codificado y mensaje2 decodificado
def diferencia_tamanio(mensaje1, mensaje2):
    tamanio1 = getsizeof(mensaje1)
    tamanio2 = getsizeof(mensaje2)
    
    return tamanio1 - tamanio2


def frecuencia(tabla):
    largo = 0
    for item in tabla:
        largo += item[0]
    for item in tabla:
        item[2] = item[0] / largo


def tiempo_meteorologico(arbol, temperatura, presion, humedad, visibilidad, viento):
    datos = {
        'Temperatura': temperatura,
        'Presion': presion,
        'Humedad': humedad,
        'Visibilidad': visibilidad,
        'Viento': viento
    }
    print('Temperatura: ', temperatura)
    print('Presion: ', presion)
    print('Humedad: ', humedad)
    print('Visibilidad: ', visibilidad)
    print('Viento: ', viento)
    pronostico = ''
    while pronostico == '' and arbol is not None:
        if datos[arbol.info[0]] <= arbol.info[1]:
            if arbol.izq.izq is not None:
                arbol = arbol.izq
            else:
                pronostico = arbol.izq.info
                print('Pronostico: ', pronostico)
        else:
            if arbol.der.der is not None:
                arbol = arbol.der
            else:
                pronostico = arbol.der.info
                print('Pronostico: ', pronostico)