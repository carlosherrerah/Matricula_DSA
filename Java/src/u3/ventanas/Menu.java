package u3.ventanas;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

public class Menu {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Ejemplo de Menú");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear la barra de menú
        JMenuBar menuBar = new JMenuBar();

        // Crear los menús
        JMenu fileMenu = new JMenu("Archivo");
        JMenu editMenu = new JMenu("Editar");
        JMenu helpMenu = new JMenu("Ayuda");

        // Crear los elementos de los menús
        JMenuItem newMenuItem = new JMenuItem("Nuevo");
        JMenuItem openMenuItem = new JMenuItem("Abrir");
        JMenuItem saveMenuItem = new JMenuItem("Guardar");
        JMenuItem exitMenuItem = new JMenuItem("Salir");

        JMenuItem cutMenuItem = new JMenuItem("Cortar");
        JMenuItem copyMenuItem = new JMenuItem("Copiar");
        JMenuItem pasteMenuItem = new JMenuItem("Pegar");

        JMenuItem aboutMenuItem = new JMenuItem("Acerca de");

        // Agregar funcionalidad al elemento "Salir" del menú "Archivo"
        exitMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int option = JOptionPane.showConfirmDialog(frame, "¿Está seguro de que desea salir?", "Salir",
                        JOptionPane.YES_NO_OPTION);
                if (option == JOptionPane.YES_OPTION) {
                    System.exit(0); // Cerrar el programa
                }
            }
        });

        /*
         * // Agregar funcionalidad al elemento "Abrir" del menú "Archivo" para llamar a
         * otro programa Java
         * openMenuItem.addActionListener(new ActionListener() {
         * 
         * @Override
         * public void actionPerformed(ActionEvent e) {
         * try {
         * // Ruta al directorio donde se encuentra el programa a ejecutar
         * //String directory = "ruta/del/otro/programa";
         * String directory = "src/pilitasA";
         * // Nombre del archivo del programa a ejecutar
         * String fileName = "Hola.java";
         * 
         * // Construir el proceso para ejecutar el programa externo
         * ProcessBuilder builder = new ProcessBuilder("javac", fileName);
         * builder.directory(new File(directory));
         * Process process = builder.start();
         * 
         * // Esperar a que el proceso termine
         * process.waitFor();
         * 
         * // Si el proceso termina correctamente, se ejecuta el programa
         * if (process.exitValue() == 0) {
         * builder.command("java", "Hola");
         * process = builder.start();
         * } else {
         * JOptionPane.showMessageDialog(frame, "Error al compilar el programa.",
         * "Error", JOptionPane.ERROR_MESSAGE);
         * }
         * } catch (IOException | InterruptedException ex) {
         * ex.printStackTrace();
         * }
         * }
         * });
         */

        /*
         * // Agregar funcionalidad al elemento "Abrir" del menú "Archivo"
         * openMenuItem.addActionListener(new ActionListener() {
         * 
         * @SuppressWarnings("deprecation")
         * 
         * @Override
         * public void actionPerformed(ActionEvent e) {
         * try {
         * // Aquí debes reemplazar "Ruta/Al/OtroPrograma.java" por la ruta al programa
         * Java que deseas ejecutar
         * // Puedes usar el método exec() de Runtime para ejecutar el programa
         * Runtime.getRuntime().exec("java -cp src/OtroPrograma.jar NombreDelPrograma");
         * } catch (IOException ex) {
         * ex.printStackTrace();
         * }
         * }
         * });
         */

        
        // Agregar funcionalidad al elemento "Abrir" del menú "Archivo"
        openMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Llamar al método main() del otro programa
                VentanaJFrame.main(new String[] {});
            }
        });


        // Agregar los elementos a los menús
        fileMenu.add(newMenuItem);
        fileMenu.add(openMenuItem);
        fileMenu.add(saveMenuItem);
        fileMenu.addSeparator(); // Separador entre elementos
        fileMenu.add(exitMenuItem);

        editMenu.add(cutMenuItem);
        editMenu.add(copyMenuItem);
        editMenu.add(pasteMenuItem);

        helpMenu.add(aboutMenuItem);

        // Agregar los menús a la barra de menú
        menuBar.add(fileMenu);
        menuBar.add(editMenu);
        menuBar.add(helpMenu);

        // Agregar la barra de menú al frame
        frame.setJMenuBar(menuBar);

        frame.setVisible(true);
    }
}
