

public class ColorEllipse extends ColorShape
{
    public ColorEllipse(java.awt.Color aBorderColor, 
			  java.awt.Color aFillColor){
	super(new java.awt.geom.Ellipse2D.Double());
	super.setBorderColor(aBorderColor);
	super.setFillColor(aFillColor);
	super.setSize(50,50);
    }
}
