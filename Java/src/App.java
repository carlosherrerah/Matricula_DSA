public class App {

    int doble(int a) {
        return a*2;
    }

    static  int duplicado(int a){
        return a*2;
    }

    public static void main(String[] args){
        System.out.println("Hello, World!");
        Operaciones.main(args);
        System.out.println(" Clase: " + duplicado(3));

        App a = new App();
        System.out.println("a -> "+ a.doble(4));

        App b = new App();
        System.out.println("b ->" +  b.doble(5));

        System.out.println(App.duplicado(6));
    }
    
}
