package u3.ventanas;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class TablaA extends JFrame {
    private JPanel contentPane;    // panelito
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

        btnCalcular.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int n = Integer.parseInt(textField.getText());
                //JOptionPane.showMessageDialog(null,"numero: " + n);
                //System.out.println(cadena);
                String cadena="";
                for (int i = 1; i <= 10; i++) {
                    cadena = cadena +   n + " X " + i + " = " + n*i + "\n";
                }
                textArea.setText("Tabla del " + n + "\n\n");
                textArea.append(cadena);
            }
        });

        String[][] teclado = {
            {"7", "8", "9"}, 
            {"4", "5", "6"},
            {"1", "2", "3"}
        };
        int m = teclado.length;    // Filas
        int n = teclado[0].length; // Columnas
        int x = 100, y= 200;       // x,y
        int ancho = 170, alto = 50; // Dimensiones del boto
        int dx = 20, dy = 60;      // separacion entre botones

        JButton[][] boton;
        boton = new JButton[m][n];
        
        for (int i = 0; i < m; i++) {
            // int l =x;
            for (int j = 0; j < n; j++) {
                boton[i][j] = new JButton(teclado[i][j]);
                boton[i][j].setBounds(x + j*(ancho+dx) , y + i*(alto+dy) , ancho, alto );
                //boton[i][j].setBounds(l,y,ancho,alto   );
                // l+=dx+ancho;  // x,y,ancho, alto
                contentPane.add(boton[i][j]);
            }
            // y=y+dy+alto;
        }


        
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(new Runnable(){
            public void run() {
                new TablaA().setVisible(true);    
            }
        });

    }
    
}
