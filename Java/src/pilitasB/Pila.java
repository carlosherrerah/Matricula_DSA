package pilitasB;

public class Pila {
    Nodo top = null;
    int max = 0;
    int size = 0;

    public Pila(int max) {
        this.max = max;
    }

    public void push(String id, String nombre, int cuatri) {
        if (size()<max) {
        Nodo nuevo = new Nodo(id, nombre, cuatri);
        nuevo.sig = top;
        top = nuevo;
        size++;
        }
    }

    public void push(Nodo reg) {
        if (max == 0 ){
            Nodo nuevo = new Nodo(reg);
            nuevo.sig = top;
            top = nuevo;
        } else {
            while (max > size){
                Nodo nuevo = new Nodo(reg);
                nuevo.sig = top;
                top = nuevo;
                size++;
            }
            System.out.println("No se pueden añadir más nodos");
            }    
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

    public boolean isEmpty() {
        boolean r = false;
        if (top == null) {
            r = true;
        }
        return r;
    }

    public Nodo pop() {
        Nodo actual = null;
        if ( !isEmpty()) {
            actual = top;
            top = top.sig;
            actual.sig = null;
            size--;
        }
        return actual;
    }
    
}
