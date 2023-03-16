
import numpy as np

class Carta:
    def __init__(self, cara, palo):
        self.cara = cara
        self.palo = palo

    def __str__(self) -> str:
        return str(self.cara) + "-" + self.palo
    
    def prueba():
        pass
    
caras = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ["C", "E", "O", "B"];  # Corazones, Espadas, Oros, Bastos 

ncaras = len(caras)
npalos = len(palos)
ncartas = ncaras * npalos
print(ncartas)

mazo = []
mazo.insert(0, Carta(1, "C") )
mazo.append(Carta(2, "B"))
print(mazo[1])

mazos = []
mazos.append([])
mazos[0].append(Carta(3, "C"))
print(mazos[0][0])

masos= np.zeros((3,40),dtype = Carta)
masos[1][39]= Carta(12, "B")
