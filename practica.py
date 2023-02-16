infix = "A + ( B * C - ( D / E ^ F ) * G ) * H"

infix = infix.split()
print(infix)
# infix.pop()
print(infix[-1])
infix.insert(0,"(")
print(infix)


fn = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log', 'aln', 'alog']
#                                                   log   log10  e^x     10^
#    
