
import javax.swing.*;
import java.awt.*;
public class ColorButtonColumn extends JPanel {
    private ColorButton _redButton, _greenButton, _blueButton;

    public ColorButtonColumn(ColorHolder holder) {
      super();

      this.setLayout(new GridLayout(0,1));
      _redButton = new ColorButton( "Red", Color.red, holder );
      _blueButton = new ColorButton( "Blue",  Color.blue, holder);
      _greenButton = new ColorButton( "Green", Color.green, holder);
	
      this.add(_redButton);
      this.add(_blueButton);
      this.add(_greenButton);
	
      ButtonGroup buttonGroup = new ButtonGroup();
      buttonGroup.add(_redButton);
      buttonGroup.add(_blueButton);
      buttonGroup.add(_greenButton);
    }
}
