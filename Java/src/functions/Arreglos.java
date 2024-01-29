package functions;

public class Arreglos {

    public static void imprimirArreglo(int[] v) {
        for (int i : v) {
            System.out.print(i + "\t");
        }
        System.out.println();
    }

    public static void imprimirArreglo(String[] v) {
        for (String i : v) {
            System.out.print(i + "\t");
        }
        System.out.println();
    }

    public static <T> void imprimirArregloT(T[] v) {
        for (T i : v) {
            System.out.print(i + "\t");
        }
        System.out.println();
    }

    public static void imprimirMatriz(int[][] m) {
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[0].length; j++) {
                System.out.print(m[i][j] + "\t");
            }
            System.out.println("");
        }
    }

    public static <T> int seekArrayDesordered(T[] arreglo, T dato) {
        // Arreglo desordenado
        int posicion = 0;
        for (T elemento : arreglo) {
            if (elemento.equals(dato)) {
                return posicion; // Devuelve la posición si encuentra el dato
            }
            posicion++;
        }
        return -1; // Devuelve -1 si el dato no se encuentra en el arreglo
    }

    public static int seekArrayOrdered(int[] datos, int num) {
        // Arreglo Ordenado
        int pos = -1, i = 0;
        while (i <= datos.length - 1 && datos[i] <= num) {
            if (num == datos[i]) {
                pos = i;
                break;
            }
            i = i + 1;
        }
        return pos;
    }

}
