
import javax.swing.JFrame;

public class App {

	public App()
	{
		JFrame frame = new JFrame("Csc212");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		//frame.add(new Component());
		ColorPanel panel = new ColorPanel();
		frame.add(panel);
		
		frame.pack();
		
		frame.setVisible(true);
		
	}
	public static void main(String[] args) 
	{
		new App();
	}
}