package u2.pilitasA;

public class TestPila {
    public static void main(String[] args) {
        Nodo reg = new Nodo();

        Pila duracell = new Pila(5);
        Pila rayoback = new Pila(10);
        
        Pila[] energizer = new Pila[5];

        System.out.println(duracell.isEmpty());

        reg.id = 32;
        reg.setNombre("Zac");
        duracell.push(reg);
        System.out.println(duracell.isEmpty());

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
        System.out.println(duracell.size());

        System.out.println(duracell.isExist("Ags"));

        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());

        /*
        reg.setId(2);
        reg.setNombre("BC");
        duracell.push(reg);

        duracell.push(15 , "DF");
        duracell.push(1, "Ags");
        */

    }
    
}
