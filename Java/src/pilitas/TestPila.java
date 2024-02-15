package pilitas;

public class TestPila {
    public static void main(String[] args) {
        Nodo reg = new Nodo();
        Pila duracell = new Pila();
        Pila energizer = new Pila();
       
        reg.matricula = "up1";
        reg.setNombre("pepito");
        reg.setCuatrimestre(1);
        duracell.push(reg);
        System.out.println(duracell);

        reg.matricula = "up2";
        reg.setNombre("pablito");
        reg.setCuatrimestre(1);
        duracell.push(reg);
        System.out.println(duracell);





        

    }

    
}
