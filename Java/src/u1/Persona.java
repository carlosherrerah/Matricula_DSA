package u1;

public class Persona {
    private String nombre;
    private  int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
        System.out.println("Estamos en la Persona");
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    @Override
    public String toString() {
        return "Persona [nombre=" + nombre + ", edad=" + edad + "]";
    }

    public static void main(String[] args) {
        int a = 1;
        int[] v = new int[3];

        Persona p1 = new Persona("Pepito", 20);
        Persona p2 = new Persona("Mafalda", 15);

        Persona[] p = new Persona[3];
        p[0] = new Persona("Jesus", 30);
        p[1] = new Persona("Maria", 20);
        p[2] = new Persona("Jose", 25);

        System.out.println(p1.nombre + " Edad: " + p1.edad);
        System.out.println(p2);
        System.out.println(p[1]);
        System.out.println(p[1].getNombre() + " Edad: " + p[1].edad);


    }

}
