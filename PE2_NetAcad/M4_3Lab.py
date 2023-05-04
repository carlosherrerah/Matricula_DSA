# 4.3.8   LAB   Histograma de frecuencia de caracteres
'''
from os import strerror

def my_filtering_function(pair):
    key, value = pair
    if value > 20:
        return True  # keep pair in the filtered dictionary
    else:
        return False  # filter pair out of the dictionary


abc = {}
first = ord('a')
for i in range(26):
    abc[chr(first+i)] = 0
    i += 1
abc = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}   # Equivalente
print(abc)

#new_abc = dict(filter(my_filtering_function, abc.items()))
new_abc = dict(filter(lambda elem: elem[1] > 20, abc.items()))
new_abc = dict(filter(lambda elem: elem[0] in 'AEIOU'.lower(), abc.items()))

texto = 'Juan Carlos'
for X in texto.lower():
    # if X.isalpha():
    if X in abc.keys():
        #abc[X] = abc.get(X)+1
        abc[X] += 1
print(abc)
new_abc = dict(filter(lambda elem: elem[1] > 0, abc.items()))
print(new_abc)

# ------------------------------------------------------------------------------
# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
from os import strerror
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra...
            if char in counters.keys():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1
    file.close()
    # Imprimamos los contadores.

    for char in counters.keys():
        pass
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):  # Orden por Valor Reversa   
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

listofTuples = sorted(counters.items(),  key=lambda x: x[1])
print(listofTuples)


# 4.3.9   LAB   Histograma de frecuencia de caracteres ordenado

archivo="Text.txt"
pos = archivo.index('.')
print(archivo[:pos]+".hist")

sorted_dict = dict(sorted(counters.items(),
                          key=lambda item: item[1],
                          reverse=True))
print(sorted_dict)
'''

# 4.3.10   LAB   Evaluating students' results
