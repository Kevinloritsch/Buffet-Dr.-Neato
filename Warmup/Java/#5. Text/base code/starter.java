import pkg.*;
public class starter implements InputControl, InputKeyControl 
{
		static Text josiah;
		static int key;
		static Ellipse one;
		static int counter = 0;
		static int stop;
		static int down;

		public void onMouseClick(double x, double y)
		{
		
		if(counter == 0)
		{
			counter = counter + 1;
		}
		else
		{
			counter = 0;
		}
	
		}
        public static void main(String args[])
        {
		
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			
			// please leave following line alone, necessary for keyboard input
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());
			System.out.println("WARNINNG!! May include a strobing effect. ");
			System.out.println("Please enter a word or phrase (shorter is recommended):");
			
			EasyReader joe_in;
			joe_in = new EasyReader();
			
			String daniel = joe_in.readLine();
			
			josiah = new Text(300,300,daniel);
			
			while(counter == 0)
			{
			
				josiah.grow(8,8);
				Canvas.pause(0);
				Canvas.snapshot();
				int redvalue = Canvas.rand(256);
				int greenvalue = Canvas.rand(256);
				int bluevalue = Canvas.rand(256);
				Color col = new Color(redvalue,greenvalue,bluevalue);
				josiah.setColor(col);
				josiah.draw();
			}
		}
		
		
		
		public void keyPress(String s)
		{
			if(s.equals("r"))
			{
			josiah.grow(-80,-80);
			}
			
		}
}