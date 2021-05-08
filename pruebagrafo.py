from tdagrafo import *
from tdapila import *
from random import *
from math import *


# Ej 1
'''grafo = Grafo()
vertices = []
while len(vertices) < 15:
    info = chr(randint(65, 90))
    if info not in vertices:
        vertices.append(info)

for dato in vertices:
    insertar_vertice(grafo, dato)

for i in range(0, 30):
    origen = chr(randint(65, 90))
    destino = chr(randint(65, 90))
    insertar_arista(grafo, randint(0, 50), origen, destino)
'''

# punto A
'''eliminados = eliminar_desconectados(grafo)
print('Vertices eliminados')
for nodo in eliminados:
    print(nodo.info)
'''
# punto B
'''nodos = nodos_aristas_salida(grafo)
print('Nodos con mayor cantidad de aristas de salida')
for nodo in nodos:
    print(nodo.info)
'''
# punto C
'''apuntado = mas_apuntado(grafo)
for nodo in apuntado:
    print('El vertice mas a puntado es: ', nodo.info)
'''
# Punto D
'''print('Vertices de los cuales no se puede acceder a otro')
verticeNoApuntaOtros(grafo)
'''
# Punto E
'''print('El grafo tiene ', grafo.tamanio, ' vertices')
'''
# Punto F
'''
se_apunta(grafo)
'''
# Punto G

'''mas_larga = arista_mas_larga(grafo)
for nodo in mas_larga:
    print('La arista mas larga es:')
    print('Origen: ', nodo[0], ' - Destino: ', nodo[1], ' - Distancia: ', nodo[2])
'''


# Ej 2
grafo = cargar_dirigido_ej2()
lista_de_Adyacencia(grafo)
# punto C
'''grafo = cargar_ej2()
arbol_min = kruskal(grafo)
print('Arbol de expansion minima')
print(arbol_min)'''
# Punto D
'''insertar_arista(grafo, randint(0, 10), 'E', 'C')'''
# Punto E
'''inicio = "A"
fin = "D"
camino_mas_corto = dijkstra(grafo, inicio, fin)
print('El camino mas corto entre A y D es: ', camino_mas_corto)
'''

# Ej 3
'''codigo = ['A', 'B', 'L', 'M', 'O', 'T', 'X', 'Y', 'G', 'H']
antenas = Grafo(False)
for char in codigo:
    insertar_vertice2(grafo, generar_antena(codigo))
    
cont = 0
while cont < 10:
    inicio = choice(codigo)
    destino = choice(codigo)
    if inicio != destino:
        insertar_arista(grafo, randint(0, 100), inicio, destino)
    cont += 1
'''
# punto C
'''tamanio = grafo.tamanio
print('Tamanio del grafo: ', tamanio)
'''
# Punto D
'''inicio = "Y"
fin = "X"
camino_mas_corto = dijkstra(grafo, inicio, fin)
if len(camino_mas_corto) > 1:
    print('El camino mas corto entre las antenas es: ', camino_mas_corto)
else:
    print('No hay conexion entre las antenas')
'''
# Punto E
'''arbol_min = kruskal(grafo)
print('Arbol de expansion minima')
print(arbol_min)
'''
# Punto F
'''buscado = buscar_vertice(grafo, 'X')
if buscado:
    print('La antena fue encontrada', buscado)
else:
    print('La antena no fue encontrada')
'''

# Ej 4
'''grafo = Grafo(False)
tipo = ['laptop', 'pc', 'router', 'servidor', 'impresora', 'switch']
# insertaar vertices
insertar_vertice2(grafo, Red('laptop-pt', 'Red Hat'))
insertar_vertice2(grafo, Red('laptop-pt', 'Debian'))
insertar_vertice2(grafo, Red('laptop-pt', 'Arch'))
insertar_vertice2(grafo, Red('pc-pt', 'Ubuntu'))
insertar_vertice2(grafo, Red('pc-pt', 'Manjaro'))
insertar_vertice2(grafo, Red('pc-pt', 'Mint'))
insertar_vertice2(grafo, Red('pc-pt', 'Parrot'))
insertar_vertice2(grafo, Red('pc-pt', 'Fedora'))
insertar_vertice2(grafo, Red('829', 'router02'))
insertar_vertice2(grafo, Red('829', 'router03'))
insertar_vertice2(grafo, Red('829', 'router01'))
insertar_vertice2(grafo, Red('server-pt', 'Guarani'))
insertar_vertice2(grafo, Red('server-pt', 'MongoDB'))
insertar_vertice2(grafo, Red('printer-pt', 'printer'))
insertar_vertice2(grafo, Red('2960-24tt', 'switch02'))
insertar_vertice2(grafo, Red('2960-24tt', 'switch01'))
# insertar aristas
insertar_arista(grafo, 25, 'router02', 'Red Hat')
insertar_arista(grafo, 9, 'router02', 'Guarani')
insertar_arista(grafo, 37, 'router02', 'router01')
insertar_arista(grafo, 50, 'router02', 'router03')
insertar_arista(grafo, 29, 'router01', 'switch01')
insertar_arista(grafo, 43, 'router01', 'router03')
insertar_arista(grafo, 17, 'switch01', 'Debian')
insertar_arista(grafo, 18, 'switch01', 'Ubuntu')
# modificado para hacer el punto G insertar_arista(grafo, 22, 'switch01', 'printer')
insertar_arista(grafo, 80, 'switch01', 'Mint')
insertar_arista(grafo, 61, 'router03', 'switch02')
insertar_arista(grafo, 40, 'switch02', 'Manjaro')
insertar_arista(grafo, 12, 'switch02', 'MongoDB')
insertar_arista(grafo, 5, 'switch02', 'Parrot')
insertar_arista(grafo, 56, 'switch02', 'Fedora')
insertar_arista(grafo, 3, 'switch02', 'Arch')
insertar_arista(grafo, 22, 'router02', 'printer')
'''
# punto B
'''print('Barrido en profundidad desde Red Hat')
buscado = buscar_vertice(grafo, 'Red Hat')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde Red Hat')
buscado = buscar_vertice(grafo, 'Red Hat')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)
'''
'''print('Barrido en profundidad desde Debian')
buscado = buscar_vertice(grafo, 'Debian')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde Debian')
buscado = buscar_vertice(grafo, 'Debian')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)
'''
'''print('Barrido en profundidad desde Arch')
buscado = buscar_vertice(grafo, 'Arch')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde Arch')
buscado = buscar_vertice(grafo, 'Arch')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''

# Punto C
'''print(dijkstra(grafo, 'Manjaro', 'printer'))
print(dijkstra(grafo, 'Red Hat', 'printer'))
print(dijkstra(grafo, 'Fedora', 'printer'))'''

# Punto D
'''arbol_min = kruskal(grafo)
print('Arbol de expansion minima')
print(arbol_min)'''

# punto E
'''servidor = 'Guarani'
buscado = buscar_vertice(grafo, servidor)
if not buscado:
    print('El servidor no ha sido encontrado')
else:
    largo_camino = inf
    camino_corto = []
    aux = grafo.inicio
    while aux is not None:
        if ('pc' in aux.tipo):
            largo = dijkstra_peso(grafo, aux.info, servidor)
            camino = dijkstra(grafo, aux.info, servidor)
            if largo_camino > largo:
                largo_camino = largo
                camino_corto = camino
        aux = aux.sig
    if largo_camino > 0:
        print('La pc que tiene el camino mas corto hasta el servidor Guarani es', camino_corto)
    else:
        print('No hay camino')
'''
# Punto f
'''servidor = 'Guarani'
switch = 'switch01'
buscado = buscar_vertice(grafo, servidor)
buscado1 = buscar_vertice(grafo, switch)
if not buscado or not buscado1:
    print('El servidor o el switch no ha sido encontrado')
else:
    largo_camino = inf
    camino_corto = []
    aux = buscado1.adyacente.inicio
    while aux is not None:
        switch_ady = buscar_vertice(grafo, aux.destino)
        if 'pc-pt' in switch_ady.tipo or 'laptop-pt' in switch_ady.tipo:
            largo = dijkstra_peso(grafo, aux.info, servidor)
            camino = dijkstra(grafo, aux.info, servidor)
            if largo_camino > largo:
                largo_camino = largo
                camino_corto = camino
        aux = aux.sig
    if largo_camino > 0:
        print('La pc que tiene el camino mas corto hasta el servidor Guarani es', camino_corto)
    else:
        print('No hay camino')'''


# punto G
'''print('Barrido en profundidad desde Red Hat')
buscado = buscar_vertice(grafo, 'Red Hat')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde Red Hat')
buscado = buscar_vertice(grafo, 'Red Hat')
marcar_no_visitado(grafo)'''
'''barrido_amplitud(grafo, buscado)
print('Barrido en profundidad desde Debian')
buscado = buscar_vertice(grafo, 'Debian')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde Debian')
buscado = buscar_vertice(grafo, 'Debian')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''
'''print('Barrido en profundidad desde Arch')
buscado = buscar_vertice(grafo, 'Arch')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde Arch')
buscado = buscar_vertice(grafo, 'Arch')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''


# Ej 6
'''grafo = Grafo(True)
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for vertice in vertices:
    insertar_vertice(grafo, vertice)

insertar_arista(grafo, 15, 'A', 'B')
insertar_arista(grafo, 13, 'A', 'D')
insertar_arista(grafo, 19, 'A', 'C')
insertar_arista(grafo, 2, 'B', 'C')
insertar_arista(grafo, 12, 'B', 'F')
insertar_arista(grafo, 20, 'B', 'E')
insertar_arista(grafo, 27, 'C', 'G')
insertar_arista(grafo, 9, 'C', 'F')
insertar_arista(grafo, 5, 'C', 'E')
insertar_arista(grafo, 45, 'D', 'G')
insertar_arista(grafo, 39, 'D', 'F')
insertar_arista(grafo, 1, 'E', 'F')
insertar_arista(grafo, 3, 'F', 'G')
'''
# punto A
'''print('Barrido en profundidad desde A')
buscado = buscar_vertice(grafo, 'A')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde A')
buscado = buscar_vertice(grafo, 'A')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''
'''print('Barrido en profundidad desde C')
buscado = buscar_vertice(grafo, 'C')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde C')
buscado = buscar_vertice(grafo, 'C')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''
'''print('Barrido en profundidad desde F')
buscado = buscar_vertice(grafo, 'F')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde F')
buscado = buscar_vertice(grafo, 'F')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''

# Punto B
'''print('Camino mas corto desde A hasta F')
camino = dijkstra(grafo, 'A', 'F')
if len(camino) <= 1:
    print('No hay camino')
else:
    print(camino)
print('Camino más corto desde C hasta D')
camino = dijkstra(grafo, 'C', 'D')
if len(camino) <= 1:
    print('No hay camino')
else:
    print(camino)
print('Camino mas corto desde B hasta G')
camino = dijkstra(grafo, 'B', 'G')
if len(camino) <= 1:
    print('No hay camino')
else:
    print(camino)'''

# Punto C
'''insertar_arista(grafo, 10, 'C', 'A')
insertar_arista(grafo, 20, 'C', 'B')
insertar_arista(grafo, 3, 'G', 'D')
'''
'''print('Barrido en profundidad desde A')
buscado = buscar_vertice(grafo, 'A')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde A')
buscado = buscar_vertice(grafo, 'A')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''
'''print('Barrido en profundidad desde C')
buscado = buscar_vertice(grafo, 'C')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde C')
buscado = buscar_vertice(grafo, 'C')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)'''
'''print('Barrido en profundidad desde F')
buscado = buscar_vertice(grafo, 'F')
marcar_no_visitado(grafo)
barrido_profundidad(grafo, buscado)
print()
print('Barrido de amplitud desde F')
buscado = buscar_vertice(grafo, 'F')
marcar_no_visitado(grafo)
barrido_amplitud(grafo, buscado)
'''

# punto D
'''matriz_adyacencia(grafo)'''


# Ej 7
# Punto A
'''grafo = Grafo(True)
cargarEj7(grafo)

# punto B
aristasEj7(grafo)
'''
# Punto C
'''grafo_aux = Grafo(False)
cargarEj7(grafo_aux)
aristasEj7(grafo_aux)
twitter = kruskal2(grafo_aux, 'T')
print('Camino mas corto twitter ', twitter)
facebook = kruskal2(grafo_aux, 'F')
print('Camino mas corto facebook ', facebook)
instagram = kruskal2(grafo_aux, 'I')
print('Camino mas corto instagram ', instagram)'''

# Punto D
'''vertice = buscar_vertice(grafo, 'X')
if existePaso2(grafo, vertice, 'Y', 'T'):
    print('Existe paso')
else:
    print('No existe paso')
'''
# Punto F
'''perfil = 'Y'
buscado = buscar_vertice(grafo, perfil)
if buscado is not None:
    aux = buscado.adyacente.inicio
    print('Seguidos por Y en Instagram:')
    while aux is not None:
        if aux.info[0] == 'I':
            print(aux.destino)
        aux = aux.sig'''


# Ej 9
'''planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino',
            'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Ahch-to', 'Anoat',
            'Christophsis', 'Coruscant', 'Crait', 'Eadu', 'Exegol']

grafo = Grafo(False)
for planeta in planetas:
    insertar_vertice(grafo, planeta)

insertar_arista(grafo, randint(0, 100), 'Alderaan', 'Scarif')
insertar_arista(grafo, randint(0, 100), 'Alderaan', 'Exegol')
insertar_arista(grafo, randint(0, 100), 'Alderaan', 'Crait')
insertar_arista(grafo, randint(0, 100), 'Alderaan', 'Endor')
insertar_arista(grafo, randint(0, 100), 'Endor', 'Tatooine')
insertar_arista(grafo, randint(0, 100), 'Endor', 'Naboo')
insertar_arista(grafo, randint(0, 100), 'Endor', 'Eadu')
insertar_arista(grafo, randint(0, 100), 'Endor', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Dagobah', 'Ahch-to')
insertar_arista(grafo, randint(0, 100), 'Dagobah', 'Crait')
insertar_arista(grafo, randint(0, 100), 'Dagobah', 'Christophsis')
insertar_arista(grafo, randint(0, 100), 'Dagobah', 'Anoat')
insertar_arista(grafo, randint(0, 100), 'Hoth', 'Crait')
insertar_arista(grafo, randint(0, 100), 'Hoth', 'Exegol')
insertar_arista(grafo, randint(0, 100), 'Hoth', 'Alderaan')
insertar_arista(grafo, randint(0, 100), 'Hoth', 'Naboo')
insertar_arista(grafo, randint(0, 100), 'Tatooine', 'Eadu')
insertar_arista(grafo, randint(0, 100), 'Tatooine', 'Endor')
insertar_arista(grafo, randint(0, 100), 'Tatooine', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Tatooine', 'Anoat')
insertar_arista(grafo, randint(0, 100), 'Kamino', 'Scarif')
insertar_arista(grafo, randint(0, 100), 'Kamino', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Kamino', 'Bespin')
insertar_arista(grafo, randint(0, 100), 'Kamino', 'Hoth')
insertar_arista(grafo, randint(0, 100), 'Naboo', 'Scarif')
insertar_arista(grafo, randint(0, 100), 'Naboo', 'Ahch-to')
insertar_arista(grafo, randint(0, 100), 'Naboo', 'Crait')
insertar_arista(grafo, randint(0, 100), 'Naboo', 'Alderaan')
insertar_arista(grafo, randint(0, 100), 'Mustafar', 'Eadu')
insertar_arista(grafo, randint(0, 100), 'Mustafar', 'Exegol')
insertar_arista(grafo, randint(0, 100), 'Mustafar', 'Anoat')
insertar_arista(grafo, randint(0, 100), 'Mustafar', 'Tatooine')
insertar_arista(grafo, randint(0, 100), 'Scarif', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Scarif', 'Bespin')
insertar_arista(grafo, randint(0, 100), 'Scarif', 'Naboo')
insertar_arista(grafo, randint(0, 100), 'Scarif', 'Mustafar')
insertar_arista(grafo, randint(0, 100), 'Bespin', 'Exegol')
insertar_arista(grafo, randint(0, 100), 'Bespin', 'Anoat')
insertar_arista(grafo, randint(0, 100), 'Bespin', 'Kamino')
insertar_arista(grafo, randint(0, 100), 'Bespin', 'Alderaan')
insertar_arista(grafo, randint(0, 100), 'Ahch-to', 'Christophsis')
insertar_arista(grafo, randint(0, 100), 'Ahch-to', 'Naboo')
insertar_arista(grafo, randint(0, 100), 'Ahch-to', 'Dagobah')
insertar_arista(grafo, randint(0, 100), 'Ahch-to', 'Hoth')
insertar_arista(grafo, randint(0, 100), 'Anoat', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Anoat', 'Eadu')
insertar_arista(grafo, randint(0, 100), 'Anoat', 'Kamino')
insertar_arista(grafo, randint(0, 100), 'Anoat', 'Bespin')
insertar_arista(grafo, randint(0, 100), 'Christophsis', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Christophsis', 'Exegol')
insertar_arista(grafo, randint(0, 100), 'Christophsis', 'Hoth')
insertar_arista(grafo, randint(0, 100), 'Christophsis', 'Dagobah')
insertar_arista(grafo, randint(0, 100), 'Coruscant', 'Alderaan')
insertar_arista(grafo, randint(0, 100), 'Coruscant', 'Tatooine')
insertar_arista(grafo, randint(0, 100), 'Coruscant', 'Anoat')
insertar_arista(grafo, randint(0, 100), 'Coruscant', 'Kamino')
insertar_arista(grafo, randint(0, 100), 'Crait', 'Coruscant')
insertar_arista(grafo, randint(0, 100), 'Crait', 'Endor')
insertar_arista(grafo, randint(0, 100), 'Crait', 'Mustafar')
insertar_arista(grafo, randint(0, 100), 'Crait', 'Kamino')
insertar_arista(grafo, randint(0, 100), 'Eadu', 'Naboo')
insertar_arista(grafo, randint(0, 100), 'Eadu', 'Scarif')
insertar_arista(grafo, randint(0, 100), 'Eadu', 'Bespin')
insertar_arista(grafo, randint(0, 100), 'Eadu', 'Hoth')
insertar_arista(grafo, randint(0, 100), 'Exegol', 'Crait')
insertar_arista(grafo, randint(0, 100), 'Exegol', 'Christophsis')
insertar_arista(grafo, randint(0, 100), 'Exegol', 'Mustafar')
insertar_arista(grafo, randint(0, 100), 'Exegol', 'Alderaan')
'''
# Punto C
'''arbol_min = kruskal(grafo)
print('Arbol de expansion minima')
print(arbol_min)'''

# Punto D
'''print('Camino mas corto desde Tatooine y Dagobah')
print(dijkstra(grafo, 'Tatooine', 'Dagobah'))'''
'''print('Camino mas corto desde Alderaan y Endor')
print(dijkstra(grafo, 'Alderaan', 'Endor'))'''
'''print('Camino mas corto desde Hoth y Tatooine')
print(dijkstra(grafo, 'Hoth', 'Tatooine'))'''

# Punto E
'''print('Planeta a los que se puede llegar desde Tatooine')
buscado = buscar_vertice(grafo, 'Tatooine')
if buscado:
    adyacente(buscado)'''


# Ej 10
'''grafo = Grafo(False)
cargar_ej10(grafo)
'''
# Punto C
'''print(kruskal(grafo))'''

# Punto D
'''camino_mas_corto = dijkstra(grafo, 'Partenon', 'Delfos')
print('El camino mas corto entre el Partenon y Delfos es: ', camino_mas_corto)'''