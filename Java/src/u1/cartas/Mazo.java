package u1.cartas;
public class Mazo {
    Carta[] mazo = new Carta[52];

    public Mazo() {
        String cara[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
        String palo[] = { "Trebol", "Picas", "Diamante", "Corazon" };

        int nCaras = cara.length;
        int nPalos = palo.length;

        // Ordenado por Palos
        for (int i = 0; i < nCaras * nPalos; i++) {
            mazo[i] = new Carta(cara[i % nCaras], palo[i / nCaras]);
        }
    }

    public void imprimirCartas() {
      for (Carta carta : mazo) {
        //System.out.println(carta);
      }
      for (int i = 0; i < mazo.length; i++) {
        System.out.println(mazo[i]);
      }
    }

    public static void main(String[] args) {
        Mazo mazo = new Mazo();
        mazo.imprimirCartas();

    }

}
