
public class CartaV {
    private String cara;  // 1,2,3..10, J,Q,K
            String palo;  // B, D, C, E

    public CartaV(String cara, String palo) {
        this.cara = cara;
        this.palo = palo;
    }

    public String getCara() {
        return cara;
    }

 
    public void setCara(String cara) {
        this.cara = cara;
    }

    public String getPalo() {
        return palo;
    }

    public void setPalo(String palo) {
        this.palo = palo;
    }

    @Override
    public String toString() {
        return "Carta [cara=" + cara + ", palo=" + palo + "]";
    }

/*
    public String toString(){
        return String.format(" %s de %s", cara, palo);
    }
*/

}
