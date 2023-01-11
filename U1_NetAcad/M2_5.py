# section 5 comment for line

''' 
coments for block
in python
'''

def doble(x):
    y = x * 2
    return y

a = [5,2,7,9,3]

for i in range(0, len(a)):
    print(a[i])

# Bubble sort
for i in range(0, len(a)+1 -2):
    for j in range(0,len(a)+1 - i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x

print(a)
b=10
if b>10:
    print("Mayor a 10")
else:
    print("menor a 10") 

print(doble(10))

print(". . . Hecho")







