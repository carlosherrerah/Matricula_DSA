package u3.ventanas;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class VentanaJFrame {
    public static void main(String[] args) {
        // Crear un nuevo marco (ventana)
        JFrame marco = new JFrame("Ejemplo de Swing");

        // Establecer el tamaño de la ventana
        marco.setSize(300, 200);

        // Establecer el cierre de la ventana
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear un botón
        JButton boton = new JButton("Haz clic");

        // Agregar un evento de clic al botón
        boton.addActionListener(e -> {
            // Mostrar un mensaje cuando se hace clic en el botón
            JOptionPane.showMessageDialog(marco, "¡Has hecho clic en el botón!");
        });

        // Agregar el botón al marco
        marco.add(boton);

        // Establecer la visibilidad del marco
        marco.setVisible(true);
    }
}
