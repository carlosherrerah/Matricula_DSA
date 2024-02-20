package pilitasA;

public class TestPila {
    public static void main(String[] args) {
        Nodo reg = new Nodo();

        Pila duracell = new Pila();

        System.out.println(duracell);

        reg.id = 32;
        reg.setNombre("Zac");
        duracell.push(reg);
        System.out.println(duracell);

        reg.id = 1;
        reg.setNombre("Ags");
        duracell.push(reg);
        System.out.println(duracell);

        reg.id = 15;
        reg.setNombre("DF");
        duracell.push(reg);
        System.out.println(duracell);
        System.out.println("hola" + duracell.top.sig.sig.nombre);

        System.out.println(duracell.top.nombre);
        System.out.println(duracell.top.sig.nombre);

        System.out.println("--- Paso de la muerte ---");
        duracell.show();

        /*
        reg.setId(2);
        reg.setNombre("BC");
        duracell.push(reg);

        duracell.push(15 , "DF");
        duracell.push(1, "Ags");
        */

    }
    
}
