package u1.cartas;


import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class MazoE {
    //List<CartaE> lista = new ArrayList<>();
    List<CartaE> lista;
    CartaE[] mazo = new CartaE[52];
    int[] a = new int[12];

    public MazoE() {

        int cuenta = 0;

        for (CartaE.Palo palo : CartaE.Palo.values()) {
            for (CartaE.Cara cara : CartaE.Cara.values()) {
                mazo[cuenta] = new CartaE(cara, palo);
                //lista.add(mazo[cuenta]);
                //System.out.println(mazo[cuenta]);
                cuenta++;
            }
        }
        lista = Arrays.asList(mazo);    // obtiene objeto List
        Collections.shuffle(lista);     // barajea el mazo

    }

    public void imprimirCartas() {
        for (int i = 0; i < 52; i++) {
            System.out.println(i + ": " + lista.get(i));
            //System.out.println(i + ": " + mazo[i]);
        }
    }

    public static void main(String[] args) {
        MazoE mazo = new MazoE();
        mazo.imprimirCartas();

        MazoE[] mazos = new MazoE[2];
        mazos[0] = new MazoE();
        //mazos[0].imprimirCartas();

    }
}
