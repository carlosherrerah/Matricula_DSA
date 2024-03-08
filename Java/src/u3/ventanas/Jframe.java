package u3.ventanas;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class Jframe extends JFrame {

  private static final long serialVersionUID = 1L;
  private JPanel contentPane;
  private JTextField textField; // General
  private JTextArea textArea;

  public static void main(String[] args) {

    EventQueue.invokeLater(new Runnable() {
      public void run() {
        new Jframe().setVisible(true); // Netbeans

        /*
         * try { // Eclipse
         * Jframe frame = new Jframe();
         * frame.setVisible(true);
         * } catch (Exception e) {
         * e.printStackTrace();
         * }
         */
      }
    });

  }

  public Jframe() {
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setBounds(100, 100, 450, 300);
    contentPane = new JPanel();
    contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

    setContentPane(contentPane);
    contentPane.setLayout(null);

    // Agregar Componentes
    textField = new JTextField();
    textField.setBounds(170, 80, 120, 20);
    contentPane.add(textField);
    textField.setColumns(10);

    JButton btnCalcular = new JButton("Tabla");
    btnCalcular.setBounds(300, 80, 120, 20);
    contentPane.add(btnCalcular);

    JTextArea textArea = new JTextArea(12, 30);
    textArea.setBounds(170, 150, 120, 150);
    JScrollPane scrollPane = new JScrollPane(textArea, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
        JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
    scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

    textArea.setLineWrap(true);
    contentPane.add(scrollPane);
    contentPane.add(textArea);


    btnCalcular.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        int x = Integer.parseInt(textField.getText());
        int r = 0;
        textArea.setText("Tabla del numero: " + x + "\n\n");
        for (int i = 1; i <= 10; i++) {
          r = x * i;
          textArea.append(x + " X " + i + " = " + r + "\n");
        }

        // JOptionPane.showMessageDialog(null, "hola");

      }
    });
  }


}
