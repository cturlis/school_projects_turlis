import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JPanel;
import javax.swing.JSlider;

public class ColorPanel extends JPanel {
	
	public ColorPanel() 
	{
		Dimension panelSize = new Dimension(300,150);
		this.setPreferredSize(panelSize);
		this.setBackground(Color.white);
		JSlider sliderRed = new JSlider(0,255);
		JSlider sliderGreen = new JSlider(0,255);
		JSlider sliderBlue = new JSlider(0,255);
		
		sliderRed.addChangeListener(new SliderListener(this, 0, sliderRed));
		sliderGreen.addChangeListener(new SliderListener(this, 2, sliderGreen));
		sliderBlue.addChangeListener(new SliderListener(this, 1, sliderBlue));
		
	
		this.add(sliderRed);
		this.add(sliderBlue);
		this.add(sliderGreen);
			}
}
