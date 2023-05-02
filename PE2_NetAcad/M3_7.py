# Seccion 7. Prueba del Modulo   17 questions

# 4
class A:
    def __init__(self,v):
        self.__a = v + 1
 
a = A(0)
# print(a.__a)   # Error porque esta oculta

# 7 
class A:
    A = 1
 
print(hasattr(A,'A'))

# 8
class A:
     def __init__(self):
        pass
  
# a = A(1)               # Genera una exception
# print(hasattr(a,'A'))   

# 13 Que imprimirá
class A:
    v = 2
 
class B(A):
    v = 1
 
class C(B):
    pass
 
o = C()
print(o.v)
 
# 16
class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)
 
try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)

# 17
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
 
 
for x in I():
    print(x,end='')