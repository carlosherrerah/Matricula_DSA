public class Prueba {

    static int doble(int a) {
        return a * 2;
    }

    int duplicado(int a) {
        return a * 2;
    }

    public static void main(String[] args) {
        System.out.println("hola mundo");
        int r = Prueba.doble(3);
        System.out.println(r);

        Prueba a = new Prueba();
        Prueba b = new Prueba();

        System.out.println(a.duplicado(4));
        doble(5);
    }
}
