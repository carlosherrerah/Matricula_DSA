package u1;

public class Maestro extends Persona {
    String titulo;
    double salario;

    public Maestro(String nombre, int edad, String titulo, double salario) {
        super(nombre, edad);
        this.titulo = titulo;
        this.salario = salario;
        System.out.println("Estamos en el maestro");
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        String a = super.toString();
        return a + " : " + "Maestro [titulo=" + titulo + ", salario=" + salario + "]";
    }

    public static void main(String[] args) {
        Maestro m1 = new Maestro("Pepito", 20, "Pobresor", 123.50);

        System.out.println(m1);
        System.out.println(m1.getNombre());
        m1.setTitulo("Chistemas");
        System.out.println(m1);

        Maestro[] m = new Maestro[2];
        m[0] = new Maestro("Pepito", 20, "Pobresor", 123.45);

    }

}
