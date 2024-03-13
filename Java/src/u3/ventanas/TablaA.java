package u3.ventanas;

import java.awt.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class TablaA extends JFrame {
    private JPanel contentPane;
    private JTextField textField;

    public TablaA() {
        setDefaultCloseOperation(TablaA.EXIT_ON_CLOSE);
        setBounds(100, 100,450, 500);

        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5,5,5,5));
        setContentPane(contentPane);
        contentPane.setLayout(null);  // absoluto x, y

        // Agregar Componentes
        textField = new JTextField();
        textField.setBounds(100,100, 100,20);
        contentPane.add(textField);

        JButton btnCalcular = new JButton("Tabla");
        btnCalcular.setBounds(250,100, 100,20);
        contentPane.add(btnCalcular);

        JTextArea textArea = new JTextArea();
        // textArea.setBounds(150,150, 150,200);
        //contentPane.add(textArea);

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setBounds(150, 150, 150, 200);
        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
        contentPane.add(scrollPane);











        
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(new Runnable(){
            public void run() {
                new TablaA().setVisible(true);    
            }
        });

    }
    
}
