package u1.cartas;

class CartaE{

    public static enum Cara{ As, Dos, Tres, Cuatro, Cinco, Seis, Siete, Ocho, Nueve, Diez, Joto, Quina, Rey};
    public static enum Palo{ Bastos, Diamantes, Corazones, Espadas};
    
    private Cara cara;
    private Palo palo;
    

    public CartaE(Cara cara, Palo palo) {
        this.cara = cara;
        this.palo = palo;
    }
    
    public Cara getCara() {
        return cara;
    }
    public void setCara(Cara cara) {
        this.cara = cara;
    }
    public Palo getPalo() {
        return palo;
    }
    public void setPalo(Palo palo) {
        this.palo = palo;
    }

    @Override
    public String toString() {
        return "Carta [cara=" + cara + ", palo=" + palo + "]";
    }
  
  
/*     public String toString(){
        return String.format(" %s de %s", cara, palo);
    }
 */
}
