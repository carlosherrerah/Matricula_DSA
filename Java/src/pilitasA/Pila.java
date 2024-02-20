package pilitasA;

public class Pila {
    Nodo top = null;

     @Override 
    public String toString() {
        return "Pila [top=" + top + "]";
    }
     

    public void push(int id, String nombre){
        Nodo nuevo = new Nodo(id, nombre);
        nuevo.sig = top;
        top = nuevo;
    }
    public void push(Nodo reg) {
        Nodo nuevo = new Nodo(reg);
        nuevo.sig = top;
        top = nuevo;

    }

    public void show(){ 
        Nodo actual = top;
        while ( actual != null){
            System.out.println(actual.id + "\t" + actual.getNombre());
            // actual = actual.sig;
            top =top.sig;
        }
        System.out.println("");
    }
    
}
