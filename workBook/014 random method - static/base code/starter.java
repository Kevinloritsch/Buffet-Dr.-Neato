import pkg.*;

public class starter implements InputKeyControl {
		
		
        public static void main(String args[])
        {
			// please leave following line alone, necessary for keyboard input
			KeyController mC = new KeyController(Canvas.getInstance(),new starter());
			
			// enter code here
			System.out.println("Type r in the canvas to make a number from zero to nine show up.");
		
			
		}
		public void keyPress(String key)
		{
			if(key.equals("r"))
			{
			System.out.println(Canvas.rand(10));

			}
			
		}

}
