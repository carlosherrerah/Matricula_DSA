package functions;

public class Matematicas {

    public static int factorial(int n) {
        int total = 1;
        for (int i = 1; i < n; i++) {
            total = total * i;
        }
        return total;
    }

    public static int max(int a, int b) {
        int mayor = (a > b) ? a : b;  // If ternario
        return mayor;
    }

    public static int maxA(int[] datos) {
        int mayor = datos[0];
        for (int elemento : datos) {   // for mejorado
            if (elemento > mayor) {
                mayor = elemento;
            }
        }
        return mayor;
    }

    public static int max(int... v) {
        int mayor = v[0];
        for (int i = 0; i < v.length; i++) {
            if (v[i] > mayor) {
                mayor = v[i];
            }
        }
        return mayor;
    }

    public static void main(String[] args) {
    //     int a = 5;
    //     int b = 7;
    //     int[] c = { 5, 8, 3 };
    //     int r = max(a, b);
    //     System.out.println(r);
    //     System.out.println(maxA(c));
        System.out.println(max(7, 4, 3, 9, 2));
        
     }

}
