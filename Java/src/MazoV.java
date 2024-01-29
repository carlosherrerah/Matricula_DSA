public class MazoV {
    CartaV[] mazo = new CartaV[52];

    public MazoV() {
        String cara[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
        String palo[] = { "Trebol", "Picas", "Diamante", "Corazon" };
        int nCaras = cara.length;
        // Ordenado por Palos
        for (int i = 0; i < cara.length * palo.length; i++) {
            mazo[i] = new CartaV(cara[i % 13], palo[ i / nCaras]);
        }
    }

    public void imprimirCartas() {
        /*
         * for (Carta carta : mazo) {
         * System.out.println(carta);
         * }
         */
        for (int i = 0; i < mazo.length; i++) {
            System.out.println(i + 1 + ":" + mazo[i]);
            //System.out.println(i+1 + ": " + mazo[i].getCara() + " de " + mazo[i].palo);
        }
    }

    public static void main(String[] args) {
        MazoV mazo = new MazoV();
        mazo.imprimirCartas();

        MazoV[] mazos = new MazoV[2];
        mazos[0] = new MazoV();
        mazos[0].imprimirCartas();
    }

}
