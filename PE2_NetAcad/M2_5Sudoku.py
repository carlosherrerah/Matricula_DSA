# Una función que verifica si una lista pasada como argumento contiene
# nueve dígitos del '1' al '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Una lista de filas que representan el Sudoku.
rows = [ ] 
rows.append('195743862')
rows.append('431865927')
rows.append('876192543')
rows.append('387459216')
rows.append('612387495')
rows.append('549216738')
rows.append('763524189')
rows.append('928671354')
rows.append('254938671')


'''
for r in range(9):
    ok = False
    while not ok: 
        row = input("Ingresa fila #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Datos de fila incorrectos: se requieren 9 dígitos")
    rows.append(row)
'''
ok = True

# Comprobar si todas las filas son correctas.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Comprobar si todas las columnas son correctas.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Comprobar si todos los subcuadrados (3x3) son correctos.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Hacer una cadena que contenga todos los dígitos de un subcuadrado.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Imprimir el veredicto final.
if ok:
    print("Si")
else:
    print("No")
    