package u1;
import functions.Arreglos;
import functions.Matematicas;


public class E04TestArreglos {
    public static void main(String[] args) {
        Integer[] v = {6,3 ,5, 7};
        String[] vs = {"hola", "Mundo", "Cruel"};

        int[][] m = {
            {5,2,8,9},
            {1,9,6,10},
            {8, 5, 4, 3}
        };
        System.out.println(v.length);
        //System.out.println("Arreglo: ");
        //Arreglos.imprimirArreglo(v);

        System.out.println("ArregloT: ");
        Arreglos.imprimirArregloT(vs);

        System.out.println("Matriz: ");
        Arreglos.imprimirMatriz(m);

        System.out.println(Arreglos.seekArrayDesordered(v, 5));
    }
}
