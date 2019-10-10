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
			if(key.equals("w"))
			{
			System.out.println("I am food");
			r.translate(0,-20);
			}
			if(key.equals("s"))
			{
			System.out.println("I am not food");
			r.translate(0,20);
			}
		}

}
