# Lists
# our list is a collection of elements, but each element is a scalar

# c:\> pip install numpy
import numpy as np

numbers = [10, 5, 7, 9, 2, 8]
# numbers.sort()
ordenado = sorted(numbers)
print(ordenado)

for i in range(0, len(numbers)):   # length
    print(numbers[i], end="\t")
print()
for i in numbers:
    print(i, end="\t")
print()

numbers[0] = 111   # Accessing list content
print(numbers)

numbers.remove(7)  # Remove the first occurrence of value
del numbers[1]     # Remove by position

print(len(numbers))
print(numbers[3])  # IndexError: list index out of range
print(numbers[-2]) # the element before last in the list

# removes the last element from the list
numbers.pop()
del numbers[-1]
print(numbers)

# insert at the end of the list
numbers.append(13)

# insert at any place int the list
numbers.insert(3,33)  # position, value

print("--->", numbers)
# Function
# result = function(arg)
r = len("hello")

# Method
# result = data.method(arg)
name = "Universidad"
r = name.replace("sida", "vih")
print(r)

# methods
# list.append(value)            # Insert at the end     
# list.insert(location, value)  # Insert in the position

my_list = []  # Creating an empty list.
suma=0
for i in range(5):
    my_list.append((i+1)*10)
    # my_list.insert(0, (i+1)*10)
    suma+=my_list[i]
print(my_list)
print(suma)
print(np.sum(my_list))

# swap
a = 5
b = 6
a, b = b, a
print(a,b)

# list.remove()
 
# ramirez, gutierrez, Quinones
# Without using reverse.
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)

# The list is a type of data in Python used to store multiple objects.
my_list = [1, None, True, "I am a string", 256, 0]

# Lists can be nested
my_list = [1, 'a', ["list", 64, [11, 22], False]]
print(my_list[2][2])
print(my_list[2][2][1])
del my_list

nombre = "  Universidad Politecnica    "
nombre = nombre.strip()   # trim
print(nombre[6:10])
x = nombre.split()
print(x[1])

# -----------------------------------------------------------------------------
'''
class Beer:
#    def __init__(self):
#        self.content = 1.0
#        self.a =""

    def __init__(self, a):
        self.content = 2
        self.a = a

    def __len__(self):
        return len(self.a)

    def drink(self):
        self.content = 0.0

becks = Beer("Hola") # constructor - create class
print(becks.content) # beer empty: b.content == 0
print(becks.__len__()) # beer empty: b.content == 0

'''