import pkg.*;
public class starter implements InputControl, InputKeyControl 
{
		

        public static void main(String args[])
        {
		
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			
			// please leave following line alone, necessary for keyboard input
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());
			System.out.println("Please press r.");
			// Rectangle hi;
			// hi = new Rectangle(200,500,30,70);
			// hi.draw();
			int counter = 0;
			while(counter<10000)
			{
			int x1 = Canvas.rand(1230);
			int y1 = Canvas.rand(630);
			int w1 = Canvas.rand(60);
			int h1 = Canvas.rand(60);
			
			int redvalue = Canvas.rand(256);
			int greenvalue = Canvas.rand(256);
			int bluevalue = Canvas.rand(256);
			Color col = new Color(redvalue,greenvalue,bluevalue);
			Canvas.pause(3);
			Ellipse a;
			a = new Ellipse(x1,y1,w1,h1);
			a.fill();
			a.setColor(col);
			counter = counter+1;
			
			}
			
		}
		
		public void onMouseClick(double x, double y){
			// Rectangle erase = new Rectangle (
		}
		
		public void keyPress(String key)
		{
			
			
			char done = (char)10;
			String temp = Character.toString(done);
			
		}
}
