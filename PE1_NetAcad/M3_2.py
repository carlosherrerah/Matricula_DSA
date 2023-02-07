# Loop 
# An infinite loop = endless loop    Ctrl C = Break

even_numbers = 0   # Par
odd_numbers = 0    # Impar

number = int(input("Enter a number or type 0 to stop: "))
while number != 0:
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))

print("Even numbers count: ", even_numbers)
print("Odd  numbers count: ", odd_numbers)
 
counter = -3
while counter:
    print("Inside the loop.", counter)
    counter += 1
print("Outside the loop.", counter)

'''
while True:
    print("Hello")
'''

#  Secret Number
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


# range() function accepts only integers as its arguments
for i in range(10): # 0..9  range(1,11)=1..10  range(2,8,3)=
    pass
    # continue
    print(i)
    break
    print("hola")
print("Fin")


# Example: word without vowels
user_word = input("Gime a Word: ")
user_word = user_word.upper()
new_word = ""
for letter in user_word:
    if letter not in ("A","E","I","O","U"):
        new_word += letter
print(new_word)

for i in range(3):
    print(i)
else:
    print("else:", i)

for i in range(3):
    print(i)
print("sino:", i)

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("else: ", i)

i = 1
while i <= 3:
    print(i)
    i += 1
print("sino: ", i)

# Sumatoria, No de bloques
# --------------------------------------------------------------
blocks = int(input("Enter the number of blocks: "))
suma=0
height=1
while suma <= blocks:
    suma+= height
    height+=1
height-=2
print("The height of the pyramid:", height)


'''
Collatz's hypothesis
1. take any non-negative and non-zero integer number and name it c0;
2.  if it's even, evaluate a new c0 as c0 ÷ 2;
3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4. if c0 ≠ 1, go back to point 2.
'''

c0=16
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 /2
    else:
        c0 = 3*c0+1
    print(c0)
    steps+=1
print("steps:", steps)


# SECTION SUMMARY
for digit in "0165031806510":
    if digit == "0":
        print("X", end="")
        continue
    print(digit,end="")

 
 



    