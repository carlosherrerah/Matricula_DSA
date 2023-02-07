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

#    E x e r c i s e s 

# ---------------------------------------------------------------------------------
# if else
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.
else:
    tax = (income-85528) * 0.32 + 14839.02
if tax < 0: tax=0;    

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 
# ---------------------------------------------------------------------------------
# if-elif-else

# Leap year or Common year
# Gregorian calendar (in 1582)
'''
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.

Tip: use the != and % operators
'''
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
    if year % 4 != 0:
        print("common year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 != 0:
        print("common year")
    else:
        print("leap year")

# They all change at the same time
x, y, z = 5, 10, 8
x, y, z = z, y, x

# -----------------------------------------------------------------------------
# SECTION SUMMARY
# Question 5: What is the output of the following snippet?
x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")











