package u3.ventanas;
import java.awt.*;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class Tabla extends JFrame {
    private JPanel contentPane;
    private JTextField textField;

    public TablaJ(){ //constructor
        setDefaultCloseOperation(Tabla.EXIT_ON_CLOSE);
        setBounds (100, 100,450, 500);
        
        contentPane = new JPanel ();
        contentPane.setBorder(new EmptyBorder(5,5,5,5));

        setContentPane (contentPane);
        contentPane.setLayout(null);;  //absoluto x,y 

        //Agregar los componentes
        textfield = new JTexField();
        textField.setBounds(100, 100, 100, 20);
        contentPane.add(textField);

        JButton btnCalcular = new JButton("Tabla");
        btnCalcular.setBounds(250, 100, 100, 20);
        contentPane.add(btnCalcular);

        JTextArea textArea = new JTextArea();
        //textArea.setBounds(150, 150, 150, 200);
        //contentPane.add (textArea);

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setBounds(150, 150, 150, 200);

        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
        contentPane.add(scrollPane);






    }

    public static void main (String [] args){
        EventQueue.invokeLater (new Runnable(){
            public void run (){
                new Tabla ().setVisible (true);

            }
        });
    }
}