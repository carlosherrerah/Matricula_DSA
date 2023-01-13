'''
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
''' 
# ---------------------------------------------------------------------------------
'''
if-elif-else

Leap year or Common year
Gregorian calendar (in 1582)

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



