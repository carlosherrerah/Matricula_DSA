# Operations on lists
a = 5
b = a
print(b)
a = 6
print(b)

list_1 =[3,5]
list_2 = list_1
# copies the name of the array, not its contents.
# the same location in the computer memory
# Modifying one of them affects the other, and vice versa.

print(list_2)
list_1[0]=10
print(list_2)
# the name of an ordinary variable is the name of its content;
# the name of a list is the name of a memory location where the list is stored.

# It actually copies the list's contents, not the list's name.
list_1 = [3, 5]
list_2 = list_1[:]   # my_list[start:end]
list_1[0] = 10
print(list_2)
print(list_1)







