from tdalista import cargaAuto, insertar, eliminar, barrido
from tdalista import lista_vacia, tamanio, Lista, eliminarNodo
from tdalista import cargaString, insertar1, primo, busquedaLista
from tdalista import campos, busquedaxcampo
from tdalistaenlazada import insertar2, Lista2, barrido2, busquedacampos2
from tdalistaenlazada import campos2, tamanio2, busquedaLista2
import math
import string
import random
import calendar
import datetime
l1 = Lista()
l2 = Lista()
l3 = Lista()
l4 = Lista()
l5 = Lista()
l6 = Lista()


'''cargaAuto(l1, 5)
barrido(l1)
while l1.inicio is not None:
    eliminarNodo(l1)
    print('lista 1')
    barrido(l1)'''


# ej1
'''cargaAuto(l1, 10)
barrido(l1)
print('El tamanio es: ' + str(l1.tamanio))'''

# ej2
'''cargaString(l1, 10)
barrido(l1)
aux1 = l1.inicio
aux = l1.inicio
while aux is not None:
    if ((aux.info == 'a') or (aux.info == 'e') or (aux.info == 'i') or
    (aux.info == 'o') or (aux.info == 'u') or (aux.info == 'A') or
    (aux.info == 'E') or (aux.info == 'I') or (aux.info == 'O') or
    (aux.info == 'U')):
        eliminar(l1, aux.info)
    aux = aux.sig
print('lista sin vocales')
barrido(l1)'''


# ej3
'''cargaAuto(l1, 10)
barrido(l1)
aux = l1.inicio
while aux is not None:
    if aux.info % 2 == 0:
        insertar(l2, aux.info)
    else:
        insertar(l3, aux.info)
    aux = aux.sig
print('Lista de numeros pares:')
barrido(l2)
print('Lista de numeros impares:')
barrido(l3)'''


# ej4
'''cargaAuto(l1, 10)
barrido(l1)
insertar1(l1, 100, 3)
print("Lista con elemente agregado")
barrido(l1)'''

# ej5
'''cargaAuto(l1, 10)
barrido(l1)
print()
aux = l1.inicio
while aux is not None:
    if primo(aux.info):
        eliminar(l1, aux.info)
    aux = aux.sig
print('Lista sin numeros primos:')
barrido(l1)'''


# ej6 PARTE D TERMINAR
'''
sheroes = ['Linterna Verde', 'Wolverine', 'Ant Man', 'Ironman', 'Black Panter']
casas = ['Marvel', 'DC']
for i in range(0, 10):
    nombre = random.choice(sheroes)
    aparicion = random.randint(1000, 2000)
    casa = random.choice(casas)
    #biografia =
    super = [nombre, aparicion, casa]
    campos(l1, super, 0)
barrido(l1)'''

# Parte A
'''aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'Linterna Verde':
        eliminar(l1, aux.info)
    aux = aux.sig
print('Sin linterna verde')
barrido(l1)'''

# Parte B
'''aux = l1.inicio
print('Aparicion de Wolverine')
while aux is not None:
    if aux.info[0] == 'Wolverine':
        print(aux.info[1])
    aux = aux.sig'''

# Parte C
'''aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'Ant Man':
        aux.info[2] = 'Marvel'
    aux = aux.sig
print('Ant Man-Marvel')
barrido(l1)'''

# Parte D

# Parte E
'''print('Nombre y casa de heroes con anio de aparecion menor a 1963')
aux = l1.inicio
while aux is not None:
    if aux.info[1] < 1963:
        print(aux.info[0] + ' ' + aux.info[2])
    aux = aux.sig'''

# ej7
'''cargaAuto(l1, 5)
cargaAuto(l2, 5)
print('lista 1')
barrido(l1)
print('lista 2')
barrido(l2)
aux = l1.inicio
aux1 = l2.inicio
c = 0
while aux is not None:
    if aux.info != aux1.info:
        insertar(l3, aux.info)
        insertar(l3, aux1.info)
    else:
        c += 1
    aux = aux.sig
    aux1 = aux1.sig
print('listas unidas')
barrido(l3)
print('Hay ' + str(c) + ' elementos repetidos')
while not lista_vacia(l3):
    eliminarNodo(l3)
    print('Menos un nodo')
    barrido(l3)'''


# ej8 TERMINAR
'''while tamanio(l1) < 10:
    aleatorio = random.randint(-999, 999)
    if busquedaLista(l1, aleatorio) is None:
        if primo(aleatorio):
            #rango con anterior y siguiente +14
                insertar(l1, aleatorio)
        else:
            if aleatorio mod 2 != 0:
                #anterior y siguiente pares
                    insertar(l1, aleatorio)
barrido(l1)'''


# ej 9
'''
artistas = ["Arctic monkeys", "The strokes", "Miles Kane", "Oasis",
            "Radiohead", "The killers", "Coldplay", "Kings of leon",
            "The kooks", "Kasabian", "Josh Homme", "Foo fighters"]
for i in range(0, 50):
    nom = 'Nombre: ' + str(random.randint(0, 50))
    artis = random.choice(artistas)
    dur = random.randint(60, 180)
    reprod = random.randint(200, 1000)
    cancion = [nom, artis, dur, reprod]
    campos(l1, cancion, 1) # por nombre
    campos(l2, cancion, 3) # por reproducciones
print('Ordenado por nombre')
barrido(l1)
print('Ordenado por reproducciones')
barrido(l2)
'''
# Parte A
'''aux = l1.inicio
clarga = aux
while aux is not None:
    if (aux.info[2] > clarga.info[2]):
        clarga = aux
    aux = aux.sig
print('La cancion mas larga es ' + str(clarga.info))'''

# Parte B
'''
top = 10
cont = l2.tamanio - top
if (cont >= 0):
    aux = l2.inicio
    for i in range(0, l2.tamanio - top):
        aux = aux.sig
    print('Top' + str(top))
    while aux is not None:
        print(aux.info)
        aux = aux.sig
else:
    print("No es posible mostrar la lista pedida")
'''
# Parte C
'''aux = l1.inicio
while aux is not None:
    if aux.info[1] == 'Arctic monkeys':
        insertar(l2, aux.info)
    aux = aux.sig
print('Canciones de Arctic Monkeys')
barrido(l2)'''


# ej10
'''personajes = ['rey', 'darth vader', 'luke', 'leia', 'han solo', 'yoda',
              'chewbacca', 'grievous']
gen = ['Femenino', 'Masculino']
esp = ['humano', 'droide', 'wookies', 'ewoks', 'gungan', 'jawas']
pla = ['naboo', 'ender', 'kashyyyk', 'tatooine', 'coruscant', 'alderan']
for i in range(0, 10):
    nombre = random.choice(personajes)
    altura = random.randint(50, 200)
    edad = random.randint(400, 1500)
    genero = random.choice(gen)
    especie = random.choice(esp)
    planeta = random.choice(pla)
    episodio = random.randint(1, 9)
    pers = [nombre, altura, edad, genero, especie, planeta, episodio]
    insertar(l1, pers)
barrido(l1)'''

# Parte A
'''print('Lista de personajes femeninos')
aux = l1.inicio
while aux is not None:
    if aux.info[3] == 'Femenino':
        insertar(l2, aux.info)
    aux = aux.sig
barrido(l2)'''

# Parte B
'''print('Personajes de especie droide:')
aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'droide':
        if (aux.info[6] == 1 or aux.info[6] == 2 or aux.info[6] == 3 or
        aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6):
            insertar(l3, aux.info)
    aux = aux.sig
barrido(l3)'''

# Parte C
'''print('Informacion de Darth Vader')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'darth vader':
        insertar(l4, aux.info)
    aux = aux.sig
barrido(l4)'''

# Parte D
'''print('Personajes del episodio 4 al 7')
aux = l1.inicio
while aux is not None:
    if (aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6 or
       aux.info[6] == 7):
        insertar(l5, aux.info)
    aux = aux.sig
barrido(l5)'''

# Parte E
'''print('Personajes mayores a 850 anios')
aux = l1.inicio
while aux is not None:
    if aux.info[2] > 850:
        print(aux.info)
        insertar(l6, aux.info)
    aux = aux.sig

dat = l6.inicio
mayor = dat
while dat is not None:
    if dat.info[2] > mayor.info[2]:
        mayor = dat
    dat = dat.sig
print('El personaje de mayor edad es:')
print(mayor.info)'''

# Parte F
'''aux = l1.inicio
print('Sin personajes de episodios 4, 5 y 6')
while aux is not None:
    if aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6:
        eliminar(l1, aux.info)
    aux = aux.sig
barrido(l1)'''

# Parte G
'''aux = l1.inicio
while aux is not None:
    if aux.info[4] == 'humano':
        if aux.info[5] == 'alderan':
            insertar(l3, aux.info)
    aux = aux.sig
print('Personajes humanos de Alderan')
barrido(l3)'''

# Parte H
'''print('Personajes con menos de 70 centimetros')
aux = l1.inicio
while aux is not None:
    if aux.info[1] < 70:
        print(aux.info)
    aux = aux.sig'''

# Parte I
'''aux = l1.inicio
while aux.sig.sig is not None:
    aux = aux.sig
eliminar(l1, aux.info)
print('Lista sin el ante ultimo elemento')
barrido(l1)'''

# Parte J
'''print('Chewbacca')
aux = l1.inicio
while aux is not None:
    if aux.info[0] == 'chewbacca':
        insertar(l4, aux.info[6])
    aux = aux.sig
print('Aparece en los episodios:')
barrido(l4)'''


# ej14 FALTA PARTE H
'''
laux = Lista()
tipos = ['fuego', 'agua', 'planta', 'bicho', 'volador', 'veneno', 'electrico']
for i in range(1, 9):
    nombre = 'Entre' + str(i)
    t_ganados = random.randint(0, 10)
    b_perdidas = random.randint(0, 10)
    b_ganadas = random.randint(0, 10)
    for j in range(0, 3):
        nomb = 'Pokemon ' + str(random.randint(0, 6))
        nivel = random.randint(1, 40)
        tipo = random.choice(tipos)
        subtipo = random.choice(string.ascii_uppercase)
        pok = [nomb, nivel, tipo, subtipo]
        campos2(laux, pok, 0)
    entrenador = [nombre, t_ganados, b_perdidas, b_ganadas, laux]
    campos2(l1, entrenador, 0)
barrido2(l1)
'''
# Parte A
'''
buscado = 'Entre1'
laux = busquedaLista2(l1, buscado)
if (laux is not None):
    print("Pokemons de entrenador " + buscado)
    barrido2(laux.info[4])
else:
    print("El entrenador buscado no está en la lista")
'''

# Parte B
'''
print('Entrenadores con mas de 3 toneos ganados')
aux = l1.inicio
while aux is not None:
    if aux.info[1] > 3:
        print(aux.info)
    aux = aux.sig
'''
# Parte C
'''
aux = l1.inicio
e_mayor = aux.info[1]
while aux is not None:
    if aux.info[1] > e_mayor:
        e_mayor = aux.info[1]
        nom = aux.info
        nod = aux
    aux = aux.sig
print('El entrenador con mayores torneos ganados es: ' + str(nom[0]))
d = nod.info[4].inicio
dat = d
while d is not None:
    if d.info[1] > dat.info[1]:
        dat = d
    d = d.sig
print('y su pokemons de mayor nivel es: ' + str(dat.info))
'''
# Parte D
'''
aux = l1.inicio
print('Entrenadores con mas del 79% de batallas ganadas')
while aux is not None:
    porc = 100*(aux.info[3]/(aux.info[3] + aux.info[2]))
    if (porc > 79):
        print(aux.info[0])
    aux = aux.sig
'''
# Parte E
'''dat = l1.inicio
while dat is not None:
    aux1 = dat.lista
    aux = aux1.inicio
    while aux is not None:
        if aux.info[2] == 'fuego' or aux.info[2] == 'planta':
            insertar(l2, dat.info)
        elif aux.info[2] == 'agua' or aux.info[2] == 'volador':
            insertar(l3, dat.info)
        aux = aux.sig
    dat = dat.sig
print('Entrenadores con pokemons de tipo fuego y planta')
barrido(l2)
print('Entrenadores con pokemons de tipo agua y volador')
barrido(l3)'''
# Parte F
'''print('Ingrese el nombre del entrenador')
nombre = input()
aux = l1.inicio
ac = 0
while aux is not None:
    if aux.info[0] == nombre:
        aux1 = aux.lista
        dat = aux1.inicio
        while dat is not None:
            ac = ac + dat.info[1]
            dat = dat.sig
        prom = ac//tamanio(laux)
        print('El nivel de pokemons de ' + nombre + ' es ' + str(prom))
    aux = aux.sig'''
# Parte G
'''nom = 'Bulbasaur'
aux = l1.inicio
cont = 0
while aux is not None:
    aux1 = aux.lista
    aux2 = aux1.inicio
    while aux2 is not None:
        if aux2.info[0] == nom:
            cont += 1
            insertar(l2, aux.info[0])
        aux2 = aux2.sig
    aux = aux.sig
print('los entrenadores que tienen a ' + nom + ' son:')
barrido(l2)'''
# Parte H


# Ej 15
'''for i in range(1, 8):
    costo = randint(1500, 3500)
    tiempo = randint(2, 12)  # tiempo en horas
    dia = randint(1, 28)
    mes = randint(1, 12)
    anio = randint(2018, 2019)
    persona = 'Persona ' + str(i)
    tarea = [costo, tiempo, dia, mes, anio, persona]
    inserCampo(l1, tarea, 1)
barrido(l1)
aux = l1.inicio'''
# Punto A
'''a = 0
while aux is not None:
    a += aux.info[1]
    aux = aux.sig
prom = (a//7)
print('El tiempo promedio de tareas es de: ' + str(prom) + ' horas')'''

# Punto B
'''a = 0
while aux is not None:
    a += aux.info[0]
    aux = aux.sig
print('El costo total del proyecto es de: $' + str(a))'''
# Punto C
'''while aux is not None:
    if aux.info[5] == 'Persona 5':
        inserCampo(l2, aux.info, 5)
    aux = aux.sig
print('Actividades realizadas por Persona 5: ')
barrido(l2)'''

# Punto D
'''f1 = [7, 8, 2018]
f2 = [5, 9, 2019]
print('Tareas a realizar entre ' + str(f1) + ' y ' + str(f2) + ' : ')
while aux is not None:
    if entre(aux.info[2], f1[0], f2[0]) and entre(aux.info[3], f1[1], f2[1])
    and entre(aux.info[4], f1[2], f2[2]):
        print(aux.info)
    aux = aux.sig'''


# Ej17
'''
prod = ['Pendrive', 'Mouse', 'Teclado inalambrico', 'Disco solido', 'Monitor']
marc = ['Kingston', 'WD Blue', 'Genius', 'Dell']
for i in range(0, 12):
    codigo = random.randint(1111, 2222)
    producto = random.choice(prod)
    marca = random.choice(marc)
    mod = 'MOD' + str(random.randint(15, 298))
    precio = random.randint(400, 1000)
    cantidad = random.randint(0, 10)
    articulo = [codigo, producto, marca, mod, precio, cantidad]
    campos(l1, articulo, 1)
print('STOCK')
barrido(l1)
'''
# Punto A

# Punto B
'''
aux = l1.inicio
while aux is not None:
    if (aux.info[1] == 'Pendrive' and aux.info[2] == 'Kingston'):
        eliminar(l1, aux.info)
        print('Se han eliminado los articulos ingresados')
    aux = aux.sig
barrido(l1)
'''

# Punto D
'''
existencia = 0
costo = 0
aux = l1.inicio
while aux is not None:
    if (aux.info[1] == 'Disco solido'):
        costo = aux.info[4] * aux.info[5]
        existencia += costo
    aux = aux.sig
print(existencia)
'''

# Ej 18


# Ej 20
'''
nom = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(0, 20):
    nombre = random.choice(nom)
    precio = random.randint(20, 50)
    calif = random.randint(1, 5)
    articulo = [nombre, precio, calif]
    insertar(l1, articulo)
    campos(l2, articulo, 2)
print('ARTICULOS ORDENADOS POR NOMBRE')
barrido(l1)
'''
# Punto A
'''
buscado = 'G'
aux = l1.inicio
print('Articulo buscado')
while aux is not None:
    if aux.info[0] == buscado:
        print(aux.info)
    aux = aux.sig
'''

# Punto B
'''
print('Presione la tecla de acuerdo a la opción que desee')
print('1- Articulos ordenados por nombre')
print('2- Articulos ordenados por calificacion')
opcion = input()
print(opcion)
if opcion == '1':
    print('Articulos ordenados por nombre')
    barrido(l1)
    if opcion == '2':
        print('Articulos ordenados por calificacion')
        barrido(l2)
else:
    print('Presione la tecla que corresponda')
'''
# Punto D
'''
aux = l1.inicio
menor = aux.info[1]
while aux is not None:
    if aux.info[2] == 3:
        if menor > aux.info[1]:
            menor = aux.info[1]
    aux = aux.sig
print('Articulo mas barato con clasificacion 3')
print(menor)
'''

# Punto E
'''
aux = l1.inicio
print('Precio de los productos que empiezan con H')
while aux is not None:
    if aux.info[0] == 'H':
        print(aux.info[1])
    aux = aux.sig
'''