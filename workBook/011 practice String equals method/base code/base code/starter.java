import pkg.*;

public class starter implements InputKeyControl {
		
			static Rectangle r;
        public static void main(String args[])
        {
			KeyController mC = new KeyController(Canvas.getInstance(),new starter());
			r = new Rectangle (20,20,20,20);
			r.draw();
			
			
		}
		public void keyPress(String key)
		{
			if(key.equals("d"))
			{
			System.out.println("I love food");
			r.translate(20,0);
			}
		
			if(key.equals("a"))
			{
			System.out.println("I do not love food");
			r.translate(-20,0);
			}
		}

}
