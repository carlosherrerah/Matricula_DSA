# Making decisions in Python
import array as arr

a = 1 == 1.
print(a)

a = 0
print(a != 0)
# n = int(input("Numero: "))
# print(n >= 100)

# colon = dos puntos =  :
# indentation = sangria
# the recommendation is to use 4 spaces of indentation), 
# or by using the tab character;
# Python 3 does not allow the mixing of spaces and tabs for indentation

the_weather_is_good = True

print("\n--> 1")
if the_weather_is_good:
    print("go_for_a_walk")
    print("drink a beer")
print("have_lunch")
print("Take a rest") 

print("\n--> 2")
if the_weather_is_good:
    print("go_for_a_walk")
    print("drink a beer")
else:
    print("have_lunch")
print("Take a rest") 

print("\n--> 3")
age = 20
if the_weather_is_good:
    if age > 18:
        print("drink a beer")
    else:
        print("go_for_a_walk")
else:
    print("have_lunch")
print("Take a rest") 

print("\n--> 4")
sex = "H"
age = 10
the_weather_is_good = None

if the_weather_is_good:
    print("go_for_a_walk")
elif age > 18:
    print("drink a beer")
elif not sex == "H":
    print("have_lunch")
else:
    print("Take a rest")

print()
number1 = 6
number2 = 5
# may be misleading
if number1 > number2: larger_number = number1
else: larger_number = number2
print("The larger number is:", larger_number)

# find the largest number from 3 numbers without using operator "and" "or" 
a = 19
b = 20
c = 15

m = a
if a > m:
    m = a
if b > m:
    m = b
if c > m:
    m = c
print("Mayor: " , m)    

print('-->and')
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

print('--->sin')
if a>b:
    if a>c:
        print(a)
    else:  # a>b c>a
        print(c)
elif b>c:  # b>a
    print(b)
else:  # b>a  c>b
    print(c)

a = max(5,2,9,3)
print(a)

a = (5,2,9,3)   # tuple
print(max(a))
print(type(a))

a = [5,2,9,3]   # list
print(max(a))
print(type(a))

a = arr.array('i', [5,2,9,3])   
print(max(a))
print(type(a))  # array











