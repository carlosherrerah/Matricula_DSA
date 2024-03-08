package u3.ventanas;

import org.jdatepicker.impl.JDatePanelImpl;
import org.jdatepicker.impl.JDatePickerImpl;
import org.jdatepicker.impl.UtilDateModel;

import javax.swing.*;
import java.awt.*;
import java.util.Calendar;
import java.util.Date;
import java.util.Properties;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class DatePicker {
    public static void main(String[] args) {
        // Crear un nuevo modelo de fecha
        UtilDateModel model = new UtilDateModel();
        // Crear un objeto de propiedades
        Properties properties = new Properties();
        // Configurar el formato de fecha
        properties.put("text.today", "Today");
        properties.put("text.month", "Month");
        properties.put("text.year", "Year");
        // Crear un panel de fecha
        JDatePanelImpl datePanel = new JDatePanelImpl(model, properties);
        // Crear el selector de fecha
        JDatePickerImpl datePicker = new JDatePickerImpl(datePanel, new DateLabelFormatter());

        // Crear un botón para mostrar la fecha seleccionada
        JButton button = new JButton("Mostrar Fecha Seleccionada");

        // Crear un marco y agregar el selector de fecha
        JFrame frame = new JFrame("Date Picker Example");
        frame.setLayout(new FlowLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(datePicker);
        frame.add(button);
        frame.pack();
        frame.setVisible(true);

        // Agregar un ActionListener al botón
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Obtener la fecha seleccionada del modelo
                Date selectedDate = (Date) datePicker.getModel().getValue();
                // Mostrar un mensaje con la fecha seleccionada
                JOptionPane.showMessageDialog(frame, "Fecha Seleccionada: " + selectedDate);
            }
        });
    }

    // Clase para formatear la etiqueta de la fecha
    static class DateLabelFormatter extends JFormattedTextField.AbstractFormatter {
        private final String datePattern = "yyyy-MM-dd";
        private final java.text.SimpleDateFormat dateFormatter = new java.text.SimpleDateFormat(datePattern);

        @Override
        public Object stringToValue(String text) throws java.text.ParseException {
            return dateFormatter.parseObject(text);
        }

        @Override
        public String valueToString(Object value) throws java.text.ParseException {
            if (value != null) {
                Calendar cal = (Calendar) value;
                return dateFormatter.format(cal.getTime());
            }
            return "";
        }
    }
}
