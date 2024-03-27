package u3.ventanas;

import javax.swing.*;
import javax.swing.border.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TablaB extends JFrame {

    public TablaB() {
        setDefaultCloseOperation(TablaB.EXIT_ON_CLOSE);
        setBounds(100, 100, 400, 500);
        JPanel panelito = new JPanel();
        panelito.setBorder(new EmptyBorder(5,5,5,5));
        setContentPane(panelito);
        panelito.setLayout(null); /* // layout absoluto x,y

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
        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);    
        panelito.add(scrollPane);    

        btnCalcular.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                //JOptionPane.showMessageDialog(null,"Valor de: " + n);
                int n = Integer.parseInt(textField.getText());
                String cadena="";
                for (int i = 1; i <= 10; i++) {
                    cadena = cadena + n + " X " + i + " = " + n*i + "\n";
                }
                textArea.setText("Tabla del: " + n + "\n\n");
                textArea.append(cadena);

            }
        }); */
        
        String[][] teclado = {
            {"7", "8", "9", "+"},
            {"4", "5", "6", "-"},
            {"1", "2", "3", "="}
        };

        int m = teclado.length;
        int n = teclado[0].length;
        int x = 100, y = 200;      // punto de partida
        //int v=x;
        int ancho= 70, alto = 50;  // tamaño del boton
        int dx = 20, dy = 10;      // separacion entre botones

        JButton[][] botones;
        botones = new JButton[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j <n; j++) {
                botones[i][j] = new JButton(teclado[i][j]);
                botones[i][j].setBounds(x+j*(ancho+dx), y+i*(alto+dy), ancho, alto);  //linea de oro
                panelito.add(botones[i][j]);
                //x= x+ancho+dx;
            }
            //x=v;
            //y= y+alto+dy;
        } 

    }

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run(){
                new TablaB().setVisible(true);
            }
        });
    }
}
