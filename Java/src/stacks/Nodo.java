package stacks;

public class Nodo {
    int id;
    String nombre;
    Nodo sig;

    public Nodo(int id, String nombre, Nodo sig) {
        this.id = id;
        this.nombre = nombre;
        this.sig = sig;
    }

    public Nodo( Nodo reg) {
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

    
    
}
