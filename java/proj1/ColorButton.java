
import javax.swing.*;
import java.awt.*;
public class ColorButton extends JRadioButton {
    private ColorHolder _colorHolder;
    private Color _thisColor;
    public ColorButton( String label, Color color, ColorHolder holder ) {
        super( label );
        _colorHolder = holder;
        _thisColor = color;
     
        this.addActionListener(new ColorListener());
    }
    private class ColorListener implements java.awt.event.ActionListener{
        public void actionPerformed( java.awt.event.ActionEvent e){
        //TODO
        	_colorHolder.setColor(_thisColor);
        }
    }
}
