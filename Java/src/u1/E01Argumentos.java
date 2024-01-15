package u1;

public class E01Argumentos {
    public static void main(String[] hola) {

        for (int i = 0; i < hola.length; i++) {
            System.out.println(hola[i]);
            for (int j = 1; j <= 10; j++) {
                System.out.println(Integer.parseInt(hola[i]) * j);
            }
            System.out.println("");
        }
    }
}

		
