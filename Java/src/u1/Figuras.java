package u1;

import java.text.DecimalFormat;

class Figura{
    public int[] position = new int[2];

    Figura() {
        position[0] = 0;
        position[1] = 0;
    }

    Figura(int[] position) {
        setPosition(position);
    }

    public int[] getPosition() {
        return position;
    }

    public void setPosition(int[] position) {
        this.position[0] = position[0];
        this.position[1] = position[1];
    }

}

class Circulo extends Figura{
    double radio;

    Circulo(double radio, int[] position) {
        // super(position);
        setPosition(position); // Herencia  
        setRadio(radio);
    }

    public void setRadio(double radio) {
        this.radio = radio;
    }

    public double area() {
        return Math.PI*Math.pow(radio, 2);
    }    

}

class Rectangulo extends Figura{
    double base;
    double altura;

    Rectangulo(double b, double a, int[] position) {
        //super(position);
        setPosition(position);   // Herencia
        setLados(b, a);
    }

    public void setLados(double b, double a) {
        this.base = b;
        this.altura = a;
    }

    public double area() {
        return base*altura;
    }    

}

public class Figuras {
    public static void main(String[] args) {
        int[] position = {10,20};
        double r = 5;
        DecimalFormat decimal = new DecimalFormat("0.00");

        Circulo    circulo1   = new Circulo(r, position);
        Rectangulo rectangulo = new Rectangulo(5,4, position);

        System.out.println(decimal.format(circulo1.area()));   // Polimorfismo
        System.out.println(decimal.format(rectangulo.area()));
 
        Figura circulo2 = new Circulo(2, position);  
        
        Circulo circulo3;
        circulo3 = (Circulo) circulo2;
        System.out.println("AREA: " + circulo3.area());

        // Circulo circulo4 = (Circulo) new Figura(position);  // Error

        position = circulo2.getPosition();
        System.out.println("position "+position[0]+","+ circulo2.getPosition()[1]);
    }

}

