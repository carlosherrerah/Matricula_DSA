package u3.ventanas;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VentanaJPanel {
    public static void main(String[] args) {
        // Crear y mostrar la interfaz gráfica en el hilo de despacho de eventos de Swing
        SwingUtilities.invokeLater(() -> {
            crearInterfazGrafica();
        });
    }

    public static void crearInterfazGrafica() {
        // Crear el marco (ventana principal)
        JFrame marco = new JFrame("Ejemplo de JPanel");

        // Establecer el tamaño del marco
        marco.setSize(300, 200);

        // Establecer la operación de cierre del marco
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear un panel
        JPanel panel = new JPanel();

        // Crear un botón
        JButton boton = new JButton("Haz clic");

        // Agregar un ActionListener al botón para manejar eventos de clic
        boton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Acción a realizar cuando se hace clic en el botón
                System.out.println("¡Se hizo clic en el botón!");
            }
        });

        // Agregar el botón al panel
        panel.add(boton);

        // Agregar el panel al marco
        marco.add(panel);

        // Hacer visible el marco
        marco.setVisible(true);
    }
}
