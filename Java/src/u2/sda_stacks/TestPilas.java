package u2.sda_stacks;

public class TestPilas {

   public static void main(String[] args) {
      Pilas p1 = new Pilas();

      Nodo reg =   new Nodo();
      reg.setId(32);
      reg.setAbr("Zac");

      p1.push(reg);

      reg.setId(1);
      reg.setAbr("Ags");
      p1.push(reg);

      p1.push(10, "BC");
      p1.push(15, "DF");
      p1.push(20, "Ver");
      p1.showStack();      
      /*		
		Pilas[] p = new Pilas[2];
		p[0] = new Pilas();
		p[1] = new Pilas(5);

		Nodo reg =   new Nodo();

		reg= new Nodo();
		reg.setId(1);
		reg.setAbr("Ags");
		p[0].push(reg);

//		reg = new Nodo(32, "Zac"); 
		reg.setId(32);
		reg.setAbr("Zac");
		p[0].push(reg);
       */


      //p1.showStack();
      
      System.out.println(p1.pop().id);
      System.out.println(p1.pop().id);
      System.out.println(p1.pop());
      System.out.println(p1.pop());
      System.out.println(p1.pop());
      System.out.println(p1.pop());
      System.out.println("------");
      p1.showStack();  
      System.out.println(". . . Hecho");

   }

}
