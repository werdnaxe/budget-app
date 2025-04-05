import javax.swing.*;
import java.awt.*;

public class GUI extends JFrame {

    JPanel panel = new JPanel();
    JButton button1 = new JButton("Bills");
    JButton button2 = new JButton("Food");
    JButton button3 = new JButton("Transportation");
    JButton button4 = new JButton("Entertainment");
    JButton button5 = new JButton("Misc");

    public static void main(String[] args) {
	GUI app = new GUI();
    }
}
