import java.awt.Color;

import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class SliderListener implements ChangeListener {
	
	private JPanel _panel;
	private int _channel;
	private JSlider _slider;
	
	public SliderListener(JPanel panel, int channel, JSlider slider) 
	{
		_panel= panel;
		_channel = channel;
		_slider = slider;
	}
	@Override
	public void stateChanged(ChangeEvent e) 
	{
		int val = _slider.getValue();
		Color bg = _panel.getBackground();
		Color newbg = null;
		
		switch(_channel) 
		{
		case 0:
			newbg = new Color(val, bg.getGreen(),bg.getBlue());
			break;
		case 1:
			newbg = new Color(bg.getRed(), bg.getGreen(),val);
			break;
		case 2:
			newbg = new Color(bg.getRed(), val,bg.getBlue());
			break;
			
		}
		_panel.setBackground(newbg);
	}
}
