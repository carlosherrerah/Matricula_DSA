package u3.ventanas;

import javax.swing.*;
import java.awt.*;

public class GridLayoutExample extends JFrame {
    
    public GridLayoutExample() {
        setTitle("GridLayout Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear el GridLayout con espacio entre los componentes
        GridLayout gridLayout = new GridLayout(3, 3);
        gridLayout.setHgap(10); // Espacio horizontal entre componentes
        gridLayout.setVgap(10); // Espacio vertical entre componentes

        // Establecer el layout del JFrame como GridLayout
        setLayout(gridLayout);

        // Agregar botones al JFrame
        for (int i = 1; i <= 9; i++) {
            JButton button = new JButton("Button " + i);
            add(button);
        }

        pack();
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(GridLayoutExample::new);
    }
}
