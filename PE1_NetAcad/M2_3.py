# Operators - data      manipulation tools

entero = 7 // 2  #  -7 // 2  rounding goes toward the lesser integer value (floor division)

residuo = 7 % 2  # modulo
potencia = 2**3
raiz = 16 ** .5
# when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.
print(entero)
print(residuo)
print(potencia)
print(-2 ** 2)
print(6. // -4)  # -2

print(12 % 4.5)  # 3.0
# 12  // 4.5 gives 2.0,
# 2.0 *  4.5 gives 9.0,
# 12  -  9.0 gives 3.0.


print(-4 - -4)     # unary operator
print(9 % 6 % 2)   # left-sided binding  1
print(2 ** 2 ** 3) # right-sided binding 


