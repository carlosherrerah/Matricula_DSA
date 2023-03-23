from tkinter import *
from tkinter import messagebox

def comenzar(i):
    # f = (i-1) // 3
    #c = (i-1)  % 3
    print("Valor:",i)
    #print(listaBotones[5].config())
    
    # listaBotones[i-1].place(x=150, y=250)
    # listaBotones[i-1].config(text=tablero[f][c])
    #listaBotones[i].config(state="anable")

ventana = Tk()
ventana.title("Juego del gato")
ventana.geometry("500x400")   # x,y

Botones= []

tablero = [['1','2','3'],
           ['4','5','6'],
           ['7','8','9']]

Boton1 = Button(ventana, width=9, height=3,  command=lambda: comenzar(1))
Boton2 = Button(ventana, width=9, height=3,  command=lambda: comenzar(2))
Boton3 = Button(ventana, width=9, height=3,  command=lambda: comenzar(3))
Boton4 = Button(ventana, width=9, height=3,  command=lambda: comenzar(4))
Boton5 = Button(ventana, width=9, height=3,  command=lambda: comenzar(5))
Boton6 = Button(ventana, width=9, height=3,  command=lambda: comenzar(6))
Boton7 = Button(ventana, width=9, height=3,  command=lambda: comenzar(7))
Boton8 = Button(ventana, width=9, height=3,  command=lambda: comenzar(8))
Boton9 = Button(ventana, width=9, height=3,  command=lambda: comenzar(9))

Botones.append(Boton1)
Botones.append(Boton2)
Botones.append(Boton3)
Botones.append(Boton4)
Botones.append(Boton5)
Botones.append(Boton6)
Botones.append(Boton7)
Botones.append(Boton8)
Botones.append(Boton9)
print(Botones)

for i in range(9):
    f = i // 3
    c = i  % 3
    Lx = 150   # Longitud entre esquina esquina de cada cuadro
    Ly = 100   # Longitud entre esquina esquina de cada cuadro
    print(i,f,c, tablero[f][c])

    Botones[i].config(text=tablero[f][c])
    Botones[i].place(x=Lx*f+60, y=Ly*c+50)

    #Boton1.place(x=Lx*f+60, y=Ly*c+50)    # x,y 60,50 Punto de origen
    #Boton2.place(x=Lx*f+60, y=Ly*c+50)    # x,y 60,50 Punto de origen


'''
for i in range(9):
    boton0 = Button(ventana, width=9, height=3, command=lambda: comenzar(0))
    boton0.place(x=50, y=50)
'''


ventana.mainloop()
