package pilitasB;

public class TestPila {
    public static void main(String[] args) {
        Nodo reg = new Nodo();
        Pila duracell = new Pila();
        System.out.println(duracell);

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
    

    }

    
}
