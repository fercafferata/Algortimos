from tdahash import *

# Ej 1
'''tabla = crearTA(26)


def hash(p):
    if len(p) > 0:
        clave = ord(p[0]) - 97
    return clave


def insertar(tabla, p, desc):
    clave = hash(p)
    indice = clave % len(tabla)
    campos(tabla[indice], [p, desc], 0)


def buscar(tabla, p):
    indice = hash(p)
    return busquedalistaxcampo(tabla[indice], p, 0)

'''# No anda

'''
def eliminarhash(tabla, p):
    indice = hash(p)
    dato = busquedalistaxcampo(tabla[indice], p, 0)
    if dato is not None:
        eliminarCampo(tabla[indice], p, 0)
'''


'''def eliminar(tabla, p):
    indice = hash(p)
    if busquedalistaxcampo(tabla[indice], p, 0) is not None:
        eliminarCampo(tabla[indice], p, 0)
'''
# Punto A
'''insertar(tabla, 'perro', 'animal')
insertar(tabla, 'billetera', 'accesorio')
insertar(tabla, 'sillon', 'mueble')
insertar(tabla, 'horno', 'cocina')
insertar(tabla, 'zapato', 'calzado')
barridoTA(tabla)'''
# Punto B

# palabra = 'caja'
'''palabra = 'perro'
buscada = buscar(tabla, palabra)

if buscada is not None:
    print(str(buscada.info[0]) + ' ha sido encontrada')
    print('Significado: ' + str(buscada.info[1]))
else:
    print('La palabra ' + str(palabra) + ' no ha sido encontrada')
'''
# Punto C no anda
'''eliminar(tabla, 'perro')
print('Diccionario con la palabra perro eliminada')
barridoTA(tabla)'''


# Ej 2


# Ej 3
'''def cargarcatedra():
    cod = randint(100, 200)
    nombre = 'Catedra ' + str(randint(0, 100))
    modalidad = choice(['C', 'A'])
    horas = randint(1, 10)
    docentes = Lista()
    catedra = [cod, nombre, modalidad, horas, docentes]
    return catedra


def buscar(tabla, catedra):
    clave = hash(catedra)
    indice = clave % len(tabla)
    if tabla[indice][1] != catedra[1]:
        indice = rehash(tabla, indice)
    return indice


def docente(tabla, catedra):
    nom = 'Docente ' + str(randint(15, 50))
    docente = [nom]
    indice = buscar(tabla, catedra)
    if indice is not None:
        insertar(tabla[indice][4], docente)


tabla = crearTC(30)


def suma_digitos(codigo):
    return sum([int(c) for c in str(codigo)])


def hash(codigo):
    clave = suma_digitos(codigo)
    return clave


def insertar(tabla, dato):
    clave = hash(dato[0])
    indice = clave % len(tabla)
    if tabla is not None:
        tabla[indice] = dato
    else:
        indice = rehash(tabla, indice)
        if indice is not None:
            tabla[indice] = dato
        else:
            print('La tabla está llena')


for i in range(0, 40):
    catedra = cargarcatedra()
    insertar(tabla, catedra)


barridoTC(tabla)
'''


# Ej 4
'''def hash(p):
    if len(p) > 0:
        clave = ord(p[0]) - 97
    return clave


def nuevatabla(tabla):
    tabla1 = crearTC(len(tabla)*2)
    for personaje in tabla:
        if personaje is not None:
            insertar(tabla1, personaje)
    return tabla1


def carga(t):
    f = 0
    ocupados = 0
    for personaje in t:
        if personaje is not None:
            ocupados += 1
    f = (ocupados*100) / len(t)
    return f


def insertar(tabla, personaje):
    clave = hash(personaje)
    indice = clave % len(tabla)
    if tabla[indice] is not None:
        indice = rehash(tabla, indice)
    tabla[indice] = personaje
    if carga(tabla) > 75:
        tabla = nuevatabla(tabla)
        print('La tabla ha sido agrandada')
    return tabla
    

tabla = crearTC(20)
for i in range(0, 15):
    tabla = insertar(tabla, 'personaje' + str(randint(0, 19)))
barridoTC(tabla)
print(len(tabla))'''


# Ej 5
'''tabla = crearTC(30)


def hash(contacto):
    if len(contacto) > 0:
        clave = ord(contacto[0]) - 97
    return clave


def insertar_contacto(tabla, contacto):
    clave = hash(contacto[0] + contacto[1])
    indice = clave % len(tabla)
    if tabla[indice] is None:
        tabla[indice] = contacto
    else:
        indice = rehash(tabla, indice)
        if indice is not None:
            tabla[indice] = contacto
        else:
            print('La tabla esta llena')


for i in range(0, len(tabla)):
    apellido = 'apellido' + str(randint(0, 20))
    nombre = 'nombre' + str(randint(0, 20))
    email = 'email' + str(randint(2500, 6500))
    insertar_contacto(tabla, [apellido, nombre, email])

barridoTC(tabla)
'''


'''# Ej 6 ORDENA SIEMPRE IGUAL
legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']


def hash(codigo):
    if len(codigo) == 2:
        clave = (ord(codigo[0])) + (ord(codigo[1]))
    else:
        clave = (ord(codigo[3])) + (ord(codigo[4])) + (ord(codigo[5]))
    return clave



def hash(clave):
    indice = 0
    if len(clave) == 2:
        indice = (ord(clave[0])*3) + (ord(clave[1])*7)
    else:
        indice = ((ord(clave[0]) * ord(clave[1])) + ord(clave[2]))
    return indice



def busquedaTrooper(tabla, digitos):
    indice = hash(digitos)
    indice = indice % len(tabla)
    return tabla[indice]


def cargartrooper():
    legion = choice(legiones)
    cohoerte = str(randint(0, 9))
    siglo = str(randint(0, 9))
    escuadra = str(randint(0, 9))
    n_trooper = str(randint(0, 9))
    trooper = legion + '-' + cohoerte + siglo + escuadra + n_trooper
    return trooper


def insertar_trooper(tabla, trooper):
    legion, codigo = trooper.split('-')
    clave = hash(codigo[2:5])
    indice = clave % len(tabla)
    insertar(tabla[indice], trooper)
    

def insertar_trooper2(tabla, trooper):
    legion, codigo = trooper.split('-')
    clave = hash(legion)
    indice = clave % len(tabla)
    insertar(tabla[indice], trooper)


tabla = crearTA(2000) # por legion
tabla1 = crearTA(2000) # por digitos


def agregar(trooper):
    insertar_trooper(tabla, trooper)
    insertar_trooper2(tabla1, trooper)


for i in range(0, 2000):
    agregar(cargartrooper())

barridoTA(tabla)
print()
barridoTA(tabla1)

# Punto C
asalto = []
exploracion = []


def buscar_trooper(tabla, codigo):
    clave = hash(codigo)
    indice = clave % len(tabla)
    return tabla[indice]


buscado = busquedaTrooper(tabla, '781')
print(buscado.info)
if buscado.tamanio > 0:
    aux = buscado.inicio
    while aux is not None:
        if aux.info[4:] == '781':
            insertar(asalto, aux.info)
        aux = aux.sig

print(asalto)'''


# Ej 7
'''tipos = ['bicho', 'dragon', 'electrico', 'hada', 'lucha', 'fuego', 'volador', 'planta']
'''