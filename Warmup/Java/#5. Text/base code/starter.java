import pkg.*;
public class starter implements InputControl, InputKeyControl 
{
		static Text josiah;
		static int key;

        public static void main(String args[])
        {
		
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			
			// please leave following line alone, necessary for keyboard input
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());
			
			System.out.println("WARNINNG!! May include a strobing effect. ");
			System.out.println("Please enter a word:");
		
			EasyReader joe_in;
			joe_in = new EasyReader();
			
			String daniel = joe_in.readLine();
			
			josiah = new Text(300,300,daniel);
			
			while(true)
			{
				josiah.grow(2,2);
				Canvas.pause(20);
				Canvas.snapshot();
				int redvalue = Canvas.rand(256);
				int greenvalue = Canvas.rand(256);
				int bluevalue = Canvas.rand(256);
				Color col = new Color(redvalue,greenvalue,bluevalue);
				josiah.setColor(col);
				josiah.draw();
				
			
		
		}
		
		public void onMouseClick(double x, double y){
			// and/or here
	
		}
		
		public void keyPress(String s)
		{
			// temp holds the enter character
			
			char done = (char)10;
			String temp = Character.toString(done);
			
		}
}
