# 9
""" 
print = 5
in  = 5
for = 4
In = 5
 """

# 14
nums = [1,2,3]
vals = nums
del vals[:]

print(vals, nums)

# 22
lst = [i for i in range(-1,-2)]
print("lista", lst)

# 23
def fun(a, b, c= 0):
    pass


# fun()
fun(b=0, a=0)
# fun(b=1)
fun (0,1,2)

# 24
def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x,y-1)

print(fun(0,3))

# 26
tup = (1,2,4,8)
tup = tup[-2:-1]
print(tup)
tup = tup[-1]
print(tup)

# 30
list = [[x for x in range(3)] for y in range(3)]
print(list)

# 32
'''
try:
    print(5/0)
    break
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")
'''
# 33

# foo = (1,2,3)
# print(foo.index(0))

# 35
# print(Hello, World!)

z = 0
y = 10
x = y < z and z > y or y < z and z < y
print(x)

