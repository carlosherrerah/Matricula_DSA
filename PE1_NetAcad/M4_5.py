# Creating multi-parameter functions
# \ backslash = continued on the next line without spaces

def bmi(weight, height):
    if weight < 20  or weight > 200 or \
       height < 1.0 or height > 2.5:
        return None
    return weight / height ** 2

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def factorial(n):
    r = 1
    for i in range(2,n+1):
        r= r*i
    return r

# recursion is a technique where a function invokes itself.
# n! = n * (n-1)!
def factorial_R(n):
    if n == 1:
        return 1
    return n * factorial_R(n-1)

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

# Fibi = Fibi-1 + Fibi-2
def fib_R(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
 
print("fun ", fun(25))


# print(bmi(352.5, 1.65))
print(factorial(0))
print(factorial_R(5))
for n in range(1, 10): # testing
    print(n, "->", fib_R(n))

 







