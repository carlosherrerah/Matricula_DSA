from tkinter import *
from tkinter import messagebox

# Variables Globales
Botones= []

tablero = [['1','2','3'],
           ['4','X','6'],
           ['7','8','9'],
           ['Fin','','']]

def pantalla():
    Boton1 = Button(ventana, width=9, height=3,  command=lambda: comenzar(1))
    Boton2 = Button(ventana, width=9, height=3,  command=lambda: comenzar(2))
    Boton3 = Button(ventana, width=9, height=3,  command=lambda: comenzar(3))
    Boton4 = Button(ventana, width=9, height=3,  command=lambda: comenzar(4))
    Boton5 = Button(ventana, width=9, height=3,  command=lambda: comenzar(5))
    Boton6 = Button(ventana, width=9, height=3,  command=lambda: comenzar(6))
    Boton7 = Button(ventana, width=9, height=3,  command=lambda: comenzar(7))
    Boton8 = Button(ventana, width=9, height=3,  command=lambda: comenzar(8))
    Boton9 = Button(ventana, width=9, height=3,  command=lambda: comenzar(9))
    BotonF = Button(ventana, width=9, height=3,  command=lambda: finalizar())

    Botones.append(Boton1)
    Botones.append(Boton2)
    Botones.append(Boton3)
    Botones.append(Boton4)
    Botones.append(Boton5)
    Botones.append(Boton6)
    Botones.append(Boton7)
    Botones.append(Boton8)
    Botones.append(Boton9)
    Botones.append(BotonF)

    for i in range(10):
        f = i // 3
        c = i  % 3
        Lx = 150   # Longitud entre esquina esquina de cada cuadro
        Ly = 100   # Longitud entre esquina esquina de cada cuadro
        print(i,f,c, tablero[f][c])

        Botones[i].config(text=tablero[f][c])
        Botones[i].place(x=Lx*c+60, y=Ly*f+50)   # x,y 60,50 Punto de origen

def comenzar(i):
    f = (i-1) // 3
    c = (i-1)  % 3
    print(i, f , c, tablero[f][c])
    tablero[f][c]= '.' + tablero[f][c] + '.'
    Botones[i-1].config(text=tablero[f][c])

def finalizar():
    print(". . . H e c h o")
    quit()

# -----------------------------------------------------------------------------
# main 
ventana = Tk()
ventana.title("Juego del gato")
ventana.geometry("500x400")   # x,y
pantalla()

ventana.mainloop()
