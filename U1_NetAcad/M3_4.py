# Lists
# our list is a collection of elements, but each element is a scalar
numbers = [10, 5, 7, 2, 1]

for i in range(0, len(numbers)):   # length
    print(numbers[i], end="\t")
print()
for i in numbers:
    print(i, end="\t")
print()

    
numbers[0] =111    # Accessing list content
print(numbers)

numbers.remove(7)  # Remove the first occurrence of value
# del numbers[1]   # Remove by position

print(numbers)
4.4. 


# -----------------------------------------------------------------------------
'''
print((lambda x:x+3)(4))
nombre = "Universidad Politecnica"
print(nombre[6:10])
x = nombre.split()
print(x[1])
# numbers.sort()

class Beer:
    def __init__(self):
        self.content = 1.0
    
    def drink(self):
        self.content = 0.0

becks = Beer() # constructor - create class
print(becks.content) # beer empty: b.content == 0
'''