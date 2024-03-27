package u3.ventanas;

import javax.swing.*;
import javax.swing.border.*;
import java.awt.*;

public class Tabla_AB extends JFrame {

    public Tabla_AB() {
        setDefaultCloseOperation(Tabla_AB.EXIT_ON_CLOSE);
        setBounds(100, 100, 400, 500);
        JPanel panelito = new JPanel();
        panelito.setBorder(new EmptyBorder(5,5,5,5));
        setContentPane(panelito);
        panelito.setLayout(null);  // layout absoluto x,y

        String[][] teclado = {
            {"7","8","9"},
            {"4","5","6"},
            {"1","2","3"},
            {"0",".","="}
        };
        int m = teclado.length;
        int n = teclado[0].length;
        int x=   100,    y=200;    // punto de partida
        int ancho=70, alto= 50;    // Dimensiones del boton 
        int dx=   20,   dy= 10;    // separacion entre botones  

        JButton[][] boton;
        boton = new JButton[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                boton[i][j] = new JButton(teclado[i][j]);
                boton[i][j].setBounds(x + j*(ancho+dx), y + i*(alto+dy), ancho, alto); 
                panelito.add(boton[i][j]);
            }
        }
        System.out.println(boton[1][2].getText());

        // Agregar Componentes
        JTextField textField = new JTextField();
        textField.setBounds(100, 100, 100,25);
        panelito.add(textField);

        JButton btnCalcular = new JButton("Tabla");
        btnCalcular.setBounds(250, 100, 100, 25); 
        panelito.add(btnCalcular);

        JTextArea textArea = new JTextArea();
        //textArea.setBounds(150, 150, 150, 200);
        //panelito.add(textArea);

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setBounds(150, 150, 150, 200);
        panelito.add(scrollPane);    
        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);    

        
    }

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run(){
                new Tabla_AB().setVisible(true);
            }
        });
    }
}
