import pkg.*;

public class starter implements InputControl {
	 static Rectangle r;
	   int tom = 1;
	   int bob = 6;

	public static void main(String args[])
		{
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			  r = new Rectangle(10, 30, 100, 200);
			r.setColor(Color.BLUE);
			r.fill();
			
		}


	public void onMouseClick(double x, double y)
	{
			
			
		if(tom<=10)
		{  
		tom=tom+1;
		r.translate(10,5);
		}

	
			

	}

			

	
}