# Section 6 – Tuples and dictionaries
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

tupla3 = tupla * 3   # repetir los elementos n veces 
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

# Diccionarios {}    # key: value
# mutable
# La llave debe ser unica y sensible, de cualquier tipo, pero no una lista
# Se busca en base a la llave, no al valor
# No guardan el orden de sus datos

dict0 = {}   # vacia
dict1 = {"gato":"miau", "Perro": "guau", "raton":1}
dict2 = {"gato":"miau", "Perro": "guau", "raton":1, 3:"tres", 4:40}

print(dict1)
print(len(dict1))
print(dict1["Perro"])
print("gata" in dict1)
dict1['Perro']="ladra"              # Cambiar
dict1["loro"]="habla"               # agregar
dict1.update({"perico":"canta"})    # agregar
del dict1["perico"]                 # Eliminar una clave
dict1.pop("raton")                  # Eliminar por clave
dict1.popitem()                     # Eliminar ultimo elemento

for llave in sorted(dict1.keys()):
    print(llave, ":", dict1[llave])
print()

for llave, valor in dict1.items():
    print(llave, "->", valor)
print()

for valor in dict1.values():
    print(valor)

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

# Resumen
# Puntos Clave: tuplas






    






