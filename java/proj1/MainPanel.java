
import javax.swing.*;
import java.awt.*;
public class MainPanel extends JPanel {
  private ColorHolder _holder;
  private ShapePanel _shapePanel;
  private ColorButtonColumn _colorButtonColumn;  
  public MainPanel() {
   super(); // default FlowLayout
   // make white default color of ColorHolder
   _holder = new ColorHolder(Color.black);  
   _shapePanel = new ShapePanel(_holder);
   _colorButtonColumn = new ColorButtonColumn(_holder);
   this.add(_shapePanel);
   this.add(_colorButtonColumn);
   this.add(new QuitButton());

  }
} // end of class ShapeColorChanger
