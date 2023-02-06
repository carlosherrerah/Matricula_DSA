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
print("-->", list_2)
# the name of an ordinary variable is the name of its content;
# the name of a list is the name of a memory location where the list is stored.

# It actually copies the list's contents, not the list's name.
list_1 = [3, 5, 8, 2, 9, 7]
list_2 = list_1[:]   # my_list[start:end]   powerful slices 
list_1[0] = 10
print(list_2)
print("Lista1 ---->")
print(list_1)
print(list_1[2:4])            # [  :    )
print(list_1[:])              # all
print(list_1[0: len(list_1)]) # all
print(list_1[1:-1])           # [  : end)
print(list_1[1:])             # [1 : end]
print(list_1[:3])             # [0 :   3)

a = 0 ^ 1
print(a)

nums = [1,2,3]
vals = nums[-1:-2]
print(vals)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list)

del list_1[1:3]
del list_1[:]
del list_1

my_list = [10, 3, 12, 8, 2]
print(12 in my_list)

largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
# print(np.max(my_list))

find = 8
found = False
for i in range(len(my_list)):
    found = my_list[i] == find
    if found: break
if found:
    print("index: ", i)
else:
    print("absent")    
# print(my_list.index(18))    

# how many numbers are in drawn
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_new=[]

# Elements unique
for i in range(len(my_list)):
    if my_list[i] not in my_new:
        my_new.append(my_list[i])
print(my_new)















