package pilitasB;

public class Pila {
    Nodo top = null;


    public void push(String id, String nombre, int cuatri) {
        Nodo nuevo = new Nodo(id, nombre, cuatri);
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
        while (actual != null) {
            System.out.println(actual.nombre);
            actual = actual.sig;   // linea de oro
        }
        System.out.println("");
    }

    public int size() {
        int n = 0;
        Nodo actual = top;
        while (actual != null) {
            actual = actual.sig;   // linea de oro
            n++;
        }
        return n;
    }

    public boolean isExist(String nombre) {
        boolean answer = false;
        Nodo actual = top;
        while (actual != null) {
            if (actual.getNombre() == nombre) {
                answer= true;
                break;
            }
            actual = actual.sig;
        }    
        return answer;
    }


    @Override
    public String toString() {
        return "Pila [top=" + top + "]";
    }
    
    
}
