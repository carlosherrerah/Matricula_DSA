package u3.ventanas;

import javax.swing.*;
import java.awt.*;

public class GridBagLayoutExample extends JFrame {
    public GridBagLayoutExample() {
        setTitle("GridBagLayout Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear el GridBagLayout
        GridBagLayout gridBagLayout = new GridBagLayout();
        setLayout(gridBagLayout);

        // Crear GridBagConstraints para configurar el espacio entre componentes
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10); // Espacio entre componentes (arriba, izquierda, abajo, derecha)

        // Agregar botones al JFrame con GridBagConstraints
        for (int i = 0; i < 9; i++) {
            JButton button = new JButton("Button " + i);
            gbc.gridx = i % 3; // Columna
            gbc.gridy = i / 3; // Fila
            add(button, gbc);
        }

        pack();
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(GridBagLayoutExample::new);
    }
}
