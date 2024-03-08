package u2.pilitasA;

public class Pila {
    Nodo top = null;
    int max = 0;

    public Pila(int max){
        this.max = max;
    }


    @Override
    public String toString() {
        return "Pila [top=" + top + "]";
    }

    public void push(int id, String nombre) {
        Nodo nuevo = new Nodo(id, nombre);
        nuevo.sig = top;
        top = nuevo;
    }

    public void push(Nodo reg) {
        Nodo nuevo = new Nodo(reg);
        nuevo.sig = top;
        top = nuevo;

    }

    public Nodo pop() {
        Nodo actual = null;
        if (top != null) {
        // if (!isEmpty()) {
            actual = top;
            top = top.sig;
            // actual.sig = null;
        }
        return actual;
    }

    public void show() {
        Nodo actual = top;
        while (actual != null) {
            System.out.println(actual.id + "\t" + actual.getNombre());
            actual = actual.sig;
        }
        System.out.println("");
    }

    public boolean isEmpty() {
        boolean r = false;
        if (top == null)
            r = true;
        return r;
    }

    public int size() {
        int n = 0;
        Nodo actual = top;
        while (actual != null) {
            actual = actual.sig;
            n++;
        }
        return n;
    }

    public boolean isExist(String nombre) {
        boolean answer = false;
        Nodo actual = top;
        while (actual != null) {
            if (actual.getNombre() == nombre) {
                answer = true;
                break;
            }
            actual = actual.sig;
        }
        return answer;
    }

    public Nodo peek() {
        return top;
    }

}
