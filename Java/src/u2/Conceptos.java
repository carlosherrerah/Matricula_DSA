package u2;

import java.util.*;
import java.util.stream.*;

public class Conceptos {
    enum Day { WEEK, WEEKEND }

    public static void main(String[] args)  {
        int value = 0;
        List<Integer> lista = Arrays.asList(7,3,9,10,5);
        
        Integer suma = lista.stream().filter(x -> x>6).reduce(0, (a,b) -> a + b);
        suma = lista.stream().reduce(0, Integer::sum);
        System.out.println(suma);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter ur age: ");
        try {
             value = scanner.nextInt();
             assert value >= 18 : " Eres menor de Edad";
        } catch (Exception e) {
            System.out.println("value is " + value);
        }        
   
        System.out.println(Day.WEEKEND);

    }

}

