package u3.ventanas;

import java.awt.GridBagConstraints;
import java.awt.GridLayout;
import java.awt.Insets;

import javax.swing.Box;
import javax.swing.JButton;
import javax.swing.JFrame;


public class EjemploGridLayout {
    public static void main(String[] args) {
        // Crear un nuevo JFrame
        JFrame frame = new JFrame("Ejemplo de GridLayout");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(3, 2)); // 3 filas, 2 columnas
        
        frame.add(Box.createVerticalStrut(10));
        frame.add(Box.createHorizontalStrut(10)); // Cambia el valor según tus necesidades
        
        
        // Agregar botones al frame
        frame.add(new JButton("Botón 1"));
        frame.add(new JButton("Botón 2"));
        frame.add(new JButton("Botón 3"));
        frame.add(new JButton("Botón 4"));
        frame.add(new JButton("Botón 5"));
        frame.add(new JButton("Botón 6"));
        // Ajustar tamaño y mostrar la ventana
        frame.pack();
        frame.setVisible(true);
    }
}
