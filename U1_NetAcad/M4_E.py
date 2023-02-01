
# 7 
'''
a
b
c
print(k["0"])
print(k)
print(k[0])
print(k['0'])
'''


dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k)
# Insert your code here.
    print(k[0])

# 13
def fun(x):
    global y 
    y = x * x
    return y
fun(2)
print(y)

# 18
def fun(inp=2,out=3):
    return inp * out

print(fun(out=2))

tup = (1,2,3,4)
print(tup[0])

# print("a"/"a")

'''
# 16
my_list =  ['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list))
'''

'''
def fun(x):
    if x %2 == 0:
        return 1
    else:
        return
print(fun(fun(2))+1)    
'''