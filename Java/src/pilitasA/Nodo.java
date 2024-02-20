package pilitasA;

public class Nodo {
    int id;
    String nombre;
    Nodo sig; // Linea de oro

    public Nodo() {
    }

    public Nodo(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
        this.sig = null;
    }

    public Nodo(Nodo reg) {
        this.id = reg.id;
        this.nombre = reg.nombre;
        this.sig = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Nodo getSig() {
        return sig;
    }

    public void setSig(Nodo sig) {
        this.sig = sig;
    }
/*

    @Override
    public String toString() {
        return "Nodo [id=" + id + ", nombre=" + nombre + ", sig=" + sig + "]";
    }
*/
    

}
