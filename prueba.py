print("P c \t p C")
P = []
p = []
C = []
c = []
for i in range(40):
    P.append(i // 10)    # Palo sort    
    c.append(i %  10)    # Cara no sort

    p.append(i %  4 )    # Palo no sort
    C.append(i // 4 )    # Cara sort
    print(i // 10, i % 10,'\t', i % 4, i // 4)
print()

# Error en la combinacion
#print(P)
#print(C)

# Error en la combinacion
# print(p)
# print(c)
