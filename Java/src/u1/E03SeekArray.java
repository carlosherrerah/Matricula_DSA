package u1;
public class E03SeekArray {
    public static void main(String[] args) {
        int datos[] = { 5, 10, 15, 17, 20 };
        int pos = -1;
        int num = 15;

        // Arreglo desordenado
        for (int i = 0; i < datos.length; i++) {
            if (num == datos[i]) {
                pos = i;
                break;
            }
        }
        System.out.println("Posicion Desordenado: " + pos);

        // Arreglo Ordenado
        int i = 0; 
        pos = -1;
        num = 200;
        while (i <= datos.length-1  && datos[i]<=num) {
            if (num == datos[i]){
                pos = i;
                break;
            }
            i = i + 1;
        }
        System.out.println("Posicion Ordenado: " + pos);
    }

}
