package u2;

import java.util.EmptyStackException;
import java.util.Stack;

public class TryCatch {

    public static void main(String[] args) {
        Stack<String> pila = new Stack<>();
        int division;

        //division = 10 / 0;
        pila.pop();
        pila.add(2, "hola");   

        try { 
            division = 10 / 5;
        } catch (ArithmeticException e) {
            //System.out.println("no se puede dividir por cero");
            System.out.println(e.getMessage());
        } finally {  // Opcional
            System.out.println("Primer tryCath");
        }

        try {
            pila.pop();            
        } catch (NullPointerException e) {
            System.out.println("NullPointer: " + e.getMessage());
        } catch (EmptyStackException e) {
            System.out.println("EmptyStack: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("General: " + e.getMessage());
        }

    }
}