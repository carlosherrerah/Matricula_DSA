# Returning a result from a function
# None = Null

import numpy as np
# print(None + 2)
a = None
b = True if a==None else False
print(b)

def no_return():
    pass

print(no_return())

# Problem: Number of days elapsed during the year
def isLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    suma = 0
    for i in range(12):
        suma = suma + dias[i]
    suma = np.sum(dias[0:month-1])           
    total = suma+1 if isLeap(year) else suma
    return suma

def day_of_year(year, month, day):
    
    total = days_in_month(year, month)+day
    return total

print(day_of_year(2000,2,2))

# A natural number is prime if it is greater than 1 and 
# has no divisors other than 1 and itself.

def es_primo(num):   # Error en 1 y 2
    if num % 2 == 0:
        return False
    for i in range(3,num,2):    # range(start, stop, step)
        if num % i == 0:
            return False
    return True

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

print(type("hola")==str)  # int float str

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
 
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(miles_gallon_to_liters_100km(60.3))


