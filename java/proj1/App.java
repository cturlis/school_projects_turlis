
import javax.swing.*;
public class App extends JFrame {
 private MainPanel _mainPanel;

  public App() {
    super("Color Changer");
    
    this.setDefaultCloseOperation(EXIT_ON_CLOSE);

    _mainPanel = new MainPanel();
    this.add(_mainPanel);
    this.pack();
    this.setVisible(true);

  }
  public static void main( String[] argv ) {
    App app = new App();
  }
} // end of class App