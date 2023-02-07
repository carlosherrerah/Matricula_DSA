import math 
from math import log10
P = ['5', '6', '2', '+', '*', '12', '4', '/', '-']
P = ['2', '3', '^', '4', '1', '*', '/', '11', '1', '-', '2', '^', 'log10', '+']
fn =['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log','log10'] # log log10 exp pow
stack = []
operando = type(P[0]) in [int, float]
operando2 = float(P[0])
'''
for i in P:
    if i in ['^','*','/','+','-']:
        b = stack.pop()
        a = stack.pop()
        c = str(eval(a+i+b))
        stack.append(c)
    else:
        stack.append(i)
value = float(stack.pop());                
print(value)
'''
print(eval('2**3'))

for i in P:
    if i in ['^','*','/','+','-']:
        i ='**' if i =='^' else '^'
        b = stack.pop()
        a = stack.pop()
        c = str(eval(a+i+b))
        stack.append(c)
    elif i in fn:
        a = stack.pop()
        c = str(eval(i+'('+ a + ')'))
        stack.append(c)
    else:
        stack.append(i)
value = float(stack.pop());     
print(value)           
