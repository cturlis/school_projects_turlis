
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ShapePanel extends JPanel {
  private ColorChangingEllipse  _ellipse;

  public ShapePanel(ColorHolder _holder)  {
    super(null, true);
    this.setBackground(java.awt.Color.gray);
    this.setSize(new Dimension(250,250));
    this.setPreferredSize(new Dimension(250,250));
    
    _ellipse = new ColorChangingEllipse(this,java.awt.Color.white,_holder);
    _ellipse.setLocation(50, 50);
    _ellipse.setSize(100,100);
  
    //add mouselistener
    this.addMouseListener(new ClickListener(this));
    }
    public void paintComponent(Graphics g) {
       super.paintComponent(g);
       Graphics2D brush = (Graphics2D) g;
       
       _ellipse.draw(brush);
       _ellipse.fill(brush);
    
    }
    
    private class ClickListener implements MouseListener{
    	
    	private JPanel _panel;
    	public ClickListener(JPanel panel) {
    		_panel = panel;
    	}
		@Override
		public void mouseClicked(MouseEvent arg0) {
			// TODO Auto-generated method stub
			if (_ellipse.contains(arg0.getPoint())) {
				_ellipse.react();
				_panel.repaint();
			}
		}

		@Override
		public void mouseEntered(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseExited(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mousePressed(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseReleased(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}
    	
    }
    

}