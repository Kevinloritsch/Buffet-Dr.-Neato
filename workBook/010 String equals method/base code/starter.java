import pkg.*;

public class starter implements InputKeyControl {
		
			static Rectangle r;
        public static void main(String args[])
        {
			KeyController mC = new KeyController(Canvas.getInstance(),new starter());
			r = new Rectangle (20,20,20,20);
			r.draw();
			
			
		}
		public void keyPress(String s)
		{
			if(s.equals("d"))
			{
			System.out.print("I love food");
			r.translate(0,20);
			}
		}

}
