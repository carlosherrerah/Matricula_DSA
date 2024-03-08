package u2;

enum Cafe {
    CHICO("Café Chico"),
    MEDIANO("Café mediano"),
    GRANDE("Café grande");

    Cafe(String tamano) {
        this.tamano = tamano;
    }

    String tamano = "";

    public String getTamano() {
        return tamano;
    }

    public static void main(String[] args) {
        Cafe cafe;
        cafe = Cafe.CHICO;
        System.out.println(cafe);

    }

}
