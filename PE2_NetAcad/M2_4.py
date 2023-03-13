# Seccion 4. Cadenas en accion
# string == number es siempre False (falso).
# string != number es siempre True (verdadero).
# string >= number siempre genera una excepción.

print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print('alpha' < 'alphabet')
print('Beta' < 'beta')
print('20' < '8')    # lo ve como ascii
print('10' == 10)    # Es falso
# print('10' > 10)     # TypeError: '>'  str vs int

# Demostración de la función sorted()  y metodo .sort():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek = sorted(first_greek)
first_greek = sorted(first_greek, reverse=True)  # genera una nueva lista
first_greek.sort(reverse=True)                   # modifica la lista
print(first_greek)

# Conversiones str, int, float
print(str(int('10')+float('1.1')) + " final")

s1 = '12.8'
# i = int(s1)    # ValueError
i = float(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

# LAB un Display LED 5X3
# /Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos


num = [['###', ' # ', '###', '###', '# #', '###', '###', '###', '###', '###'],
       ['# #', ' # ', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #'],
       ['# #', ' # ', '###', '###', '###', '###', '###', '  #', '###', '###'],
       ['# #', ' # ', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #'],
       ['###', ' # ', '###', '###', '  #', '###', '###', '  #', '###', '###']]

n = int(input("Numero: "))
N = str(n)

for i in range(0, 5):
    for j in N:
        print(num[i][int(j)], end=' ')
    print()


# -------------------------------------------------------------------------
digits = ['1111110',  # 0
          '0110000',  # 1
          '1101101',  # 2
          '1111001',  # 3
          '0110011',  # 4
          '1011011',  # 5
          '1011111',  # 6
          '1110000',  # 7
          '1111111',  # 8
          '1111011',  # 9
          ]

def print_number(num):
    global digits
    digs = str(num)
    lines = ['' for lin in range(5)]
    for d in digs:
        segs = [[' ', ' ', ' '] for lin in range(5)]
        ptrn = digits[ord(d) - ord('0')]
        if ptrn[0] == '1':  #a
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1':  #b
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1':  #c
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1':  #d
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1':  #e
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1':  #f 
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1':  #g
            segs[2][0] = segs[2][1] = segs[2][2] = '#'

        for lin in range(5):
            lines[lin] += ''.join(segs[lin]) + ' '

    for lin in lines:
        print(lin)

print_number(int(input("Ingresa el número que deseas mostrar: ")))
