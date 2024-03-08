package u2;

import java.util.*;

public class Colecciones {
    public static void main(String[] args) {
        int[] a = new int[100];    // OK

        // Flexible y buenas practicas, generico, programacion por interfaz
        List<String> names = new ArrayList<>();  // OK
        List<Integer> list = Arrays.asList(7,3,9,10,5);

        // No sincronizado, mas rapido, (un solo hilo)
        ArrayList<String> cars = new ArrayList<>();

        // Declaración de un vector (sincronizado y concurrente, multihilos)
        Vector<String> vector = new Vector<>();

        Queue<String> cola = new LinkedList<>();
        Stack<String> pila = new Stack<>(); // Linea de Oro

        // Declaración de un conjunto
        Set<Integer> conjunto = new HashSet<>();

        // Declaración de un mapa
        Map<String, Integer> mapa = new HashMap<>();

        // Declaración de una lista enlazada (doble)
        LinkedList<String> linkedList = new LinkedList<>();

        // Declaración de un conjunto ordenado
        TreeSet<String> treeSet = new TreeSet<>();

        // Declaración de un mapa ordenado
        TreeMap<String, Integer> treeMap = new TreeMap<>();

        // Declaración de una cola de prioridad
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();

        // Declaración de un conjunto sincronizado
        Set<String> synchronizedSet = Collections.synchronizedSet(new HashSet<>());

        // Declaración de una lista sincronizada
        List<String> synchronizedList = Collections.synchronizedList(new ArrayList<>());

        // -------------------------------------------------------------------------
        // Convert ArrayList to an array.
        String[] namesArray = names.toArray(new String[0]);
        // Convert an array to an ArrayList.
        List<String> namesList = Arrays.asList(namesArray);

        // Ejemplos
        List<Integer> lista = Arrays.asList(7,3,9,10,5);

        String expresion= "5 * ( 6 +  2 ) - 12 / 4";
        String[] expresion2 = expresion.split(" ");
        List<String> expresion3 = new ArrayList<>(Arrays.asList(expresion2));

        expresion3.add(0, "(");

        for (String element : expresion3) {
            System.out.print(element+ "\t");
        }
        System.out.println("");

        String n = "123";
        System.out.println(Integer.parseInt(n) + 1);
        pila.push("Jesus");
        pila.push("Maria");
        pila.push("Jose");
        pila.add(1, "Espiritu");

        boolean bandera = pila.contains("Maria");
        System.out.println(bandera);
        System.out.println("Contiene: " + pila.contains("Maria"));
        System.out.println("Pop: " + pila.pop());

        System.out.println("\nPila: ");
        pila.forEach(System.out::println);
        System.out.println("capacity: " + pila.capacity());
        System.out.println("size: " + pila.size());
        System.out.println("peek: " + pila.peek());

        names.add("Jesus");
        names.add("Maria");
        names.add("Jose");

        for (int i = 0; i < names.size(); i++) {
            System.out.println(i + ":" + names.get(i));
        }
        for (String element : names) {
            System.out.println(":" + element);
        }
        names.forEach(System.out::println);

        System.out.println("Arrays: ");
        for (String name : names) {
            System.out.println(name);
        }
        names.set(1, "Mary");
        // names.remove(0);
        String nombre = names.get(1);
        System.out.println(nombre);

        // Sort elements in natural order.
        System.out.println("Ordenacion1: ");
        Collections.sort(names);
        names.forEach(System.out::println);

        // Sort elements using a custom comparator.

        names.add("Yo");
        System.out.println("Ordenacion2: ");
        Collections.sort(names, new Comparator<String>() {
            public int compare(String a, String b) {
                return a.length() - b.length();
            }
        });
        names.forEach(System.out::println);
        /*
         * // Use the Stream API to filter elements.
         * List<String> filteredNames = names.stream().filter(name ->
         * name.startsWith("A")).collect(Collectors.toList());
         * // Compute sum of salaries of employee
         * int total = employees.stream()
         * .collect(Collectors.summingInt(Employee::getSalary)));
         */
    }
}
