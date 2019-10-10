import pkg.*;
public class starter implements InputControl, InputKeyControl 
{
		
		static Ellipse one;
		
		static int stop;
		static int down;
		static Color key;
		
        public static void main(String args[])
        {
		
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());	
		key = Color.BLACK;			
			
		}
		
		public void onMouseClick(double x, double y){
			one = new Ellipse (stop,down,35,35);
			one.fill();
			one.setColor(key);
			if (stop<550)
			{
			stop=stop+40;
			}
			else
			{
			down=down+40;
			stop=stop-600;
			}

			
		}
		
		public void keyPress(String s)
		{
			
			if(s.equals("r"))
			{
			key = Color.RED;
			}
		
			if(s.equals("b"))
			{
			key = Color.BLUE;
			}
			if(s.equals("p"))
			{
			key = Color.PINK;
			}
			if(s.equals("g"))
			{
			key = Color.GREEN;
			}
			if(s.equals("w"))
			{
			key = Color.WHITE;
			}
			if(s.equals("l"))
			{
			key = Color.BLACK;
			}
			if(s.equals("m"))
			{
			key = Color.MAGENTA;
			}	
			
		}
}
