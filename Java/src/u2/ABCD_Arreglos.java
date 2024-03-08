package u2;

import functions.Arreglos;

public class ABCD_Arreglos {
    static int n;

    public static int deletePosition(int[] arr, int pos) {
        int r = arr[pos];
 
        for (int i = pos; i <= n - 2; i++) {
            arr[i] = arr[i + 1];
        }
        n = n - 1;
        arr[n] = 0;
        return r;
    }

    public static void main(String[] args) {
        int[] datos1 = new int[10];
        datos1[0] = 20;

        int[] datos = { 20, 15, 5, 8, 7, 0, 0, 0, 0, 0 };
        n = 5;
        
        int pos  =2; 

        Arreglos.imprimirArreglo(datos);
        
        int r = deletePosition(datos, pos);
        System.out.println("Elemento borrado: " + r);
        Arreglos.imprimirArreglo(datos);

    }

}
