package u2;

enum Cara{ Cero, As, Dos, Tres, Cuatro, Cinco, Seis, Siete, Ocho, Nueve, Diez, Joto, Quina, Rey};

public class Enum {
    public static void main(String[] args) {
        int num = 3;
        Cara cara;

        cara = Cara.values()[num];
        System.out.println(cara);
        System.out.println("El número " + num + " corresponde a enum: " + cara);

        cara = Cara.Cuatro;
        num = cara.ordinal();
        System.out.println("El enum " + cara + " corresponde a número: " + num);
    }
    
}
