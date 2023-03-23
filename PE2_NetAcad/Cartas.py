
import numpy as np
import os

os.system("cls")
class Carta:
    def __init__(self, cara, palo):
        self.cara = cara
        self.palo = palo

    def __str__(self) -> str:
        return str(self.cara) + "-" + self.palo
    
caras = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ["C", "E", "B", "O"];  # Corazones, Espadas, Bastos, Oros 

ncaras = len(caras)
npalos = len(palos)
ncartas = ncaras * npalos
print("No. de Cartas: ", ncartas)

mazo1 = []
mazo2 = []
#mazo1.insert(0, Carta(1, "C") )
#mazo1.append(Carta(2, "B"))
#print(mazo1[1])

mazos = []
mazos.append([])
mazos.append([])
#mazos[0].append(Carta(3, "C"))
#mazos[1].append(Carta(3, "C"))
#print(mazos[0][0])           # Jugador 1, carta 1

masos= np.zeros((2,40), dtype = Carta)
masos[1][39]= Carta(12, "B")  # Jugador 2, carta 39

print("P c     \t p C")
for i in range(ncartas):
    palo1 = i //  ncaras  # Palo sort
    cara1 = i %   ncaras  # cara NO sort

    palo2 = i %   npalos  # palo NO sort
    cara2 = i //  npalos  # Cara sort

    mazo1.append(Carta(caras[cara1], palos[palo1]))
    mazo2.append(Carta(caras[cara2], palos[palo2]))

    mazos[0].append(Carta(caras[cara1], palos[palo1]))
    mazos[1].append(Carta(caras[cara2], palos[palo2]))
    
    print(palo1, cara1, mazo1[i], '\t', palo2, cara2, mazo2[i] )

