package pilitas;

public class Pila {
    Nodo top = null;


    public void push(String id, String nombre, int cuatri) {
        Nodo nuevo = new Nodo(id, nombre, cuatri);
        top = nuevo;
    }

    public void push(Nodo reg) {
        Nodo nuevo = new Nodo(reg);
        top = nuevo;
    }

    @Override
    public String toString() {
        return "Pila [top=" + top + "]";
    }
    
    
}
