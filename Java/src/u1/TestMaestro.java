package u1;

public class TestMaestro {
    public static void main(String[] args) {
        Persona a = new Persona();
        a.id = 1;
        a.nombre="Pepito";
        System.out.println(a.nombre);
        a.setEdad(40);
        System.out.println(a.getEdad());

    }
    
}
