package u2.pilitasB;

public class TestPila {
    public static void main(String[] args) {
        Nodo reg = new Nodo();
        Pila duracell = new Pila(10);
        Pila energizer[] = new Pila[5];
        //Pila rayoback = new Pila();

        System.out.println(duracell);
        duracell.pop();

        reg.matricula = "up1";
        reg.setNombre("pepito");
        reg.setCuatrimestre(1);
        duracell.push(reg);
        System.out.println(duracell);

        duracell.push("up02", "Mafalda", 2);
        System.out.println(duracell);

        reg.matricula = "up3";
        reg.setNombre("pablito");
        reg.setCuatrimestre(1);
        duracell.push(reg);
        System.out.println(duracell);

        System.out.println("---------->");
        //System.out.println(duracell.top.sig.sig.nombre);
        duracell.show();
        System.out.println(duracell.size());
    
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
        System.out.println(duracell.pop());
    }

    
}
