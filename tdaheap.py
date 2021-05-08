class heap():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None]*tamanio


def intercambio(vector, indice1, indice2):
    vector[indice1], vector[indice2] = vector[indice2], vector[indice1]


def flotar(H, indice):
    padre = (indice - 1) // 2
    while (indice > 0) and (H.vector[indice][0] < H.vector[padre][0]):
        intercambio(H.vector, indice, padre)
        indice = padre
        padre = (indice - 1) // 2


def agregar(H, dato):
    H.vector[H.tamanio] = dato
    flotar(H, H.tamanio)
    H.tamanio += 1


def hundir(H, indice):
    hijo_izq = (indice * 2) + 1
    control = True
    while (control and hijo_izq < H.tamanio-1):
        menor = hijo_izq
        hijo_der = hijo_izq + 1
        if (hijo_izq <= H.tamanio-1) and (H.vector[hijo_der][0] < H.vector[hijo_izq][0]):
            mayor = hijo_der
        if (H.vector[indice][0] > H.vector[menor][0]):
            intercambio(H.vector, indice, menor)
            indice = menor
            hijo_izq = (2 * indice) + 1
        else:
            control = False


def quitar(H):
    aux = H.vector[0]
    intercambio(H.vector, 0, H.tamanio-1)
    H.tamanio -= 1
    hundir(H, 0)
    return aux


# cola de proridad
def arribo_H(H, prioridad, dato):
    agregar(H, [prioridad, dato])


def atencion_H(H):
    aux = quitar(H)
    return(aux)


def Heapsort(H):
    aux = H.tamanio
    for i in H.tamanio-2:
        quitar(H)
        H.tamanio = aux


def heap_vacio(heap):
    return heap.tamanio == 0


def cambiarPrioridad(H, indice, prioridad):
    prioridad_anterior = H.vector[indice][0]
    H.vector[indice][0] = prioridad
    if(prioridad < prioridad_anterior):
        flotar(H, indice)
    elif(prioridad > prioridad_anterior):
        hundir(H, indice)


def buscar_H(H, buscado):
    for i in range(len(H.vector)):
        if H.vector[i][1][0].info == buscado:
            return i
    return -1