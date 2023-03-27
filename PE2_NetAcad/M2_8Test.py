# UNICODE es un estandar como ASCII, pero mucho mas expansivo

try:
    print("5"/0)
except ArithmeticError:
    print("arit")
except ZeroDivisionError:
    print("cero")
except:
    print("algo") 

x = '\''
print(len(x))


print('Mike' > 'Mikey')


print(float("1, 3"))
