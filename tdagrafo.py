from tdacola import *
from tdapila import *
from tdaheap import *
from math import inf
import random


class Grafo():
    def __init__(self, dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido


class Arista():
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class lista_arista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class Vertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()


def insertar_vertice(grafo, dato):
    vertice = Vertice(dato)
    if grafo.inicio is None or vertice.info < grafo.inicio.info:
        vertice.sig = grafo.inicio
        grafo.inicio = vertice
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        while (act is not None) and (act.info <= vertice.info):
            act = act.sig
            ant = ant.sig
        vertice.sig = act
        ant.sig = vertice
    grafo.tamanio += 1


def agregar_arista(lista_adyacentes, dato, destino):  # Las aristas se ordenan por peso en la lista
    arista = Arista(dato, destino)
    if lista_adyacentes.inicio is None or destino < lista_adyacentes.inicio.destino:
        arista.sig = lista_adyacentes.inicio
        lista_adyacentes.inicio = arista
    else:
        act = lista_adyacentes.inicio.sig
        ant = lista_adyacentes.inicio
        while act is not None and act.destino < arista.destino:
            ant = act
            act = act.sig
        arista.sig = act
        ant.sig = arista
    lista_adyacentes.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    orig = buscar_vertice(grafo, origen)
    dest = buscar_vertice(grafo, destino)
    if (orig is not None) and (dest is not None):
        if grafo.dirigido:
            agregar_arista(orig.adyacente, dato, dest.info)
        else:
            agregar_arista(orig.adyacente, dato, dest.info)
            agregar_arista(dest.adyacente, dato, orig.info)


def grafo_vacio(grafo):
    return grafo.inicio is None


def buscar_arista(vertice, buscado):
    aux = vertice.adyacente.inicio
    while aux is not None and aux.destino != buscado:
        aux = aux.sig
    return aux


def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig
    return aux


def adyacente(vertice):
    aux = vertice.adyacente.inicio
    while(aux is not None):
        print('Destino: {}-Info: {}'.format(aux.destino, aux.info))
        aux = aux.sig


def barrido_profundidad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacente = vertice.adyacente.inicio
            while adyacente is not None:
                aux_adyacente = buscar_vertice(grafo, adyacente.destino)
                if not aux_adyacente.visitado:
                    barrido_profundidad(grafo, aux_adyacente)
                adyacente = adyacente.sig
        vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                aux_adyacentes = nodo.adyacente.inicio
                while aux_adyacentes is not None:
                    adyacente = buscar_vertice(grafo, aux_adyacentes.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    aux_adyacentes = aux_adyacentes.sig
    vertice = vertice.sig


def existePaso(grafo, origen, destino):
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscarVertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existePaso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


def marcar_no_visitado(grafo):
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


def eliminar_vertice(grafo, clave):
    dato = None
    if grafo.inicio.info == clave:
        dato = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info != clave:
            ant = act
            act = act.sig
        if act is not None:
            dato = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if dato is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacente.inicio is not None:
                eliminar_arista(aux, dato)
            aux = aux.sig
    return dato


def eliminar_arista(vertice, destino):
    dato = None
    aux = vertice.adyacente.inicio
    if aux.destino == destino:
        dato = aux.info
        vertice.adyacente.inicio = aux.sig
        vertice.adyacente.tamanio -= 1
    else:
        ant = aux
        act = aux.sig
        while act is not None and act.destino != destino:
            ant = act
            act = act.sig
        if act is not None:
            dato = act.info
            ant.sig = act.sig
            vertice.adyacente.tamanio -= 1
    return dato


def quitar_arista(grafo, vertice, destino):
    nodo = eliminar_arista(vertice, destino)
    if not grafo.dirigido:
        nodo_origen = buscar_vertice(grafo, destino)
        eliminar_arista(nodo_origen, vertice.info)
    return nodo


def lista_de_vertices(grafo):
    lista = []
    aux = grafo.inicio
    while aux is not None:
        lista.append(aux.info)
        aux = aux.sig
    return lista


def kruskal(grafo):
    bosque = []
    heap_aristas = heap(grafo.tamanio**2)
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        bosque.append([aux_vertices.info])
        adyacentes = aux_vertices.adyacente.inicio
        while adyacentes is not None:
            datos = [aux_vertices.info, adyacentes.destino]
            peso = adyacentes.info
            arribo_H(heap_aristas, peso, datos)
            adyacentes = adyacentes.sig
        aux_vertices = aux_vertices.sig
    while (len(bosque) > 1) and (not heap_vacio(heap_aristas)):
        datos_y_peso = atencion_H(heap_aristas)
        peso = datos_y_peso[0]
        datos = datos_y_peso[1]
        origen = datos[0]
        destino = datos[1]
        array_origen = None
        array_destino = None
        for array_conexo in bosque:
            if origen in array_conexo:
                indice = bosque.index(array_conexo)
                array_origen = bosque.pop(indice)
                break
        for array_conexo in bosque:
            if destino in array_conexo:
                indice = bosque.index(array_conexo)
                array_destino = bosque.pop(indice)
                break
        if (array_origen is not None) and (array_destino is not None):
                if (len(array_origen) > len(array_destino)) or (len(array_origen) == len(array_destino)):
                    bosque.append(array_origen + array_destino)
                else:
                    bosque.append(array_destino + array_origen)
        else:
            bosque.append(array_origen)
    return bosque[0]


def resolverDijkstra(pila_camino, fin):
    camino = []
    while not pila_vacia(pila_camino):
        dato = desapilar(pila_camino)
        if dato[1][0].info == fin:
            camino.append(dato[1][0].info)
            fin = dato[1][1]
    return camino[::-1]  # Array invertido


def dijkstra(grafo, origen, destino):
    no_visitados = heap(grafo.tamanio)
    camino = Pila()
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        if aux_vertices.info == origen:
            arribo_H(no_visitados, 0, [aux_vertices, None])
        else:
            arribo_H(no_visitados, inf, [aux_vertices, None])
        aux_vertices = aux_vertices.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux_adyacentes = dato[1][0].adyacente.inicio
        while aux_adyacentes is not None:
            pos = buscar_H(no_visitados, aux_adyacentes.destino)
            distancia_acumulada = dato[0] + aux_adyacentes.info
            if (distancia_acumulada < no_visitados.vector[pos][0]):
                no_visitados.vector[pos][1][1] = dato[1][0].info  # Cambia el valor "de donde viene"
                cambiarPrioridad(no_visitados, pos, distancia_acumulada)  # Cambia el peso y flota o hunde
            aux_adyacentes = aux_adyacentes.sig
    return resolverDijkstra(camino, destino)


def sin_apuntar(vertice):
    return vertice.adyacente.tamanio == 0


def apuntado(grafo, vertice):
    es_apuntado = False
    aux = grafo.inicio
    while aux is not None and not es_apuntado:
        aux_adyacente = aux.adyacente.inicio
        while aux_adyacente is not None and not es_apuntado:
            if aux_adyacente.destino == vertice.info:
                es_apuntado = True
            aux_adyacente = aux_adyacente.sig
        aux = aux.sig
    return es_apuntado


def eliminar_desconectados(grafo):
    eliminar = []
    aux = grafo.inicio
    while aux is not None:
        if sin_apuntar(aux) and not apuntado(grafo, aux):
            eliminar_vertice(grafo, aux.info)
            eliminar.append(aux)
        aux = aux.sig
    return eliminar


def nodos_aristas_salida(grafo):
    nodos = []
    mayor = 0
    aux = grafo.inicio
    while aux is not None:
        if aux.adyacente.tamanio > mayor:
            mayor = aux.adyacente.tamanio
            nodos = [aux]
        elif aux.adyacente.tamanio == mayor:
            nodos.append(aux)
        aux = aux.sig
    return nodos


def mas_apuntado(grafo):
    aux = grafo.inicio
    vertices = []
    mayor = 0
    nodos = []
    while aux is not None:
        aux_vertice = aux.adyacente.inicio
        while aux_vertice is not None:
            vertices.append(aux)
            aux_vertice = aux_vertice.sig
        aux = aux.sig
    
    aux = grafo.inicio
    while aux is not None:
        entran = len(vertices)
        if entran > mayor:
            nodos = [aux]
        elif entran == mayor:
            nodos.append(aux)
        aux = aux.sig
    return nodos


def verticeNoApuntaOtros(grafo):
    aux = grafo.inicio
    while aux is not None:
        if sin_apuntar(aux):
            print(aux.info)
        aux = aux.sig


def se_apunta(grafo):
    cont = 0
    aux_grafo = grafo.inicio
    while aux_grafo is not None:
        aux = adyacente(aux_grafo)
        if aux != -1:
            cont += 1
        aux_grafo = aux_grafo.sig
    print(cont, ' vertices se apuntan a si mismos')
    return cont


def arista_mas_larga(grafo):
    aux = grafo.inicio
    mayor = 0
    nodos = []
    while aux is not None:
        aux_adyacente = aux.adyacente.inicio
        while aux_adyacente is not None:
            distancia = aux_adyacente.info
            if distancia > mayor:
                mayor = distancia
                origen = aux.info
                destino = aux_adyacente.destino
                nodos.append([origen, destino, distancia])
            aux_adyacente = aux_adyacente.sig
        aux = aux.sig
    return nodos


def cargar_dirigido_ej2():
    grafo = Grafo(True)
    vertices = ['A', 'B', 'C', 'D', 'E']
    for char in vertices:
        insertar_vertice(grafo, char)
    insertar_arista(grafo, random.randint(0, 10), 'A', 'E')
    insertar_arista(grafo, random.randint(0, 10), 'A', 'B')
    insertar_arista(grafo, random.randint(0, 10), 'A', 'C')
    insertar_arista(grafo, random.randint(0, 10), 'B', 'C')
    insertar_arista(grafo, random.randint(0, 10), 'C', 'B')
    insertar_arista(grafo, random.randint(0, 10), 'C', 'D')
    insertar_arista(grafo, random.randint(0, 10), 'D', 'D')
    return grafo


def cargar_ej2():
    grafo = Grafo(False)
    vertices = ['A', 'B', 'C', 'D', 'E']
    for char in vertices:
        insertar_vertice(grafo, char)
    insertar_arista(grafo, random.randint(0, 10), 'A', 'E')
    insertar_arista(grafo, random.randint(0, 10), 'A', 'B')
    insertar_arista(grafo, random.randint(0, 10), 'A', 'C')
    insertar_arista(grafo, random.randint(0, 10), 'B', 'C')
    insertar_arista(grafo, random.randint(0, 10), 'C', 'D')
    insertar_arista(grafo, random.randint(0, 10), 'D', 'D')
    return grafo


def lista_adyacencia(vertice):
    lista = []
    aux = vertice.adyacente.inicio
    while aux is not None:
        lista.append(aux.destino)
        aux = aux.sig
    return lista


def lista_de_Adyacencia(grafo):
    aux = grafo.inicio
    while aux is not None:
        lista = lista_adyacencia(aux)
        print('Vertice: ', aux.info, 'Aristas: ',','.join(lista))
        print()
        aux = aux.sig


class Antena():
    def __init__(self, id, longitud, latitud, velocidad):
        self.info = id
        self.ubicacion = [longitud, latitud]
        self.velocidad = velocidad
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()
    
    def __str__(self):
        return 'Id: ', str(self.info), '- Ubicacion: ', str(self.ubicacion), '- Velocidad: ', str(self.velocidad)


def generar_antena(codigo):
    id = codigo
    longitud = random.randint(-100, 100)
    latitud = random.randint(-100, 100)
    velocidad = random.randint(0, 100)
    return Antena(id, longitud, latitud, velocidad)



class Red():
    def __init__(self, tipo, info):
        self.info = info
        self.tipo = tipo
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()


def insertar_vertice2(grafo, dato):
    'inserta un objeto en lugar de un dato'
    vertice = dato
    if grafo.inicio is None or vertice.info < grafo.inicio.info:
        vertice.sig = grafo.inicio
        grafo.inicio = vertice
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        while act is not None and act.info <= vertice.info:
            act = act.sig
            ant = ant.sig
        vertice.sig = act
        ant.sig = vertice
    grafo.tamanio += 1


def dijkstra_peso(grafo, origen, destino):
    no_visitados = heap(grafo.tamanio)
    camino = Pila()
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        if aux_vertices.info == origen:
            arribo_H(no_visitados, 0, [aux_vertices, None])
        else:
            arribo_H(no_visitados, inf, [aux_vertices, None])
        aux_vertices = aux_vertices.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux_adyacentes = dato[1][0].adyacente.inicio
        while aux_adyacentes is not None:
            pos = buscar_H(no_visitados, aux_adyacentes.destino)
            distancia_acumulada = dato[0] + aux_adyacentes.info
            if (distancia_acumulada < no_visitados.vector[pos][0]):
                no_visitados.vector[pos][1][1] = dato[1][0].info  # Cambia el valor "de donde viene"
                cambiarPrioridad(no_visitados, pos, distancia_acumulada)  # Cambia el peso y flota o hunde
            aux_adyacentes = aux_adyacentes.sig
    peso = resolverDijkstra_peso(camino, destino)
    camino = resolverDijkstra(camino, destino)
    return peso


def resolverDijkstra_peso(pila, fin):
    pila_aux = copiar_pila(pila)
    peso = 0
    while not pila_vacia(pila_aux):
        dato = desapilar(pila_aux)
        if dato[1][0].info == fin:
            peso += dato[0]
            fin = dato[1][1]
    return peso


def matriz_adyacencia(grafo):
    matriz = []
    aux = grafo.inicio
    while aux is not None:
        fila = [0] * grafo.tamanio
        lista_adyacentes = aux.adyacente
        lista = lista_adyacentes.inicio
        while lista is not None:
            if lista.destino == 'A':
                fila[0] = 1
            elif lista.destino == 'B':
                fila[1] = 1
            elif lista.destino == 'C':
                fila[2] = 1
            elif lista.destino == 'D':
                fila[3] = 1
            elif lista.destino == 'E':
                fila[4] = 1
            elif lista.destino == 'F':
                fila[5] = 1
            elif lista.destino == 'G':
                fila[6] = 1
            lista = lista.sig
        matriz.append(fila)
        aux = aux.sig
    print('Matriz de adyacencia')
    for fila in matriz:
        for valor in fila:
            print(valor)
        print()


class Perfil():
    def __init__(self, nombre, apellido):
        self.info = nombre
        self.apllido = apellido
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()


def cargarEj7(grafo):
    personas = [
        Perfil('M', 'Casa'),
        Perfil('L', 'Auto'),
        Perfil('N', 'Puerta'),
        Perfil('X', 'Ventana'),
        Perfil('Y', 'Piso'),
        Perfil('Z', 'Mesa'),
        Perfil('K', 'Silla'),
        Perfil('A', 'Pared')
    ]
    for elemento in personas:
        insertar_vertice2(grafo, elemento)


def aristasEj7(grafo):
    red_social = ['T', 'F', 'I']
    for i in range(10):
        rs = random.choice(red_social)
        rt_mg = random.randint(0, 1000)
        lista = lista_de_vertices(grafo)
        origen = random.choice(lista)
        destino = random.choice(lista)
        insertar_arista(grafo, [rs, rt_mg], origen, destino)


def arista_mayor_pero(grafo, rs):
    mayor_peso = 0
    aux = grafo.inicio
    while aux is not None:
        aux_adyacentes = aux.adyacente.inicio
        while aux_adyacentes is not None:
            red = aux_adyacentes.info[0]
            peso = aux_adyacentes.info[1]
            if red == rs and peso > mayor_peso:
                mayor_peso = peso
            aux_adyacentes = aux_adyacentes.sig
        aux = aux.sig
    return mayor_peso


def kruskal2(grafo, rs):
    bosque = []
    heap_aristas = heap(grafo.tamanio**2)
    mayor_peso = arista_mayor_pero(grafo, rs)
    aux_vertices = grafo.inicio
    while aux_vertices is not None:
        bosque.append([aux_vertices.info])
        adyacentes = aux_vertices.adyacente.inicio
        while adyacentes is not None:
            if adyacentes.info[0] == rs:
                datos = [aux_vertices.info, adyacentes.destino]
                peso = mayor_peso - adyacentes.info[1]
                arribo_H(heap_aristas, peso, datos)
            adyacentes = adyacentes.sig
        aux_vertices = aux_vertices.sig
    while (len(bosque) > 1) and (not heap_vacio(heap_aristas)):
        datos_y_peso = atencion_H(heap_aristas)
        peso = datos_y_peso[0]
        datos = datos_y_peso[1]
        origen = datos[0]
        destino = datos[1]
        array_origen = None
        array_destino = None
        for array_conexo in bosque:
            if origen in array_conexo:
                indice = bosque.index(array_conexo)
                array_origen = bosque.pop(indice)
                break
        for array_conexo in bosque:
            if destino in array_conexo:
                indice = bosque.index(array_conexo)
                array_destino = bosque.pop(indice)
                break
        if (array_origen is not None) and (array_destino is not None):
            if (len(array_origen) > len(array_destino)) or (len(array_origen) == len(array_destino)):
                bosque.append(array_origen + array_destino)
            else:
                bosque.append(array_destino + array_origen)
        else:
            bosque.append(array_origen)
    return bosque[0]


def existePaso2(grafo, vertice, destino, rs):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                if nodo.info == destino:
                    return True
                aux = nodo.adyacente.inicio
                while aux is not None:
                    if aux.info[0] == rs:
                        resultado = buscar_vertice(grafo, aux.destino)
                        if not resultado.visitado:
                            resultado.visitado = True
                            arribo(cola, resultado)
                    aux = aux.sig
        vertice = vertice.sig
    return False


class Puntos():
    def __init__(self, nombre, longitud, latitud):
        self.info = nombre
        self.longitud = longitud
        self.latitud = latitud
        self.sig = None
        self.visitado = False
        self.adyacente = lista_arista()
    
    def __str__(self):
        return 'Punto: ', self.info, ': longitud: ', str(self.longitud), ': latitud: ', str(self.latitud)


def cargar_ej10(grafo):
    templos = ['Partenon', 'Olimpia', 'Delfos', 'Sunion', 'Efeso', 'Acropolis']
    for templo in templos:
        longitud = random.randint(-100, 100)
        latitud = random.randint(-100, 100)
        punto = Puntos(templo, longitud, latitud)
        insertar_vertice2(grafo, punto)
    for templo in templos:
        vertice = buscar_vertice(grafo, templo)
        for punto in templos:
            if (templo != punto) and (buscar_arista(vertice, punto) is None):
                peso = random.randint(0, 100)
                insertar_arista(grafo, peso, vertice.info, punto)
