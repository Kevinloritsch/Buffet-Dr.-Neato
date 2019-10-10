import pkg.*;
public class starter implements InputControl, InputKeyControl 
{
		static Line joe;
		static Line bob;
		static Line fred;
		static String jackson;
		static EasyReader joe_in;

        public static void main(String args[])
        {
		
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			
			// please leave following line alone, necessary for keyboard input
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());
			System.out.println("Would you like a triangle (input the letter t)?");
			joe_in = new EasyReader();
			jackson = joe_in.readWord();
			
			
			
		}
		
		public void onMouseClick(double x, double y)
		{
			
						int t = Canvas.rand(1000);
						int r = Canvas.rand(1000);
						int i = Canvas.rand(1000);
						int a = Canvas.rand(1000);
						int n = Canvas.rand(1000);
						int g = Canvas.rand(1000);
						int l = Canvas.rand(1000);
						
						int e = Canvas.rand(1000);
						
			
				if (jackson == x)
				{
					
				}
				if (jackson.equals("t")) 
				{
						joe = new Line (t, r, i, a);
						joe.draw();
						bob = new Line (i, a, n, g);
						bob.draw();
						fred = new Line (n, g, t, r);
						fred.draw();
				}
	
		}
		
		public void keyPress(String key)
		{
			
		}
 }
