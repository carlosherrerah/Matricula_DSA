# Logic and bit operations
# and conjuction  ^
# or  disjunction v

# Morgan's laws.
# The negation of a conjunction is the disjunction of the negations.
# The negation of a disjunction is the conjunction of the negations.

# Bitwise operators
# & (ampersand) ‒ bitwise conjunction;
# | (bar)       ‒ bitwise disjunction;
# ~ (tilde)     ‒ bitwise negation;
# ^ (caret)     ‒ bitwise exclusive or (xor).

i = 34
j = 22
bit = i & j
print(bit)
print(~bit)

# binary left/right shift  
print(i>>1) # divide   by 2    2^1   i // 2
print(i<<3) # multiply by 8    2^3


