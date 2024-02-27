package _personal.sda_stacks;

public class Nodo {

   int id;
   String abr;
   Nodo sig;

   public Nodo() {
      this.id = 0;
      this.abr = "";
      this.sig = null;
   }

   public Nodo(int id, String abr) {
      this.id = id;
      this.abr = abr;
      this.sig = null;
   }

   public Nodo(Nodo reg) {
      this.id = reg.id;
      this.abr = reg.abr;
      this.sig = null;
   }

   public int getId() {
      return id;
   }

   public void setId(int id) {
      this.id = id;
   }

   public String getAbr() {
      return abr;
   }

   public void setAbr(String abr) {
      this.abr = abr;
   }

   @Override
   public String toString() {
      return "Nodo [id=" + id + ", abr=" + abr + ", sig=" + sig + "]";
   }

/*   
   @Override
   public String toString() {
      return "Nodo [id=" + id + ", abr=" + abr + ", sig=" + sig + "]";
   }
*/

}
