# Sección 3 – Métodos de Cadenas
'''
capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en mayúsculas.

endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?
'''

print('aBcD'.capitalize())
print(' aBcD'.capitalize())
print('[' + 'hola'.center(11) + ']')
print('[' + 'hola'.center(11,'*') + ']')

if "epsilon".endswith("on"):    # .startwith
    print("si")
else:
    print("no")

print("find: ")
print("Hello".find("lo"))       # regresa la posicion
print("Hello".find("la"))       # -1 si no existe
#      012345678
print('cacahuata'.find('a', 2))    # busca a partir de la posicion 4
print('cacahuata'.find('a', 7, ))  # ini, fin 
print('cacahuata'.find('a', 7, 8)) # ini, fin-1

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by the advertisements""" 
# Regresa las posiciones de la palabra the
print()
pos = the_text.find('the')
while (pos != -1):
    print(pos)
    pos = the_text.find('the', pos+1)

print('lambda30'.isalnum())
print('lambda 30'.isalnum())
print(''.isalnum())
print('20E1'.isalnum())

print('Mu40'.isalpha())
print("Year2019".isdigit())
print("3.1416".isdigit())
print("Moooo".islower())
print(' \n '.isspace())
print("Moooo".isupper())

a =",".join(["A", "B", "C"])
print(a)
b = a.split(",")
print(b)

print("SiGmA=60".lower())
print("[" + "  uno  dos  ".lstrip() + "]")   # left trim
print("www,cisco.com".lstrip(",w")) # izq elimina cualquiera de los caracteres   
print("cisco.com".rstrip(".com"))
print("[" + "   hello   ".strip() + "]")

print("Apple Juice".replace(" ", ""))
print("black and jack".replace("ck", "s",2)) # indica el numero de reemplazos

# rfind = reverse find, regresa la posicion
# string.rfind(value, start, end)
print("Mi casa es tu casa".rfind("casa"))
print("Mi casa es tu casa".rfind("casa",4, ))

print("phi       chi\npsi".split())  # separar por espacio

print("Hello World".swapcase()) # upper to lower and vs
print("hello world".title())    
print("Hello World".upper())    
print("Hello World".count("lo")) # cuenta las ocurrencias 

# Cuestionario



