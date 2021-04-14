from tdaarbol import *
import random
r = None

# ej1
'''for i in range(0, 1000):
    r = insertar(r, random.randint(0, 2000))
# Parte A
print('Barrido preorden:')
preorden(r)
'''
'''print('Barrido inorden:')
inorden(r)
print('Barrido postorden:')
postorden(r)'''

# Parte B
'''n = 40
if busqueda(r, n) is None:
    print('El numero no se encuentra en el arbol')
else:
    print('EL numero se encuentra en el arbol')
'''
# Parte C
'''for i in range(0, 3):
    dato1 = 10
    dato2 = 2
    dato3 = 7
    eliminar(r, dato1)
    eliminar(r, dato2)
    eliminar(r, dato3)
print('Arbol con valores borrados')
preorden(r)
'''
# Parte D
'''aux = altura(r.izq)
print('Altura del arbol izquierdo ' + str(aux))
aux1 = altura(r.der)
print('Altura del arbol derecho ' + str(aux1))
'''

# Parte E
'''repetidos(r)
'''


# Parte F
'''cp, ci = numParImpar(r)
print('Cantidad de numeros pares: ', cp)
print('Cantidad de numeros impares: ', ci)
'''

# Ej 2
'''def expresion(r=None):
    # expresion = (10/2) + (4*3)
    r = NodoArbol('+')
    r.izq = NodoArbol('/')
    r.izq.izq = NodoArbol(10)
    r.izq.der = NodoArbol(2)
    r.der = NodoArbol('*')
    r.der.izq = NodoArbol(4)
    r.der.der = NodoArbol(3)
    return r
    # expresion = (15x2-10) - (8/4)
    r = NodoArbol('-')
    r.izq = NodoArbol('-')
    r.izq.der = NodoArbol(10)
    r.izq.izq = NodoArbol('*')
    r.izq.izq.izq = NodoArbol(15)
    r.izq.izq.der = NodoArbol(2)
    r.der = NodoArbol('/')
    r.der.izq = NodoArbol(8)
    r.der.der = NodoArbol(4)
    return r'''

'''
r = expresion()
print('Preorden')
preorden(r)
print('La expresion se muestra en orden')
inorden(r)
print('Postorden')
postorden(r)

# punto B
print('Resultado: ' + str(calcular(r)))
'''

# Ej 4
'''r = NodoArbol(5)
r.izq = NodoArbol(3)
r.der = NodoArbol(7)
r.izq.izq = NodoArbol(10)
r.izq.der = NodoArbol(4)
r.der.izq = NodoArbol(9)
r.der.der = NodoArbol(2)
print('Inorden')
inorden(r)
print('Hijo izquierdo')
inorden(hijo_izquierdo(r))
print('Hijo derecho')
inorden(hijo_derecho(r))
'''

# ej5
# True heroe, false villano
'''sh = ['Capitan America ', 'Thor ', 'Hulk ', 'Black Widow ', 'Iron Man ',
        'Vision ', 'Hawkeye', 'Groot', 'Spider-man', 'Dr Strange']
        
villano = ['Thanos', 'Yellowjacket', 'Ultron', 'Red Skull', 'Iron Monger',
            'Loki', 'Vulture', 'Whiplash', 'Crossbones', 'The Mandarin']
contSH = 0
for i in range(10):
    r = insertar(r, [sh[i], True])
    contSH += 1
    r = insertar(r, [villano[i], False])'''
'''preorden(r)
print('Inorden')
inorden(r)'''

# Parte B
'''print('Villanos ordenados alfabeticamente')
villanos(r)'''

# Parte C
'''print('Superheroes con C')
sh_con_c(r)'''

# Parte D
'''print('Cantidad de superheroes: ' + str(contSH))'''

# Parte E
'''buscar = busquedaProxCampo(r, 'Dr Strange', 0)
if buscar is not None:
    buscar.info[0] = 'Doctor Strange'
    print('El nombre del personaje ha sido cambiado a ' + buscar.info[0])
else:
    print('El personaje no ha sido encontrado')

print('Arbol con el nombre del personaje modificado')
inorden(r)'''

# Parte F
'''print('Barrido inverso')
barridoInvertido(r)'''

# Parte G
'''bosque = [None, None]
separarHyV(r, bosque)
'''
# punto 1
'''print('Cantidad de nodos del arbol superheroes: ' + str(pesoArbol(bosque[0])))
print('Cantidad de nodos del arbol villanos: ' + str(pesoArbol(bosque[1])))'''

# punto 2
'''print('Arbol de superheroes')
inorden(bosque[0])
print('Arbol de villanos')
inorden(bosque[1])'''


# Ej7
'''r = NodoArbol(5)
r.izq = NodoArbol(3)
r.der = NodoArbol(7)
r.izq.izq = NodoArbol(10)
r.izq.der = NodoArbol(4)
r.der.izq = NodoArbol(9)
r.der.der = NodoArbol(2)
print('Inorden')
inorden(r)
print('Nodo minimo ', minimo(r).info)
print('Nodo maximo ', maximo(r).info)
'''


# Ej 8
'''tabla = [
            [0.2, 'A'],
            [0.17, 'F'],
            [0.13, '1'],
            [0.21, '3'],
            [0.05, '0'],
            [0.09, 'M'],
            [0.15, 'T']
        ]
diccionario = {
        'A': '00',
        '3': '01',
        '1': '100',
        '0': '1010',
        'M': '1011',
        'T': '110',
        'F': '111'
    }

tabla.sort()
r = crearArbolHuffman(tabla)
inorden(r)
mensaje = 'FAMA'
print('Mensaje a codificar: ', mensaje)
mensaje_codificado = codificar(mensaje, diccionario)
print('Mensaje comdificado: ', mensaje_codificado)
print('Mensaje decodificado: ', decodificar(r, mensaje_codificado))
'''

# Ej 9
'''r = NodoArbol(5)
r.izq = NodoArbol(3)
r.der = NodoArbol(7)
r.izq.izq = NodoArbol(10)
r.izq.der = NodoArbol(4)
r.der.izq = NodoArbol(9)
r.der.der = NodoArbol(2)
inorden(r)
nivel = 1
print('En el nivel ', nivel, ' hay ', nodosxnivel(r, nivel), ' tendría que haber ', nodostotalXnivel(nivel), ' nodos')
'''

# Ej 10
'''for i in range(0, 20):
    r = insertar(r, i)
inorden(r)
'''
# punto A
'''
print('Hay ' + str(pesoArbol(r)) + ' nodos en el arbol')
'''

# punto B y C
'''print('Hay ' + str(contarHojas(r)) + ' hojas en el arbol')
print('Informacion de las hojas del arbol')
infoHojas(r)'''

# Punto D
'''nodo = 3
if nodo == r.info:
    print('El nodo ingresado es la raiz')
else:
    print('El padre de ' + str(nodo) + ' es ' + str(padre(r, nodo).info))
'''
# Punto E
'''
print('La altura del arbol es: ' + str(altura(r)))
'''


# Ej 11
'''niveles = 9
r = generarNiveles(niveles)
imprimirArbol(r)

# Punto A
nivel = 3
bosque = []
cortarNiveles(r, bosque, nivel)
print('Bosque sin los primeros tres niveles')
for arbol in bosque:
    print('------------------ Arbol ------------------')
    imprimirArbol(arbol)
'''
# Punto B
'''for arbol in bosque:
    print('Hay ' + str(pesoArbol(arbol)) + ' nodos en el arbol')
'''

# punto C
'''for arbol in bosque:
    print('Barrido preorden')
    preorden(arbol)
    print()
'''
# Punto D
'''aux = bosque[0]
mayor = 0
for arbol in bosque:
    if mayor < pesoArbol(arbol):
        mayor = pesoArbol(arbol)
        aux = arbol
print('El arbol con mayor cantidad de nodos tiene ', mayor, ' nodos y es el arbol con la raiz ', aux.info)
'''

# Punto E
'''aux = bosque[0]
for arbol in bosque:
    if arbolcompleto(arbol):
        print('El arbol con la raiz ', arbol.info, ' está completo')
    else:
        print('No hay ningun arbol completo')
'''


# Ej 12
'''mision = 'Itergalactica'
superheroe_para_mision(mision)'''


# Ej 13
'''tabla = [
        ['E', 500],
        ['T', 1500],
        ['I', 250],
        ['A', 750],
        ['N', 1250],
        ['M', 1750],
        ['S', 225],
        ['U', 275],
        ['R', 725],
        ['W', 775],
        ['D', 1225],
        ['K', 1275],
        ['G', 1725],
        ['O', 1775],
        ['H', 112],
        ['V', 237],
        ['F', 265],
        [' ', 285],
        ['L', 612],
        [' ', 737],
        ['P', 765],
        ['J', 785],
        ['B', 1112],
        ['X', 1237],
        ['C', 1265],
        ['Y', 1285],
        ['Z', 1612],
        ['Q', 1737],
        [' ', 1765],
        [' ', 1785],
        ['5', 55],
        ['4', 115],
        ['3', 247],
        ['2', 747],
        ['1', 795],
        ['6', 1055],
        ['7', 1606],
        ['8', 1755],
        ['9', 1778],
        ['0', 1788]
]

r = NodoArbolD(' ', 1000)
for item in tabla:
    r = insertarDecision(r, item[0], item[1])

mensaje1 = '.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- - .- -- . / .- .-.. --. --- / --.- ..- . / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. / .... --- -- -... .-. . .-.-.'
mensaje2 = '-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.'
mensaje3 = '-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.'
mensaje4 = '-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.'
mensaje5 = '.--. --- -.. .-. .. .- / .... .- -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-.'
m = '. ... / .-.. ..- -. . ...'
print('Dr. Abraham Erskine')
print(morse_decod(r, mensaje1))
print('Rocket Raccoon')
print(morse_decod(r, mensaje2))
print('Natasha Romanoff')
print(morse_decod(r, mensaje3))
print('Tony Stark')
print(morse_decod(r, mensaje4))
print('Steve Rogers')
print(morse_decod(r, mensaje5))
'''


# Ej 15
'''tabla = [
        [0.22, 'Despejado'],
        [0.15, 'Nublado'],
        [0.03, 'Lluvia'],
        [0.26, 'Baja'],
        [0.14, 'Alta'],
        [0.05, '1'],
        [0.01, '2'],
        [0.035, '3'],
        [0.06, '5'],
        [0.02, '7'],
        [0.025, '8']
]
diccionario = {
            'Despejado': '00',
            'Lluvia': '01011',
            'Nublado': '111',
            'Baja': '10',
            'Alta': '110',
            '1': '0100',
            '2': '011100',
            '3': '01111',
            '5': '0110',
            '7': '011101',
            '8': '01010',
}
tabla.sort()
r = crearArbolHuffman(tabla)

mensaje = mensajeSatelite()
print('Mensaje original: ', mensaje)
mensaje_comprimido = codificar_mensajeSatelite(diccionario, mensaje)
print('Mensaje codificado: ', mensaje_comprimido)
mensaje_decodificado = decodificar(r, mensaje_comprimido)
print('Mensaje decodificado: ', mensaje_decodificado)
diferencia = diferencia_tamanio(mensaje_comprimido, mensaje_decodificado)
print('Diferencia de tamaño: ', diferencia)
'''

# Ej 19
'''clima = [
        ['Visibilidad', 15],
        ['Humedad', 70],
        'Despejado',
        ['Viento', 8.7],
        ['Visibilidad', 8],
        ['Viento', 5],
        'Parcialmente Nublado',
        ['Presion', 1013],
        ['Humedad', 92],
        'Despejado',
        'Nublado',
        ['Humedad', 96],
        ['Viento', 7.2],
        ['Visibilidad', 12],
        ['Viento', 12.2],
        'Nublado',
        'Mayormente Nublado',
        ['Presion', 1018],
        'Nublado',
        'Despejado',
        'Mayormente Nublado',
        'Lluvia',
        'Nublado',
        ['Visibilidad', 1],
        'Nublado',
        'Lluvia',
        'Mayormente Nublado'
]

codigos = [3000, 1000, 3100, 500, 2100, 250, 750, 1400, 2500, 200, 300, 1300, 1900, 2300, 2700, 1100, 1200, 1700, 2000, 2200, 2400, 2600, 2800, 1500, 1800, 1450, 1600]
for i in range(0, len(clima)):
    r = insertarDecision(r, clima[i], codigos[i])

temperatura = random.randint(0, 50)
presion = random.randint(1000, 1050)
humedad = random.randint(0, 100)
visibilidad = random.randint(0, 50)
viento = random.randint(0, 100)

tiempo_meteorologico(r, temperatura, presion, humedad, visibilidad, viento)'''


# Ej 21
# criatura 0, vencedor 1, descripcion 2
'''tabla = [
            ['Ceto', '', ''],
            ['Tifon', 'Zeus', ''],
            ['Equidna', 'Argos Panoptes'],
            ['Dino', '', ''],
            ['Pefredo', '', ''],
            ['Enio', '', ''],
            ['Escila', '', ''],
            ['Caribdis', '', ''],
            ['Euriale', '', ''],
            ['Esteno', '', ''],
            ['Medusa', 'Perseo', ''],
            ['Cerda de cromion', 'Teseo', ''],
            ['Ortro', 'Heracles', ''],
            ['Toro de creta', 'Teseo', ''],
            ['Jabali de calidon', 'Atalanta', ''],
            ['Carcinos', '', ''],
            ['Gerion', 'Heracles', ''],
            ['Cloto', '', ''],
            ['Laquesis', '', ''],
            ['Atropos', '', ''],
            ['Minotauro de creta', 'Teseo', ''],
            ['Harpias', '', ''],
            ['Ladon', 'Heracles', ''],
            ['Aguila del Caucaso', '', ''],
            ['Quimera', 'Belerofonte', ''],
            ['Hidra de Lerna', 'Heracles', ''],
            ['Leon de Nemea', 'Heracles', ''],
            ['Esfinge', 'Edipo', ''],
            ['Dragon de la Colquida', '', ''],
            ['Cerbero', '', ''],
            ['Argos Panoptes', 'Hermes', ''],
            ['Aves del Estínfalo', '', ''],
            ['Talos', 'Medea', ''],
            ['Sirenas', '', ''],
            ['Piton', 'Apolo', ''],
            ['Cierva de Cerinea', '', ''],
            ['Basilisco', '', ''],
            ['Jabalí de Erimanto', '', '']
]

for i in tabla:
    r = insertar(r, i)
print('Barrido inorden: ')
inorden(r)
'''
# punto b
'''print('Cargar descripcion')
bus = busquedaCampo(r, 'Enio')
print('Criatura: ', bus.info[0])
print('Descripción: ', bus.info[2])

cargar_descripcion(r, 'Enio', 'Descripcion')
print('Criatura: ', bus.info[0])
print('Descripción: ', bus.info[2])
'''

# punto C
'''busc = busquedaCampo(r, 'Talos')
print('Criatura: ', busc.info[0])
print('Derrotado por: ', busc.info[1])
print('Descripcion: ', busc.info[2])'''

# punto D
'''venc = []
venc = vencedores(r, venc)
venc_aux = []
for item in venc:
    if item not in venc_aux:
        venc_aux.append(item)
for i in range(0, len(venc_aux)):
    aux = venc.count(venc_aux[i])
    venc_aux[i] = str(aux)+venc_aux[i]
venc_aux.sort(reverse=True)
print('Los 3 mas vencedores')
for i in range(0, 3):
    print(venc_aux[i][1:])
'''

# punto E
'''vencidos = []
vencidos = derrotadoPor(r, 'Heracles', vencidos)
print('Criaturas derrotadas por Heracles')
print(vencidos)'''


# punto F
'''noderrotados = []
noderrotados = derrotadoPor(r, '')
print('Criaturas no derrotadas')
print(noderrotados)
'''

# punto H
'''print('Sin las criaturas eliminadas')
print(inorden(r))
eliminar, clave = eliminarCampo(r, 'Basilisco')
eliminar, clave = eliminarCampo(r, 'Sirenas')
print('Con las criaturas eliminadas')
print(inorden(r))'''

# punto I
'''buscado = busquedaCampo(r, 'Aves del Estínfalo')
buscado.info[1] = 'Heracles'
buscado.info[2] = 'Derroto a varias aves'
inorden(r)'''

# punto J
'''buscado = busquedaCampo(r, 'Ladon')
buscado.info[0] = 'Dragon ladon'
inorden(r)'''


# ej 22
'''tabla = [
        [1, 'Q', 0],
        [2, 'B', 0],
        [2, 'V', 0],
        [3, 'D', 0],
        [3, 'G', 0],
        [3, 'M', 0],
        [3, 'T', 0],
        [4, 'C', 0],
        [4, 'P', 0],
        [4, 'S', 0],
        [4, 'U', 0],
        [6, 'I', 0],
        [6, 'L', 0],
        [6, 'N', 0],
        [7, 'O', 0],
        [10, 'R', 0],
        [11, 'A', 0],
        [14, 'E', 0],
        [17, '‘ ’', 0],
        [2, ',', 0],
]
frecuencia(tabla)
r = crearArbolHuffman(tabla)
mensaje1 = '10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100'
mensaje2 = '0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010'
mensaje1_decodificado = decodificar(r, mensaje1)
mensaje2_decodificado = decodificar(r, mensaje2)
print('Mensaje 1: ')
print(mensaje1_decodificado)
print('Mensaje 2: ')
print(mensaje2_decodificado)
tamanio1 = diferencia_tamanio(mensaje1, mensaje1_decodificado)
print('Diferencia de tamanio entre mensaje1 codificado y decodificado: ', tamanio1)
tamanio2 = diferencia_tamanio(mensaje2, mensaje2_decodificado)
print('Diferencia de tamanio entre mensaje2 codificado y decodificado: ', tamanio2)
'''