package _personal.sda_stacks;

public class Pilas {

   private Nodo p = null;
   private int n;	         // Si quisiera controlar el tamaño

   public Pilas() {
   }

   public Pilas(int tamano) {
      n = tamano;
   }

   public void push(Nodo reg) {
//     	Nodo nuevo = new Nodo();
      Nodo nuevo = new Nodo(reg);
      /*
    	nuevo.id  = reg.id;
    	nuevo.abr = reg.abr;
    	nuevo.sig = null;

    	nuevo.setId(reg.id);
    	nuevo.setAbr(reg.abr);
       */
      nuevo.sig = p;
      p = nuevo;
   }

   public void push(int id, String abr) {
      Nodo nuevo = new Nodo();
      /*
    	nuevo.id  = id;
    	nuevo.abr = abr;
    	nuevo.sig = null;
       */
      nuevo.setId(id);
      nuevo.setAbr(abr);

      nuevo.sig = p;
      p = nuevo;
   }

   public void showStack() {
      Nodo actual = p;
      while (actual != null) {
         System.out.println(actual.id + "\t" + actual.abr);
         actual = actual.sig;
      }
      System.out.println("");
   }

   public boolean isEmpty() {
      if (p == null) {
         return true;
      } else {
         return false;
      }
   }

   public Nodo pop() {
      Nodo actual = null;
      if (isEmpty()) {
         System.out.println("La pila no contiene elementos");
      } else {
         actual = p;
         p = p.sig;
         actual.sig =null; // Anular la referencia del nodo eliminado
      }
      return actual;
   }
}
