package u1;
public class E02Estatico {

    static int doble(int a) {
        return a * 2;
    }

    int duplicado(int a) {
        return a * 2;
    }

    public static void main(String[] args) {
        System.out.println("hola mundo");
        int r = E02Estatico.doble(3);
        System.out.println(r);

        E02Estatico a = new E02Estatico();
        E02Estatico b = new E02Estatico();

        System.out.println(a.duplicado(4));
        doble(5);
    }
}
