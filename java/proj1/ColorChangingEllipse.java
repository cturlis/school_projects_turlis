
/**
 * ColorChangingEllipse has extra method to react to mouse click. It is also a client of the ColorHolder.
 * 
 * @author (Ruby) 
 */
import javax.swing.*;
import java.awt.*;
public class ColorChangingEllipse extends ColorEllipse
{
    /* reference to the spiffy object storing current color */
  private Colorable _colorHolder;
  
  public ColorChangingEllipse(JPanel container,java.awt.Color aColor, ColorHolder holder) {
	  //TODO
	  super(aColor,aColor);
	  _colorHolder = holder;
	  

  }
  public void react(){
	this.setColor(_colorHolder.getColor());
  }
  //TODO
}
