# Section 6 – Tuples() and dictionaries {}
# Los datos mutables pueden ser actualizados libremente en cualquier momento
# Una tupla () solo puede ser asignada y leída : inmutable
# cada elemento de una tupla puede ser de distinto tipo

tupla = (1,2,4,8)
# tupla[2] = 3  # No es soportado
# del tupla[2]  # No es soportado
print(tupla[2])
print(tupla[2:])

for elem in tupla:
    print(elem)

tupla2 = tupla + (3, 5, 7)   # unir tuplas
print(tupla2)

tupla3 = tupla * 3           # multiplicar tuplas = repetir los elementos n veces 
print(tupla3)

print(8 in tupla)

var = 55
t0 = ()
t1 = (1, )
t2 = (4, 6, 8, "Ten")
t3 = (5, var )
t4 = [10, var]

t1, t2 = t2, t1
print(t1)
print(t2)
print(t3)
print(t4)

# Diccionarios { clave: valor}
# son colecciones indexadas de datos, mutables y desordenadas.
# La llave debe ser unica y sensible, de cualquier tipo, pero no una lista
# Se busca en base a la llave, no al valor
# No guardan el orden de sus datos

dict0 = {}   # vacia
dict1 = {"gato":"miau", "Perro": "guau", "raton":1}
dict2 = {"gato":"miau", "Perro": "guau", "raton":1, 3:"tres", 4:40}
dict2.clear()
dict2 = dict1.copy()

print(dict1)
print(len(dict1))
print(dict1["Perro"])
print(dict1.get("Perro"))    # igual al anterior

print("gata" in dict1)
dict1['Perro']="ladra"              # Cambiar
dict1["loro"]="habla"               # agregar
dict1.update({"perico":"canta"})    # agregar
del dict1["perico"]                 # Eliminar una clave
dict1.pop("raton")                  # Eliminar por clave
dict1.popitem()                     # Eliminar ultimo elemento

print("\nDiccionarios:")
for llave in dict1:
    print(llave)

for llave in sorted(dict1.keys()):
    print(llave, ":", dict1[llave])
print()

for llave, valor in dict1.items():
    print(llave, "->", valor)
print()

for valor in dict1.values():
    print(valor)
print()

school_class={"carlos": (9,7,8,9), "juan":(8,9,4,7)}
school_class["charlie"] = (5,)     # primera vez
school_class["charlie"] += (10,)   # ya existe, agregar
print(school_class)

# Average by student
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# Puntos Clave: tuplas ()
# Las Tuplas son colecciones de datos ordenadas e inmutables
# lo que significa que no se puede agregar, modificar, cambiar o quitar elementos.

my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)

tupla1 = ("uno",)
tupla2 = "uno",
print(type(tupla2))

# convertir a tupla
lista = [2, 5, 8]
tupla = tuple(lista)

nombre ="UPA"
tupla2 = tuple(nombre)
print(tupla2)    

# convertir a lista
tupla = 1,2,3, 
lista = list(tupla)
print(lista)


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
print(tup.count(2))  # Numero de dos en la tupla

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

# Unir dos diccionarios 
for item in (d1, d2):
    d3.update(item)
print(d3)

# convetir de tupla a Diccionario
colors = (("green", "#008000"), ("blue", "#0000FF"))
colores = dict(colors)
print(colores)

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }


#------------------------------------------------------------------------------
 ## Companies
c = {'CoolCompany' : {'Alice' : 33, 'Bob' : 23, 'Frank' : 29},
     'CheapCompany' : {'Ann' : 4, 'Lee' : 9,'Chrisi' : 7},
     'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}

## One-Liner to find illegal companies
i = [x for x in c if any (y<9 for y in c[x].values())]
print(i)
# ['CheapCompany', 'SosoCompany']

## Data
cols = ['name', 'salary', 'job']
db = [('Alice', 180000, 'scientist'),
      ('Bob', 99000, 'manager'),
      ('Frank', 87000, 'CEO')]

## One-Liner
db = [dict(zip(cols, row)) for row in db]

## Result
print()
print(db)




