package u3.ventanas;

import java.awt.*;
import javax.swing.*;

public class EjemploGridBagLayout {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Ejemplo de GridBagLayout");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();

        // Definir las propiedades comunes de los componentes
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 0.5;  // 0.5 
        gbc.weighty = 0.5;  // 0.5

        gbc.insets = new Insets(10, 10, 10, 10); // Espacio de 10 píxeles en todas direcciones


        // Agregar el primer botón en la fila 0, columna 0
        gbc.gridx = 0;
        gbc.gridy = 0;
        frame.add(new JButton("Botón 1"), gbc);

        // Agregar el segundo botón en la fila 0, columna 1
        gbc.gridx = 1;
        gbc.gridy = 0;
        frame.add(new JButton("Botón 2"), gbc);

        // Agregar el tercer botón que ocupa dos columnas en la fila 1
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        frame.add(new JButton("Botón 3"), gbc);

        // Restablecer gridwidth antes de agregar más componentes
        gbc.gridwidth = 1;

        // Agregar el cuarto botón en la fila 2, columna 0
        gbc.gridx = 0;
        gbc.gridy = 2;
        frame.add(new JButton("Botón 4"), gbc);

        // Agregar el quinto botón en la fila 2, columna 1
        gbc.gridx = 1;
        gbc.gridy = 2;
        frame.add(new JButton("Botón 5"), gbc);

        // Ajustar tamaño y mostrar la ventana
        frame.pack();
        frame.setVisible(true);
    }
}
