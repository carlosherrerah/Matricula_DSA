# section 5 comments
# section 6 Interaction with the user
import os
import time

print("What is your last name")
lastName = input()

Name = input("What is your name: ")

Edad = int(input("Give me a number: "))  # casting: int() , float()
print(type(Edad))  # Tipo

complete_name = Name + " " + lastName    # concatenation
print("Hi", complete_name, "your number is", Edad)
print("Hola"*2, 2*"Adios")

# os.system("cls")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
time.sleep(2)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
leg_c = (leg_a**2 + leg_b**2) ** .5

print(leg_c)
print(round(leg_c,4))
print("%.3f" % leg_c)
print(f'{leg_c:.2f}')

print(f'{1000000:,.2f}')   # separados por comas
print(f'{123:0<6d}')       # right padding with 0

print("Hypotenuse length is " + str(leg_c))    # casting  str()


# -----------------------------------------------------------------------------

# Lab1 
x = float(input("Enter value for x: "))
y = 1 / ( x + 1/(x+1/(x + 1/x)))
print("y =", y)

# Lab2
'''
               hh:mm 
Example: start 12:17
         last     59
         End   13:16 
'''
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

tot_min = mins + dura
add_hor = tot_min // 60
res_min = tot_min %  60

tot_hor = hour + add_hor 
res_hor = tot_hor % 24 
print(res_hor,":", res_min)

# Exam
# The value twenty point twelve times ten raised to the power of eight should be written as: 20.12E8
# multiplications precede additions  
# the ** operator uses right-sided binding
# Which of the following variable names are illegal? TRUE and True true  
