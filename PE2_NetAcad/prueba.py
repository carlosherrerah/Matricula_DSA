#           0   1   2   3   4   5   6
valores = "Lun Mar Mie Jue Vie Sab Dom"
valor = valores.split()
day = "Mar"
if day in valor:
    # print(valor.index(day))
    pos = valor.index(day)
    add = 15
    sub = 23
    vueltas = (pos-sub) // 7
    porcion = (pos-sub) % 7
    print(vueltas, porcion)




