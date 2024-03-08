package u3.ventanas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Scroll{
    private JFrame f; //Main frame
    private JTextArea ta; // Text area
	private JScrollPane sbrText; // Scroll pane for text area
    private JButton btnQuit; // Quit Program
    
    public Scroll(){ //Constructor
        // Create Frame
        f = new JFrame("Swing Demo");
		f.getContentPane().setLayout(new FlowLayout());
        
        // Create Scrolling Text Area in Swing
        ta = new JTextArea("", 5, 50);
		ta.setLineWrap(true);
		sbrText = new JScrollPane(ta);
		sbrText.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        
		// Create Quit Button
        btnQuit = new JButton("Quit");
        btnQuit.addActionListener(
			new ActionListener(){
				public void actionPerformed(ActionEvent e){
					System.exit(0);         
				}
			}
		);
        
    }

    public void launchFrame(){ // Create Layout
        // Add text area and button to frame
		f.getContentPane().add(sbrText);
        f.getContentPane().add(btnQuit);
		
		 // Close when the close button is clicked
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		//Display Frame
        f.pack(); // Adjusts frame to size of components
        f.setVisible(true);
    }
    
    public static void main(String args[]){
        Scroll gui = new Scroll();
        gui.launchFrame();
    }
}